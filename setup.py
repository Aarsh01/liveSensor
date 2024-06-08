from setuptools import find_packages,setup
# find_packages: find the number of packages file in the folder 
# setup: provide me the information  

from typing import List
# Later ....

# from pip.req import parse_requirements

def get_requirements() -> list[str]:
    requirements_list: list[str] = []
    return requirements_list


# install_reqs = parse_requirements('requirements.txt')

# reqs = [str(ir.req) for ir in install_reqs]


# import os
# from setuptools import setup

# with open('requirements.txt') as f:
#     required = f.read().splitlines()

setup(      
    name='sensor',
    version='0.0.1',
    author='aarsh',
    author_email='aarshmehtani01@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(), #['pymongo'] # later we will make function {get_requirements()} so that we will not manually list the requirement.text libraies 
    
    
)