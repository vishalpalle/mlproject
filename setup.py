from setuptools import find_packages,setup
from typing import List
Hyphen_dot_e = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        reuirements = file_obj.readlines()
        requirements= [req.replace ("\n" , " ")for req in requirements]

        if Hyphen_dot_e in requirements:
            requirements.remove(Hyphen_dot_e)
    return requirements

setup(
    name ='mlproject',
    version = '0.0.1',
    author='Vishal',
    author_email='pallevishal2@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)