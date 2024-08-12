import os
import logging
import importlib
import subprocess
import sys
import threading
import time
from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor
from io import BytesIO

# installer tesseract
# installer poppler

cdef int threads_rest = 1
cdef int nb_phrases_avant = 10
cdef int nb_phrases_apres = 10
cdef int taille = 20
cdef int TIMEOUT = 200
cdef str TESSERACT_CMD = ""
cdef str input_path = ""
cdef str output_path = ""

cdef list KEYWORDS = []

max_threads = os.cpu_count() - threads_rest
os.environ['NUMEXPR_MAX_THREADS'] = str(max_threads)
FILE_SIZE_LIMIT = taille * 1024 * 1024

def configurer_parametres(int new_threads_rest=1, int new_nb_phrases_avant=10, int new_nb_phrases_apres=10, int new_taille=1, int new_TIMEOUT=200, str new_TESSERACT_CMD="", str new_input_path="", str new_output_path = "", list new_KEYWORDS=[]):
    global threads_rest, nb_phrases_avant, nb_phrases_apres, taille, TIMEOUT, TESSERACT_CMD, input_path, output_path, KEYWORDS, max_threads, FILE_SIZE_LIMIT
    
    if not new_KEYWORDS:
        raise ValueError("La liste des mots-clés (KEYWORDS) ne peut pas être vide. Veuillez fournir une liste valide")
    if new_output_path is None or not os.path.isdir(new_output_path ) :
        raise ValueError("Veuillez définir un output_path")
    if  new_input_path is None or not os.path.isdir(new_input_path):
        raise ValueError("Veuillez définir un input_path")
    if  new_TESSERACT_CMD is None :
        raise ValueError("Veuillez définir le chemin vers tesseract")

    
    threads_rest = new_threads_rest
    nb_phrases_avant = new_nb_phrases_avant
    nb_phrases_apres = new_nb_phrases_apres
    taille = new_taille
    TIMEOUT = new_TIMEOUT
    TESSERACT_CMD = new_TESSERACT_CMD
    input_path = new_input_path
    output_path = new_output_path
    KEYWORDS = new_KEYWORDS
    max_threads = os.cpu_count() - threads_rest
    os.environ['NUMEXPR_MAX_THREADS'] = str(max_threads)
    FILE_SIZE_LIMIT = taille * 1024 * 1024


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def install_and_import(package, import_name=None):
    try:
        if import_name is None:
            importlib.import_module(package)
        else:
            importlib.import_module(import_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
    finally:
        if import_name is None:
            return importlib.import_module(package)
        else:
            return importlib.import_module(import_name)

json = install_and_import('json')


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

pdfplumber = install_and_import('pdfplumber')
pd = install_and_import('pandas')
spacy = install_and_import('spacy')
pytesseract = install_and_import('pytesseract')
PIL = install_and_import('Pillow', 'PIL')  
openpyxl = install_and_import('openpyxl')
pdf2image = install_and_import('pdf2image')
pandoc = install_and_import('pandoc')
pypandoc = install_and_import('pypandoc')
reportlab = install_and_import('reportlab')
re = install_and_import('re')

from docx import Document # type: ignore
from pdf2image import convert_from_bytes# type: ignore
from reportlab.lib.pagesizes import A4# type: ignore
from reportlab.lib.units import inch# type: ignore
from reportlab.lib.styles import getSampleStyleSheet# type: ignore
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer# type: ignore

Event = threading.Event
Image = PIL.Image

try:
    nlp = spacy.load("fr_core_news_lg")
except OSError:
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "fr_core_news_lg"])
    nlp = spacy.load("fr_core_news_lg")










def extraire_phrases(texte, mot_clé):
    doc = nlp(texte)
    phrases_avec_contexte = []
    phrases = list(doc.sents)
    for i, sent in enumerate(phrases):
        if mot_clé.lower() in sent.text.lower():
            start = max(0, i - nb_phrases_avant)
            end = min(len(phrases), i + nb_phrases_apres + 1)
            phrases_contexte = [s.text for s in phrases[start:end]]
            phrases_avec_contexte.append(" ".join(phrases_contexte))
    return phrases_avec_contexte

def compter_mots(phrase):
    return len(phrase.split())

def effectuer_ocr(image):
    return pytesseract.image_to_string(image, lang='fra')

def extraire_blocs_texte(page):
    blocs = []
    if page.extract_text():
        for bloc in page.extract_words():
            blocs.append({
                'x0': bloc['x0'],
                'top': bloc['top'],
                'x1': bloc['x1'],
                'bottom': bloc['bottom'],
                'text': bloc['text']
            })
    return blocs

def extraire_ocr_des_images(page, bbox):
    try:
        image_page = page.to_image(resolution=300).original
        width, height = image_page.size
        x0, y0, x1, y1 = bbox
        x0, y0, x1, y1 = max(0, x0), max(0, y0), min(x1, width), min(y1, height)
        image_recadree = image_page.crop((x0, y0, x1, y1))
        return effectuer_ocr(image_recadree)
    except Exception as e:
        if str(e) != "tile cannot extend outside image":
            logging.error(f"Erreur lors de l'extraction OCR de l'image: {str(e)}")
        return ""

