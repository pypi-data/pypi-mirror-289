from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="MikkUtils",
    version="0.0.2",
    author="Mikk155",
    author_email="",
    description="Utilities for scripting in my projects, almost is goldsource-related",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mikk155/MikkUtils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
