from setuptools import setup, find_packages
import os
import re

# Read version from version.py
version_file = os.path.join(os.path.dirname(__file__), "ai_logstash", "version.py")
with open(version_file, "r") as f:
    version_content = f.read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_content, re.M
    )
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." % version_file)


extras_test = [
    "hypothesis",
    "ruff",
    "pyproj",
    "pytest",
    "pytest-cov",
    "pytest-asyncio",
    "tox",
    "build",
    "pip-audit",
    "twine",
]

setup(
    name="ai_logstash",
    version=version,
    install_requires=[
        "python-logstash-async",
    ],
    setup_requires=[
        "setuptools_scm",
    ],
    extras_require={
        "test": extras_test,
    },
    author="Bip Bop",
    packages=find_packages(exclude=("tests", "scripts")),
    author_email="no_email@example.com",
    description="A versatile logging package with async support",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
)
