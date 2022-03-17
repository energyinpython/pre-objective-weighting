import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="objective-weighting-aleksandraba",
    version="0.0.4",
    author="Aleksandra Bączkiewicz",
    author_email="aleksandra.baczkiewicz@phd.usz.edu.pl",
    description="Package with Objective Criteria Weighting Methods for Multi-Criteria Decision Making",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/energyinpython/pre-objective-weighting",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)