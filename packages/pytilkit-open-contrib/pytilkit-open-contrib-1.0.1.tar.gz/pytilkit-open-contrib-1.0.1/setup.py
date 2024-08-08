from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pytilkit-open-contrib',
    version='1.0.1',
    author='Srijal Dutta',
    author_email='srijaldutta.official+pytilkit@gmail.com',
    description='A utility package for various functionalities including math operations, JSON handling, and RSA encryption',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pyutilkit',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        "cryptography"
    ],
)
