from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="digifoam",
    version="0.2.0",
    author="Michael",
    author_email="michael@digitalcarbon.ai",
    description="DigiFOAM CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://digifoam.ai",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "python-dotenv",
        "requests",
        "chardet",
        "typer",
        "websockets",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "digifoam=digifoam.cli:app",
        ],
    },
)
