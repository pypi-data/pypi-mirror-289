from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="DrugTargetTool",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
        "deap",
        "numpy",
    ],
    entry_points={
        'console_scripts': [
            'drugtargettool=drugtargettool.main:combination_therapy',
        ],
    },
    author="Seyedeh Sadaf Asfa & Reza Arshinchi Bonab",
    description="Genetic Algorithm Based Combination Therapy Finder",
    long_description=long_description,
    long_description_content_type="text/markdown",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
