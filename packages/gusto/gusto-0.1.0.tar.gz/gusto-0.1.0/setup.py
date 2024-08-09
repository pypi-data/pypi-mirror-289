from setuptools import setup, find_packages
import os


# Read the contents of requirements.txt
def read_requirements():
    with open("requirements.txt") as req_file:
        return req_file.read().splitlines()


# Read the contents of README.md
def read_long_description():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()


setup(
    name="gusto",
    version="0.1.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=read_requirements(),
    author="Jackson Walker",
    author_email="jacksonrgwalker@gmail.com",
    description="A lightweight LLM agent and tool manager",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/jacksonrgwalker/gusto",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    keywords="llm agent tool manager ai",
    project_urls={
        "Bug Reports": "https://github.com/jacksonrgwalker/gusto/issues",
        "Source": "https://github.com/jacksonrgwalker/gusto",
    },
    include_package_data=True,
)
