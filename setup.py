from setuptools import find_packages, setup  # type: ignore
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(  # type: ignore
    name='mlproject',
    version='0.0.1',
    author='Swaminathan',
    author_email='lokeshnarasimhan824@gmail.com',
    packages=find_packages(),  # ✅ Added missing comma
    install_requires=get_requirements('requirements.txt')  # ✅ Now valid
)
