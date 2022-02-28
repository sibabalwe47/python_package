from ensurepip import version
from gettext import install
from setuptools import setup, find_packages

setup(
    name="python_package",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    license="MIT",
    description="EDSA example python package",
    long_description=open("README.md").read(),
    install_requires=["numpy"],
    url="http://github./com/sibabalwe47/python_package",
    author="Siba N.",
    author_email="sibabalwe47@gmail.com"
)
