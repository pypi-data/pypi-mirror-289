from setuptools import setup, find_packages
import os

def find_pyc_files(directory):
    pyc_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pyc'):
                pyc_files.append(os.path.join(root, file))
    return pyc_files

setup(
    name='safi',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Insolify',
    author_email='safi@insolify.com',
    description='Safi is a versatile and super fast Ai Platform. This is a Python library for Safi API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://safi.insolify.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
