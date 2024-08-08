from setuptools import setup, find_packages
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="django-mongodb",
    version="5.0a1",
    author="AnupamAs0x1",
    author_email="your.email@example.com",
    description="MongoDB support for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'requests',  # List other dependencies here
    ],
    classifiers=[
        "Development Status :: 3 - Alpha"
    ],
    keywords="django mongodb",
)
