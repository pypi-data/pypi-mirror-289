from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("find_keyword_xtvu", ["find_keyword.pyx"])
]

setup(
    name="find_keyword_xtvu",
    version="2.0",
    ext_modules=cythonize(extensions),
    author="Xuan Tung VU",
    description="A package to find keywords in .pdf, .docx, .odt, and .rtf files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xtvu2207/find_keyword.git",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Cython",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.10', 
)