def traiter_page(page, id_dossier, fichier, num_page):
    data = []
    pages_problematiques = []
    logging.info(f"Traitement de la page {num_page} du fichier {fichier} dans le dossier {id_dossier}")
    try:
        blocs_texte = extraire_blocs_texte(page)
        for img in page.images:
            x0, y0, x1, y1 = img["x0"], img["top"], img["x1"], img["bottom"]
            texte_ocr = extraire_ocr_des_images(page, (x0, y0, x1, y1))
            if texte_ocr:
                blocs_texte.append({
                    'x0': x0,
                    'top': y0,
                    'x1': x1,
                    'bottom': y1,
                    'text': texte_ocr
                })
        blocs_texte.sort(key=lambda x: (x['top'], x['x0']))
        texte_complet = " ".join([bloc['text'] for bloc in blocs_texte])
        if texte_complet:
            for mot_clé in KEYWORDS:
                phrases = extraire_phrases(texte_complet, mot_clé)
                for phrase in phrases:
                    data.append({
                        'Dossier_PDF': id_dossier,
                        'Document_PDF': fichier,
                        'Num_Page': num_page,
                        'Mots_Clés_Trouvés': mot_clé,
                        'Longueur_Phrase_Conteint_Mots_Clés': compter_mots(phrase),
                        'Info': phrase
                    })
    except Exception as e:
        logging.error(f"Erreur lors du traitement de la page {num_page} du fichier {fichier}: {str(e)}")
        pages_problematiques.append(num_page)
    return data, pages_problematiques

def convertir_en_docx_in_memory(doc_path):
    try:
        temp_docx_path = doc_path.rsplit('.', 1)[0] + '_temp.docx'
        
        pypandoc.convert_file(doc_path, 'docx', outputfile=temp_docx_path)
        

        with open(temp_docx_path, 'rb') as f:
            docx_buffer = BytesIO(f.read())
        
        os.remove(temp_docx_path)
        
        return docx_buffer
    
    except Exception as e:
        logging.error(f"Erreur lors de la conversion de {doc_path} en DOCX en mémoire: {str(e)}")
        return None


def convertir_docx_en_pdf_en_memoire(docx_path):
    try:
        doc = Document(docx_path)
        pdf_buffer = BytesIO()
        pdf = SimpleDocTemplate(pdf_buffer, pagesize=A4)
        styles = getSampleStyleSheet()
        elements = []

        for para in doc.paragraphs:
            text = para.text
            style = styles['Normal']
            p = Paragraph(text, style)
            elements.append(p)
            elements.append(Spacer(1, 0.2 * inch)) 

        pdf.build(elements)
        pdf_buffer.seek(0)  
        return pdf_buffer.read()
    
    except Exception as e:
        logging.error(f"Erreur lors de la conversion en PDF en mémoire: {str(e)}")
        return None

def traiter_fichier_pdf(args):
    chemin_pdf, id_dossier, fichier = args
    logging.info(f"Traitement du fichier {fichier} dans le dossier {id_dossier}")
    data = []
    pages_problematiques = []
    try:
        if chemin_pdf.endswith(('.rtf','.odt')):
            docx_buffer = convertir_en_docx_in_memory(chemin_pdf)
            if docx_buffer is None:
                raise Exception(f"Erreur lors de la conversion du fichier {fichier} en DOCX")
            pdf_bytes = convertir_docx_en_pdf_en_memoire(docx_buffer)
            if pdf_bytes is None:
                raise Exception(f"Erreur lors de la conversion du fichier DOCX en mémoire")
        elif chemin_pdf.endswith('.docx'):
            pdf_bytes = convertir_docx_en_pdf_en_memoire(chemin_pdf)
            if pdf_bytes is None:
                raise Exception(f"Erreur lors de la conversion du fichier DOCX {chemin_pdf}")
        else:
            with open(chemin_pdf, "rb") as f:
                pdf_bytes = f.read()

        images = convert_from_bytes(pdf_bytes)
        
        for num_page, image in enumerate(images, start=1):
            with pdfplumber.open(BytesIO(pdf_bytes)) as pdf:
                page = pdf.pages[num_page - 1]
                with ThreadPoolExecutor(max_workers=1) as page_executor:
                    future = page_executor.submit(traiter_page, page, id_dossier, fichier, num_page)
                    try:
                        page_data, problematic_pages = future.result(timeout=TIMEOUT)
                        data.extend(page_data)
                        pages_problematiques.extend(problematic_pages)
                    except Exception as e:
                        logging.error(f"Timeout ou erreur lors du traitement de la page {num_page} du fichier {fichier}: {str(e)}")
                        pages_problematiques.append(num_page)
    except Exception as e:
        logging.error(f"Erreur à l'ouverture du fichier {chemin_pdf}: {str(e)}")
        return None, {'Dossier_PDF': id_dossier, 'Document_PDF': fichier, 'Issue': str(e)}
    
    if pages_problematiques:
        issue_description = f'Délai dépassé ou erreur sur les pages {", ".join(map(str, pages_problematiques))}'
        return data, {'Dossier_PDF': id_dossier, 'Document_PDF': fichier, 'Issue': issue_description}
    
    data.sort(key=lambda x: x['Num_Page'])
    return data, None

