# setup.py

from setuptools import setup, find_packages

setup(
    name='Connet',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl'
    ],
    entry_points={
        'console_scripts': [
            'calculate_dist=ceszhendehmf.calculate:calculate_dist',
        ],
    },
    author='Gongruihao',
    author_email='202031200039@mail.bnu.edu.cn',
    description='A package for generating network files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
