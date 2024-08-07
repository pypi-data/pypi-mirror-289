# GREYDATA

## Introduction

`greydata` is a Python library for data analysts. This library provides tools and functions for data processing and analysis.

## Installation

To install the `greydata` library, use `pip`:

```bash
pip install greydata
```

## Updating the Library
To update the greydata library on PyPI, follow these steps:

### 1. Update the Version
Before updating, make sure to change the version number in your setup.py file.

1. Open setup.py.
2. Update the version value to the new version number.

Example:
```python
# setup.py

from setuptools import setup, find_packages

setup(
    name='greydata',
    version='0.1.4',  # Update the version here
    author='Grey Ng',
    author_email='luongnv.grey@gmail.com',
    description='Library for data analyst',
    url='https://greyhub.github.io/',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # Your dependencies here
    ],
)
```

### 2. Package the Library
Use setuptools to package the library. Run the following command from the project root directory:

```bash
python setup.py sdist bdist_wheel
```
This command will create distribution files in the dist/ directory.

### 3. Upload to PyPI
Use twine to upload the distribution files to PyPI. Run the following command:

```bash
twine upload dist/*
```

### 4. Verify the Update
After uploading, check the PyPI page for the library to confirm that the new version is available.

PyPI page for greydata: https://pypi.org/project/greydata/

## Usage Instructions
For usage instructions, refer to the documentation or examples in the docs folder or visit the online documentation.

## Contact
If you encounter issues or have questions, please contact the author via email: luongnv.grey@gmail.com.

## Upgrading the Library
To upgrade greydata to the latest version, use pip:

```bash
pip install --upgrade greydata
```
This command will install the latest version of the greydata library if it's already installed, or install it if it’s not.