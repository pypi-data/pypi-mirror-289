import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def get_dll_files():
    return ['crand.dll']

setuptools.setup(
    name="phtcloud_pkg_pycrand",
    version="0.0.1",
    author="phtcloud",
    author_email="phtcloud@foxmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phtcloud-dev",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={
        '': get_dll_files(),
    },
)
