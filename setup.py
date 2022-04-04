from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in paraguay_defaults/__init__.py
from paraguay_defaults import __version__ as version

setup(
	name="paraguay_defaults",
	version=version,
	description="A custom app to manage paraguay custom settings",
	author="Lewin Villar",
	author_email="lewinvillar@tzcode.tech",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
