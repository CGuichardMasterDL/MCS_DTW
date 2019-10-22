# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import mcs_dtw

with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

setup(
    name='mcs_dtw',
    version=mcs_dtw.__version__,
    author=mcs_dtw.__author__,
    author_email=mcs_dtw.__email__,
    description=mcs_dtw.__description__,
    long_description=readme,
    url='https://github.com/CGuichardMasterDL/MCS_DTW',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    keywords="audio reconnaissance dtw python3",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts' : [
            'mcs_dtw = mcs_dtw:cmd_mcsdtw',
        ]
    }
)
