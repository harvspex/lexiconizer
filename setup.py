from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="lexiconizer",
    version="1.0",
    description="Lexiconizer: Count words and find neighbours",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harvspex/lexiconizer",
    author="harvspex",
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "lexiconizer = src.lexiconizer:main",
        ],
    },
)
