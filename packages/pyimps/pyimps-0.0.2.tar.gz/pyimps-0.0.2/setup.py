# Copyright (c) 2023 bedbad
from setuptools import setup, find_packages

setup(
    name='pyimps',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='bedbad',
    author_email='antonyuk@bu.edu',
    description='Unconfuse your Py imports',
    long_description='''Resolve your Py imports - see where '''
                     '''all tha you have sit;\n where '''
                     '''all tha you don't, should be;\n see all transitives '''
                     '''and the way the were imported and defined;\n'''
                     '''All of it - right in your terminal''',
    long_description_content_type='text/markdown',
    url='https://github.com/bedbad/justpyplot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)
