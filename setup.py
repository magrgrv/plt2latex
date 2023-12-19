from setuptools import setup, find_packages
import codecs
import os

with codecs.open(os.path.join(os.path.abspath(os.getcwd()), "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
    fh.close()

VERSION = '0.0.8'
DESCRIPTION = 'Make the pyplot figure perfect for LaTeX'

# Setting up
setup(
    name="plt2latex",
    version=VERSION,
    author="mihail73351",
    author_email="mihail73351@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['matplotlib', 'numpy'],
    keywords=['python', 'matplotlib', 'pyplot', 'plt', 'latex'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
