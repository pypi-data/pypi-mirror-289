# setup.py

from setuptools import setup, find_packages

setup(
    name='plotdetection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
    ],
    description='A library for real-time data visualization on a polar plot.',
    author='Anvai Shrivastava',
    author_email='anvaishrivastava@example.com',
    url='https://github.com/anvai0304/plotdetection',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
