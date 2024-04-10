from setuptools import find_packages,setup
from typing import List

from setuptools.sandbox import save_path

HYPEN_E_DOT='-e  .'
def get_requirements(file_patth:str)->List[str]:
      '''
      This function will return the list of requirements 
      '''  
def process_requirements(save_path):
    requirements = []
    with open(save_path) as file_obj:
        requirements = file_obj.readline().strip().split(',')
        requirements = [req.strip() for req in requirements]

        if "HYPEN_E_DOT" in requirements:
            requirements.remove("HYPEN_E_DOT")

    return requirements

setup(
    name='mlproject2',
    version='0.0.1',
    author='sam', 
    author_email='oluwatemitopesam@gamil.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.text')

   ) 