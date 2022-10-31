from setuptools import setup,find_packages
from typing import List

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR= "Aditya Jadhav"
DESRCIPTION = "This is the housing predictor project"

REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:

    """
    Descripition :This function is going to return the list of requirements mention in requirements.txt files
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_files:
        return requirement_files.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)