from setuptools import setup, find_packages

VERSION = '1.2.0'
DESCRIPTION = 'Basic Utilities for python development.'
LONG_DESCRIPTION = "Some basic utilities in python to save you some time! You won't ever need to write some lines of code to for example clear the screen but use our solution which also should adjust for nt os systems! Visit the official github: ItzSCodez1467/pybasicutils"

# Setting up
setup(
    name="pybasicutils",
    version=VERSION,
    author="ItzSCodez1467 (Srijal Dutta)",
    author_email="<srijaldutta.official+pybasicutils@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["cryptography", "getpass"],
    keywords=['python', 'utils', 'pytils', 'pyutils', 'basic utils', 'utilities'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
