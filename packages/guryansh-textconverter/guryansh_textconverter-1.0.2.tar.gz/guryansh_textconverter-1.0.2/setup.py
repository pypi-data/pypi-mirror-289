import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="guryansh-textconverter",
    version="1.0.2",
    description="Python package for Square",
    long_description=README,
    long_description_content_type="text/markdown",

    author="Guryansh",
    author_email="guryanshsingla@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["square"],
    include_package_data=True,
    install_requires=['time', 'argparse'],
    entry_points={"console_scripts": ["square=square.cli:main"]},
)
