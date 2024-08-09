import codecs
import os
import setuptools
from pathlib import Path

VERSION = '1.0.4'
DESCRIPTION = 'None'
LONG_DESCRIPTION = 'None'

# Setting up
setuptools.setup(
    name="my_robot",
    version=VERSION,

    author="Ahao",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=setuptools.find_packages(include="gym_foo*"),
    install_requires=[
        'getch; platform_system=="linux"',
        'getch; platform_system=="windows"',
        'gym'
    ],
    keywords=['python', 'flink', 'arg', 'toml', 'windows', 'linux'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix"
    ]
)