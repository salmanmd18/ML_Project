from webbrowser import get
from setuptools import setup
from typing import List

#Declaring varialbles for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Salman"
DESCRIPTION = "This is a first fsds Nov batch Machine Learning Project"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"



def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file

    return: This function is going to return a list which contain name of libraries mention in requirements.txt file

    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        requirements_file.readlines()



setup(
name = PROJECT_NAME,
version = VERSION,
author=AUTHOR,
packages=PACKAGES,
install_requires = get_requirements_list()
)


if __name__=="__main__":
    print(get_requirements_list())
    