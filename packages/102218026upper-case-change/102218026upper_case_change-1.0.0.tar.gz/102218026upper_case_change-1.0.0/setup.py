import pathlib
from setuptools import setup,find_packages # type: ignore

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="102218026upper-case-change",
    version="1.0.0",
    description="It uppercases whole folder",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Shubhamaggarwal6/upper-case-change",
    author="shubham",
    author_email="09shubhamaggarwal@gmial.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
        packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'upper-case-change=upper_case_change.__main__:main',
        ],
    },
)