# setup.py
from setuptools import setup, find_packages

setup(
    name="pymovavg",              
    version="0.2",                  
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
    extras_require={
        'test': ['unittest']
    },          
    description="A simple Python library to calculate moving averages",
    author="Galang Latief",
    author_email="galangallatief@gmail.com",
    url="https://github.com/GalangLatief/pymovavg", 
    license="MIT",                  
    classifiers=[                   
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',        
)
