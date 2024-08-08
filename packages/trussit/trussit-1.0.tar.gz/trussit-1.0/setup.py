from setuptools import setup, find_packages

setup(
    name='trussit',
    version='1.0',
    author='kunalgokhe',
    author_email='kunalgokhe@gmail.com',
    description='A basic graphical interface to solve truss problems',
    long_description='Program used to compute the deformation in the truss structure based on the input parameters.',
    keywords=['Truss','Force','FEA','Beam','Deformation Plot'],
    packages=find_packages(),
    install_requires=[
    'setuptools==68.1.2',
    'numpy==2.0.1',
    'tk==0.1.0',
    'customtkinter==5.2.2',
    'matplotlib==3.6.3',
    'pandas==2.2.2',
    ],
    entry_points={
        'console_scripts': [
            'trussit=trussit.main:GUI',
        ],
    },
)