# setup.py

import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a local file"""
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='mkdocs-auto-figure-plugin',
    version='0.1',
    description='A MkDocs plugin that converts markdown encoded images into <figure> elements.',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'auto_figure = src:AutoFigurePlugin',
        ]
    }
)
