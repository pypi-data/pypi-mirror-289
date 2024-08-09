# setup.py

from setuptools import setup, find_packages

setup(
    name='my_unique_datasets_library',  # Make sure this is unique
    version='0.9.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
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
        'my_datasets': ['/home/ravi/Desktop/datasets/my_datasets/data/*.csv','/home/ravi/Desktop/datasets/my_datasets/data/images/*','/home/ravi/Desktop/datasets/my_datasets/data/images/brain_tumor_dataset/*','/home/ravi/Desktop/datasets/my_datasets/data/images/cardetection/*','/home/ravi/Desktop/datasets/my_datasets/data/images/ChestXraydetection/*','/home/ravi/Desktop/datasets/my_datasets/data/images/Covid19-datasets/*','/home/ravi/Desktop/datasets/my_datasets/data/images/Riped and Unriped Tomato Dataset/*'],
    },
)

