# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:51:52 2024

@author: U435712
"""

from setuptools import setup, find_packages

setup(
    name='finishes-library',  # Choose a unique name for your library
    version='0.1.0',  # Start with a version number (e.g., 1.0.0)
    author='Pratiksha Kohokade',
    author_email='pratiksha.kohokade@danfoss.com',
    description='A library to manage finish specifications',
    url= 'https://github.com/pratiksha306/finish_specification.git',
    packages=find_packages(), 
    install_requires=[
        'python-dotenv', 
    ],
)