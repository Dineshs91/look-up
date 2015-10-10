import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "look-up",
    version = "0.1.0",
    author = "Dinesh S",
    author_email = "dineshpy07@gmail.com",
    description = ("Get the meaning of a word on your terminal"),
    license = "MIT",
    keywords = "english dictionary words",
    url = "https://github.com/Dineshs91/lookup",
    packages = ['lookup'],
    long_description = read('README.md'),
    install_requires = [
        "click>=5.0",
        "wordnik==2.1.3"
    ],
    entry_points = {
        'console_scripts': [
            'look-up=lookup:main'
        ],
    }
)