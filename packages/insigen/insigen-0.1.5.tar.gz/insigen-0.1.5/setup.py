from setuptools import setup, find_packages
# with open ("requirements.txt") as f:
    # print("AARYAN IS A BIG FILTHY BITCHASS HARYANVI")
    # requirements = f.readlines()

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
name='insigen',
version='0.1.5',
author='Aaryan Tyagi',
author_email='tyagiaaryan00@gmail.com',
url = "https://github.com/4RCAN3/insigen",
description='Generates Insights from text pieces such as Documents or Articles',
long_description=long_description,
long_description_content_type='text/markdown',
packages=find_packages(where = 'src'),
#data_files={'insigen/resources/Data': ['src/insigen/resources/Data/embeds.pickle','src/insigen/resources/Data/topics.pickle']},
package_dir={'': 'src'},
#package_data={'insigen' :['insigen/resources/Data/*']},
# install_requires=requirements,
include_package_data=True,
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: Apache Software License',
'Operating System :: OS Independent',
],
python_requires='>=3.11',
)