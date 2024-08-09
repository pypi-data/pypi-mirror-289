from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.2"
DESCRIPTION = "A python implementation on the FWPODS algorithm."
LONG_DESCRIPTION = 'A fully python, mostly self-contained implementation of the FWPODS algorithm, based on the paper named "A sliding window-based approach for mining frequent weighted patterns over data streams", Bui et al. (2021) doi: 10.1109/ACCESS.2021.30701.32.'

# Setting up
setup(
    name="fwpods_py",
    version=VERSION,
    author="Fishappy0",
    author_email="<fishappy0@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["orderedset"],
    keywords=[
        "fwpods",
        "data stream mining",
        "stream mining",
        "frequent weighted pattern data stream",
        "sliding window over data streams",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ],
)
