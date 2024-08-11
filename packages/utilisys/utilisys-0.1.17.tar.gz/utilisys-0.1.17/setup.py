from setuptools import setup, find_packages

import io
with io.open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="utilisys",
    version="0.1.17",
    author="Lifsys, Inc",
    author_email="info@lifsys.com",
    description="A collection of utility functions for various tasks by Lifsys, Inc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lifsys/utilisys",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "phonenumbers",
        "pandas",
        "redis",
        "fuzzywuzzy",
        "requests",
        "beautifulsoup4",
        "urllib3",
        "onepasswordconnectsdk",
        "sqlalchemy",
    ],
)
