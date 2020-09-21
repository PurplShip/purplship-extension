from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

dev_requirements = [
    "appdirs",
    "attrs",
    "black",
    "certifi",
    "chardet",
    "click",
    "coverage",
    "generateDS",
    "idna",
    "lxml",
    "requests",
    "six",
    "toml",
    "urllib3",
    "xmltodict",
    "mypy",
    "wheel",
]

setup(
    name="freightcom.extension",
    version="2020.9.0",
    description="Freightcom purplship extension",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PurplShip/purplship-extension/tree/main/src/freightcom",
    license="LGPLv3",
    packages=find_namespace_packages(exclude=["tests*"]),
    install_requires=[
        "six",
        "purplship~=2020.8.0",
        "purplship.package~=2020.8.0",
        "purplship-server.core~=2020.8.0",
    ],
    extras_require={"dev": dev_requirements},
    dependency_links=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
)
