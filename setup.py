from setuptools import setup

setup(
    name="page_objects",
    version="0.1.0",
    author="Zac Delagrange",
    author_email="zac.delagrange@gmail.com",
    packages=["page_objects", "tests"],
    install_requires=["selenium", "eyes-selenium"],
)
