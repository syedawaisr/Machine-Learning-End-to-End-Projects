from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='signature_validation_project',
    version='0.0.1',
    packages=find_packages(),  # Automatically find packages in the current directory
    # Add more metadata like author, description, etc.
    author='Awais Raza',
    description='This pacakge is a project for signature reidentification using basic image processing techniques',
    # Add other relevant metadata
)
