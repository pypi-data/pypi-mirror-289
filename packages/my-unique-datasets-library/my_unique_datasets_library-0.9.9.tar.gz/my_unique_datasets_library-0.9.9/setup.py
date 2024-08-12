# setup.py

from setuptools import setup, find_packages

setup(
    name='my_unique_datasets_library',
    version='0.9.9',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'tensorflow',
        'Pillow',
    ],
    description='A library that provides predefined datasets.',
    author='ravishankar',
    author_email='your.email@example.com',
    keywords=['datasets', 'iris', 'data science'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_data={
        'my_datasets': [
            'data/*.csv',
            'data/images/brain_tumor_dataset/*.jpeg',
            'data/images/brain_tumor_dataset/*.jpg',
            'data/images/brain_tumor_dataset/*.png',
        ],
    },
)


