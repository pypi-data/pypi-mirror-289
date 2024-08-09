from setuptools import setup, find_packages

setup(
    name='trussit',
    version='0.0',
    author='kunalgokhe',
    author_email='kunalgokhe@gmail.com',
    long_description=open('README.md').read(),
    packages=find_packages(),
install_requires=[
        'numpy==1.26.4',
        'tk==0.1.0',
        'customtkinter==5.2.2',
        'matplotlib==3.9.1',
    ],
classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
python_requires='>=3.12',
    entry_points={
        'console_scripts': [
            'trussit = trussit.main:GUI',
        ]
    }
)