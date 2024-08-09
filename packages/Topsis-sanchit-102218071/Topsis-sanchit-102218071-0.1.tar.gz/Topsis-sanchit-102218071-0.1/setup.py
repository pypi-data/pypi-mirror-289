from setuptools import setup, find_packages

setup(
    name='Topsis-sanchit-102218071',
    version='0.1',
    author='Sanchit',
    author_email='sanchit@example.com',
    description='A Python package for implementing the TOPSIS method',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'topsis=102218071:topsis',
        ],
    },
    install_requires=[
        'pandas',
        'numpy',
    ],
)
