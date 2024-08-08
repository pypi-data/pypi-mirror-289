import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="102218023_TEXTCONVERTOR",
    version="1.0.0",
    description="This package provides a simple tool to convert the contents of a file to uppercase.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="JASHANDEEP SINGH",
    author_email="jashandeepgarry2003@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        
    ],
    packages=["uppercase"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "uppercase=uppercase.__main__:main",
        ]
    },
)