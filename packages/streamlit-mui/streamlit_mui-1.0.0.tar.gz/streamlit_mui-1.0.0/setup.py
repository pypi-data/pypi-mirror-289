"""
This module provides setup configurations to create a build that can be uploaded on pypi server.

Author: Dilip Thakkar [dilip.thakkar.eng@gmail.com]
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='streamlit_mui',
    version='1.0.0',
    author="Dilip Thakkar",
    author_email="dilip.thakkar.eng@gmail.com",
    description='Streamlit module which provides implementation of various Material UI components',
    long_description=long_description,
    py_module=['streamlit_mui'],
    packages=setuptools.find_packages(exclude=('venv')),
    package_data={'streamlit_mui': [
        'component/frontend/build/**']},
    python_requires='>=3.9.0',
    install_requires=['streamlit >= 1.36.0'],
    zip_safe=False
)
