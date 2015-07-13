import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="NokiaLCD",
    version="0.0.1",
    author="Paul Pletenev",
    author_email="cpp.create@gmail.com",
    description=("BlackSwift Nokia LCD Python module with examples"),
    license="GPL",
    keywords="blackswift nokialcd",
    url="http://packages.python.org/",
    packages=['NokiaLCD'],
    long_description=read("README.md"),
    classifiers=
        ["Development Status :: 3 - Alpha",
         "Topic :: Utilities",
         "License :: OSI Approved :: BSD License",
         ],
)
