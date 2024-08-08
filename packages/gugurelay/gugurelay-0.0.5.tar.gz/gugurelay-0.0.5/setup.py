import codecs
import os
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi (if you dont need delete it)
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# you need to change all these
VERSION = '0.0.5'
DESCRIPTION = 'DESCRIPTION'
LONG_DESCRIPTION = 'LONG_DESCRIPTION'

setup(
    name="gugurelay",
    version=VERSION,

    install_requires=[
        'python-can',
        'python-can[canalystii]',
        'pywin32',
        'pywin32-ctypes',
    ],

    author="wangzc",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    # packages=find_packages(where='src'),  # Specify the source directory
    # package_dir={'': 'src'},  # Maps the root package to the src directory
    packages=find_packages(),
    keywords=['python', 'can'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        # "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
