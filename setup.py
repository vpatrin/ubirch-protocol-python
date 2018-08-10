import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ubirch-protocol",
    version="0.0.2",
    author="Matthias L. Jugel",
    author_email="matthias.jugel@ubirch.com",
    description="A ubirch-protocol implementation for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ubirch/ubirch-protocol-python",
    packages=setuptools.find_packages(exclude=['bin', 'docs', 'examples', 'tests*']),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)