from setuptools import setup, find_packages

setup(
name='insigen',
version='0.1.0',
author='Aaryan Tyagi',
author_email='tyagiaaryan00@gmail.com',
description='Generates Insights from text pieces such as Documents or Articles',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: Apache Software License',
'Operating System :: OS Independent',
],
python_requires='>=3.11',
)