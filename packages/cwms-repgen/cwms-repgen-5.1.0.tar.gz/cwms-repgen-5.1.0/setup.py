from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cwms-repgen",  
    version="5.1.0", 
    author="USACE-HEC, Charles Graham", 
    description='''This is a partial copy of HEC's (Hydrologic Engineering Center) repgen program.
The program creates fixed form text reports from a time series database, and textfiles.''',
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url="https://github.com/USACE-WaterManagement/repgen5", 
    packages=find_packages(where="repgen"),
    package_dir={"": "repgen"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', 
    install_requires=[
        "pytz>=2022.1"
    ],
    extras_require={
        "dev": [
            "sphinx",
            "sphinx_rtd_theme",
            "myst-parser",
            "sphinx-copybutton",
        ],
    },
    entry_points={
        "console_scripts": [
            "repgen5=repgen5:main", 
            "repgen=repgen5:main", 
        ],
    },
)
