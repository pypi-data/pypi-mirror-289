# setup.py

from setuptools import setup, find_packages

setup(
    name='pip-sdk-test',
    version='0.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pip-sdk-test=pip_sdk_test.main:main',
        ],
    },
    description='A simple package that prints Hello, World!',
    author='Mahesh Karre',
    author_email='your.email@example.com',
)

