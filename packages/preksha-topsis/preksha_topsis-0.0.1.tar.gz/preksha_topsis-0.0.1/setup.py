import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding='utf-8')


# This call to setup() does all the work
setup(
    name="preksha_topsis",
    version="0.0.1",
    description="It calculates the topsis score and gives the best alternative",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Preksha-Dadoo/preksha_topsis",
    author="Preksha Dadoo",
    author_email="pdadoo_be22@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
)