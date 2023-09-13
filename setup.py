from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    '''
    This func will return a list of python libraries.
    '''

    HYPEN_E_DOT = "-e ."

    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [ req.replace('\n',' ') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name = "ETN Machine Learning Project",
    version= "0.0.1",
    author= "Muhammad Farhan",
    author_email="mfarhanzafrani@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)