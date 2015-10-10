from setuptools import setup


setup(
    name = "look-up",
    version = "0.1.1",
    author = "Dinesh S",
    author_email = "dineshpy07@gmail.com",
    description = ("Get the meaning of a word on your terminal"),
    license = "MIT",
    keywords = "english dictionary words",
    url = "https://github.com/Dineshs91/lookup",
    packages = ['lookup'],
    long_description = "Get the meaning of a word, its pronunciation and "\
                       "examples. Also get word of the day",
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