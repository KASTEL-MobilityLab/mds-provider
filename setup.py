from pathlib import Path
import re
from setuptools import find_packages, setup

__version__ = re.search(
    r"__version__ = ['\"]([^'\"]*)['\"]",
    Path("mds", "versions.py").read_text()
    ).group(1)

setup(
    name="mds_provider",
    version=__version__,
    description="Tools for working with Mobility Data Specification Provider data",
    long_description=Path("README.md").read_text(),
    url="https://github.com/CityofSantaMonica/mds-provider",
    author="City of Santa Monica and contributors",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Fiona",
        "jsonschema",
        "packaging",
        "pandas",
        "psycopg2-binary",
        "requests",
        "scipy",
        "Shapely",
        "sqlalchemy"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
    ],
)