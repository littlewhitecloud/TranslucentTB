"""Setup"""
from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="translucenttb",
    version="0.0.4",
    description="A python version TranslucentTB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="littlewhitecloud",
    url="https://github.com/littlewhitecloud/TranslucentTB/",
)
