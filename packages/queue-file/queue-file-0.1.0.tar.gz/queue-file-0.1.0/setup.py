from setuptools import setup, find_packages

from src.queue_file import __program__, __version__, __author__, __email__


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=__program__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description=__program__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/philiporange/queue-file",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "jsonpickle",
    ],
)
