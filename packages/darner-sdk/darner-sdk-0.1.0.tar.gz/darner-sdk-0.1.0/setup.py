from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="darner-sdk",
    version="0.1.0",
    author="Ebot Tabi",
    author_email="ebot.tabi@gmail.com",
    description="A Python SDK for loading and saving data within darner python supports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ebottabi/darner",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas",
        "pyarrow",
    ],
)