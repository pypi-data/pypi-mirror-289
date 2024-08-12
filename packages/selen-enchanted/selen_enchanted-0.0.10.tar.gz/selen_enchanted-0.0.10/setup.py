"""
To install run 
```
python setup.py sdist bdist_wheel
```
"""

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='selen-enchanted',
    version='0.0.10',
    packages=find_packages(),
    summary='A Selenium wrapper with additional functionalities.',
    author="Andrew Naaem",
    author_email="andrew.naaem99@gmail.com",
    license='Apache License 2.0',
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.8",
)