def nettoyer_donnees(dataframe):

    def clean_cell(cell):
        if isinstance(cell, str):  
            cleaned = cell.replace('=', '').replace('+', '').replace('-', '').replace('@', '').replace('{', '').replace('}', '')
            cleaned = re.sub(r'[^\x00-\x7F]+', '', cleaned) 
            return cleaned.strip()
        return cell 

    for col in dataframe.columns:
        if dataframe[col].dtype == 'object':
            dataframe.loc[:, col] = dataframe[col].apply(clean_cell)

    return dataframe


data = []
heavy_or_slow_files = []

def generer_tables_contingence(data):
    df_data = pd.DataFrame(data)
    tables_contingence = {}
    for id_dossier, group in df_data.groupby('Dossier_PDF'):
        table = group.pivot_table(
            index='Document_PDF',
            columns='Mots_Clés_Trouvés',
            values='Longueur_Phrase_Conteint_Mots_Clés',
            aggfunc='count',
            fill_value=0
        )
        tables_contingence[id_dossier] = table
    return tables_contingence

def enregistrer_tables_contingence(tables_contingence, output_path):
    excel_path = os.path.join(output_path, "tables_conteingences.xlsx")
    with pd.ExcelWriter(excel_path) as writer:
        for id_dossier, table in tables_contingence.items():
            table.to_excel(writer, sheet_name=id_dossier[:31])
    logging.info(f"Les tables de contingence ont été enregistrées dans {excel_path}")

def main():
    start_time = time.time()
    pdf_files = []
    resultat_path = output_path

    os.makedirs(resultat_path, exist_ok=True)
    for racine, dossiers, fichiers in os.walk(input_path):
        for fichier in fichiers:
            chemin_complet = os.path.join(racine, fichier)
            id_dossier = os.path.basename(racine)
            taille_fichier = os.path.getsize(chemin_complet)

            if fichier.endswith(('.docx', '.odt', '.pdf', '.rtf')):
                chemin_pdf = chemin_complet
            else:
                logging.warning(f"Fichier ignoré car non supporté: {fichier}")
                heavy_or_slow_files.append({
                    'Dossier_PDF': id_dossier,
                    'Document_PDF': fichier,
                    'Issue': f"Le fichier est en format {os.path.splitext(fichier)[1]}, veuillez convertir en .docx / .odt / .pdf / .rtf"
                })
                continue

            if taille_fichier > FILE_SIZE_LIMIT:
                logging.warning(f"Fichier ignoré car trop volumineux: {fichier}")
                heavy_or_slow_files.append({
                    'Dossier_PDF': id_dossier,
                    'Document_PDF': fichier,
                    'Issue': f'Fichier supérieur à {taille} MB'
                })
                continue
            
            pdf_files.append((chemin_pdf, id_dossier, fichier))
    
    with ProcessPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(traiter_fichier_pdf, pdf_file): pdf_file for pdf_file in pdf_files}
        for future in as_completed(futures):
            pdf_file = futures[future]
            try:
                file_data, issue = future.result()
                if file_data:
                    data.extend(file_data)
                if issue:
                    heavy_or_slow_files.append(issue)
            except Exception as e:
                chemin_pdf, id_dossier, fichier = pdf_file
                logging.error(f"Erreur lors du traitement du fichier {fichier}: {str(e)}")
                heavy_or_slow_files.append({'Dossier_PDF': id_dossier, 'Document_PDF': fichier, 'Issue': str(e)})

    data.sort(key=lambda x: (x['Document_PDF'], x['Num_Page']))


    if data:
        tables_contingence = generer_tables_contingence(data)
        enregistrer_tables_contingence(tables_contingence, resultat_path)
    else:
        logging.error("Il n'y a aucun document contenant les mots-clés ! Veuillez vérifier vos mots-clés =)")
        sys.exit(1)

    df = pd.DataFrame(data, columns=['Dossier_PDF', 'Document_PDF', 'Num_Page', 'Mots_Clés_Trouvés', 'Longueur_Phrase_Conteint_Mots_Clés', 'Info'])
    df =nettoyer_donnees(df)
    df_heavy_or_slow = pd.DataFrame(heavy_or_slow_files, columns=['Dossier_PDF', 'Document_PDF', 'Issue'])

    df_heavy_or_slow = df_heavy_or_slow.drop_duplicates()

    df_path = os.path.join(resultat_path, "df.xlsx")
    heavy_or_slow_df_path = os.path.join(resultat_path, "heavy_or_slow_df.xlsx")
    df.to_excel(df_path, index=False)
    df_heavy_or_slow.to_excel(heavy_or_slow_df_path, index=False)

    logging.info(f"Les résultats ont été enregistrés dans {resultat_path}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f"Le script a pris {elapsed_time:.2f} secondes pour s'exécuter.")

if __name__ == "__main__":
    main(output_path)
