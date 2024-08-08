# setup.py

from setuptools import setup, find_packages

setup(
    name='cliquest',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
        'cdlib'
    ],
    entry_points={
        'console_scripts': [
            'estimate_cli=cliquest.cli:estimate_cli',
        ],
    },
    author="Gongruihao",
    author_email="202031200039@mail.bnu.edu.cn",
    description='A package for estimating clique structure',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

