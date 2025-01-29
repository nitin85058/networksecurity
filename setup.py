from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    "This function will retur list of requirments"
    requirement_list:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            # process each line
            for line in lines:
                requirement=line.strip()
                if requirement and requirement !='-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError :
        print("requirements.txt is not found")
    return requirement_list

setup(
    name='Network Security',
    version="0.0.1",
    author="Nitin Jaiswal",
    author_email="nitinjai9315@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)