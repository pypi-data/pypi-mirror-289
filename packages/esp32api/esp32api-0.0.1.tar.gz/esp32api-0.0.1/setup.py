# setup.py

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="esp32api",
    version="0.0.1",
    author="AL",
    author_email="zhoulong0014@163.com",
    description="A Python wrapper for interacting with a MicroPython device.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypymodule",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)