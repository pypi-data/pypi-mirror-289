from setuptools import setup, find_packages
import os,codecs


here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
    
    
VERSION = '1.0.2'
DESCRIPTION = 'Simple Calculator Package'
LONG_DESCRIPTION = 'A Calculator which do some simple kind of calculations like addition,subtraction, multiplication, etc it does not take only 2 argument you can pass multiple arguments'

# Setting up
setup(
    name="sameer-simple-calculator",
    version=VERSION,
    author="Muhammad Sameer",
    author_email="muhammadsameer.css@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'calculator', 'python calculator','cli'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    
    python_requires='>=3.6',
)
