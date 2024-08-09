from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PyMediaTools",
    version="1.0.0",
    author="Zied Boughdir",
    author_email="ziedboughdir@gmail.com",
    description="A library to read video and audio files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zinzied/PyMediaTools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "moviepy",
        "pydub",
    ],
)