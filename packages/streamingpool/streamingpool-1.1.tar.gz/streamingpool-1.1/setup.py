from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent

setup(
    name = "streamingpool",
    version = "1.1",
    packages = find_packages(),
    install_requires = [

    ],    
    long_description=(this_directory / "README.md").read_text("utf-8"),
    long_description_content_type='text/markdown'
)