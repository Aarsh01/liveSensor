from setuptools import find_packages,setup
# find_packages: find the number of packages file in the folder 
# setup: provide me the information  

from typing import List
# Later ....


def get_requirements()-> List[str]:
    requirements_list=list[str]=[]
    return requirements_list


setup(      
    name='sensor',
    version='0.0.1',
    author='aarsh',
    author_email='aarshmehtani01@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements(), #['pymongo'] # later we will make function {get_requirements()} so that we will not manually list the requirement.text libraies 
    
    
)