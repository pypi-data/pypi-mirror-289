from setuptools import setup, find_packages

setup(
    name="windcomponents",
    version="0.1",
    description="A library for calculating crosswind and tailwind components on a runway",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sebastiaan Menger",
    author_email="sebastiaan.menger@outlook.com",
    packages=find_packages(),
    license="GPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
