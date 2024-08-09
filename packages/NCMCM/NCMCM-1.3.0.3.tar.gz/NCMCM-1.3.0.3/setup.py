# setup.py
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='NCMCM',
    version='1.3.0.3',
    author='Hofer Michael, Kumar Akshey',
    author_email='hofer.michael.98@email.com',
    description='A toolbox to visualize neuronal imaging data and apply the NC-MCM framework to it',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DriftKing1998/NC-MCM-Visualizer',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['ncmcm/data/datasets/NoStim_Data.mat', 'ncmcm/data/default_physic.json']},
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'matplotlib',
        'scikit-learn',
        'networkx',
        'pyvis',
        'statsmodels',
        'tensorflow',
        'tqdm',
        'scipy',
        'mat73'
    ],
)
