# setup.py

from setuptools import setup, find_packages

setup(
    name='matmul_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'joblib',
        'numpy'
    ],
    author='Md_sazzad_hossain',
    author_email='sazzad1779@gmail.com',
    description='A simple package for parallel matrix multiplication using joblib',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sazzad1779/matmul_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
