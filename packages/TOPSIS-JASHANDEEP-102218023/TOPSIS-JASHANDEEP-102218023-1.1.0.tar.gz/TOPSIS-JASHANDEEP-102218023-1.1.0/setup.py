import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README1.md").read_text()

# This call to setup() does all the work
setup(
    name="TOPSIS-JASHANDEEP-102218023",
    version="1.1.0",
    description="This Python package implements the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) for multi-criteria decision-making.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Jashandeep Singh",
    author_email="jashandeepgarry2003@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        
        
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
)