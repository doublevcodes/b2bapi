import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="b2bapi",
    version="2.0.0",
    description="Interact with the BytesToBits API through Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/doublevcodes/b2bapi",
    packages=["b2bapi"],
    install_requires=["aiohttp"],
    include_package_data=True
)
