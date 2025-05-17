'''
The setup file is essential part of packaging and distributng python projects it is used by setuptools 
to define the configuartion of your project, such as its metadata, dependancies and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:

    '''
    This function will return list of requirements
    '''
    requirement_list:List[str]=[]
    try:
        
        with open('requirements.txt', 'r') as file:
            lines=file.readlines()

            for line in lines:
                requirement=line.strip()

                if requirement and requirement!='-e':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found" )

    return requirement_list



print(get_requirements())




setup(
    name="Networksecurity",
    version="0.01",
    author="Manya Goyal",
    author_email="manyabuzz85@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)