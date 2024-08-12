from setuptools import setup, find_packages
setup(
    name='adaptive-cards-io',
    version='1.1.0',
    author='Melqui Brito',
    author_email='melquibrito07@gmail.com',
    description='A lightweight framework for building MS adaptive cards programmatically.',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)