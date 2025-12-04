"""
Setup script for pyrua package.

For modern installations, pyproject.toml is preferred.
This file is maintained for backward compatibility with older pip versions.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyrua",
    version="1.0.0",
    author="Farhan Ali",
    author_email="i.farhanali.dev@gmail.com",
    description="Professional Random User-Agent Generator for web scraping and browser simulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/farhaanaliii/pyrua",
    project_urls={
        "Documentation": "https://github.com/farhaanaliii/pyrua#readme",
        "Bug Tracker": "https://github.com/farhaanaliii/pyrua/issues",
        "Source Code": "https://github.com/farhaanaliii/pyrua",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Typing :: Typed",
    ],
    keywords=[
        "pyrua",
        "user-agent",
        "useragent",
        "random-user-agent",
        "web-scraping",
        "browser-simulation",
        "http-headers",
        "web-crawler",
        "scraping",
        "automation",
        "testing",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={},
)
