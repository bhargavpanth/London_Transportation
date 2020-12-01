import os
from setuptools import setup

def read(file_name: str):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name = "transportation_pipeline",
    version = "0.0.1",
    author = "Bhargav Panth",
    author_email = "bhargavrpanth@gmail.com",
    description = (""),
    license = "MIT",
    keywords = "PySpark, Analytics, TFL",
    url = "",
    packages=[],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)