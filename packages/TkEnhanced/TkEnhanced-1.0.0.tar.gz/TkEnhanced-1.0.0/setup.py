# Standard libraries:
from setuptools import setup, find_packages
from typing import Dict, List, Any

# Commands:
# pip install twine wheel
# python setup.py sdist bdist_wheel
# twine upload dist/*

# Setup:
application_packages: List[str] = find_packages()
application_settings: Dict[str, Any] = {
    "name": "TkEnhanced",
    "version": "1.0.0",
    "description": "Enhanced Tkinter widgets for a modern look and additional functionality.",
    "author": "Bunnitown",
    "packages": application_packages,
    "install_requires": [],
    "classifiers": [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]}
setup(**application_settings)
