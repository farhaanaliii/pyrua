from setuptools import setup

long_desc = open("README.md","r").read()
setup(
	name = "pyrua",
	version = "0.1",
	author = "Farhan Ali",
	description = "Simple module for generating random User-Agent for web scraping",
	long_description = long_desc,
	long_description_content_type = "text/markdown",
	packages = ["pyrua"],
	keywords = [
		"pyrua",
		"rua",
		"random user agent",
		"user agent",
		"random_user_agent",
		"random useragent",
		"useragent",
		"random_useragent",
		"useagent for web scraping"
	],
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: Apache License, Version 2.0",
		"Operating System :: OS Independent",
    ],
	install_requires=[],
)
