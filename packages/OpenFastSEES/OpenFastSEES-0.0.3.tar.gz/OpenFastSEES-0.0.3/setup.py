""""Distribution setup"""

import os
from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open(os.path.join(ROOT, "VERSION")) as version_file:
    VERSION = version_file.read().strip()

setup(
    name="OpenFastSEES",
    description="Combined package of OpenSeesPy and pyFAST",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    version=VERSION,  # Ensure this matches the new version number
    url="https://github.com/ALSHAMIQAHTAN/OpenFastSEES",
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Software Development :: Testing",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "matplotlib",
        "openpyxl",
        "numpy>=1.15.2",
        "pandas",
        "pyarrow",  # for parquet files
        "scipy",
        "chardet",
        "xarray",  # for netcdf files
        "pytest",
        "openseespy",
    ],
    test_suite="pytest",
    tests_require=["pytest"],
    entry_points={"console_scripts": ["OpenFastSEES = OpenFastSEES.__main__:main"]},
)
