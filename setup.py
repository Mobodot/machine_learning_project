from setuptools import setup, find_packages
from typing import List


def get_requirements_list() -> List[str]:
    """
    Description: this function will return list of requirements
    mention in requirements.txt file

    :return: This function is going to return a list which contain names
    of libraries  mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")


# declaring variables ofr setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "mobo"
DESCRIPTION = "This is the first FSDS Nov batch Machine Learning Project"
PACKAGES = find_packages()
REQUIREMENTS_FILE_NAME="requirements.txt"


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)


