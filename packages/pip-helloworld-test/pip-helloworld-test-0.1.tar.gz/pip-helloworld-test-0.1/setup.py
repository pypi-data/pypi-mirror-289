# setup.py

from setuptools import setup, find_packages

setup(
    name='pip-helloworld-test',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pip-helloworld-test=pip_helloworld_test.main:main',
        ],
    },
    description='A simple package that prints Hello, World!',
    author='Mahesh Karre',
    author_email='your.email@example.com',
)

