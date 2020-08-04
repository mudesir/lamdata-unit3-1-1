import setuptools
REQUIRED = [
    "numpy",
    "pandas"
]
with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()
setuptools.setup(
    name="lamdata-unit3-1-1",
    version="0.0.1",
    author="Mudesir Suleyman",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/mudesir/lamdata-3-1-1",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)