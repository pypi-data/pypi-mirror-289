from setuptools import setup, find_packages
import os

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='SAFT_model_implementation_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[

    ],
    entry_points={
        "console_scripts": [
            "create-project = model_implementation_project:setup_project_structure"
        ]
    },
    long_description=description,
    long_description_content_type="text/markdown"
    # other setup options
)
