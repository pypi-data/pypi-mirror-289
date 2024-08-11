from setuptools import setup, find_packages

setup(
    name='masterlog',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        
    ],
    author='Sergey Hovhannisyan',
    description='This module offers a versatile logging system with configurable log levels, sources, and formatting options. It features colorized terminal output and supports customizable file-based logging, making it suitable for various logging needs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)