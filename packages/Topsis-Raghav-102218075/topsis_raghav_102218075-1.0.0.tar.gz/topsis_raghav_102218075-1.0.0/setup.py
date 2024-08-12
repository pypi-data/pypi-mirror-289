import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="Topsis-Raghav-102218075",
    version="1.0.0",
    description="This package implements the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method.",
    long_description=README,
    long_description_content_type="text/markdown", 
    url="https://github.com/raghavsharma2865/Topsis-Raghav-102218075", 
    author="Raghav Sharma",
    author_email="raghavsharma2865@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=["topsis"], 
    include_package_data=True,
    install_requires=[
        "pandas>=1.0",
        "numpy>=1.18"
    ],
    entry_points={
        "console_scripts": [
            "",  
        ]
    },
)
