# coding=utf-8

from setuptools import setup
import os

appname = "tr"
version = "2.3.0"

try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
except:
    readme = ""

packages = ["tr"]

setup(
    name=appname,
    version=version,
    description=(
        '''%s''' % appname
    ),

    author='anycode',
    author_email='anycode@yahoo.com',
    maintainer='anycode',
    maintainer_email='anycode@yahoo.com',
    packages=packages,
    platforms=["linux"],
    url='https://pypi.org/project/%s/' % appname,
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        "numpy"
    ],
    include_package_data=True,

    long_description=readme,
    long_description_content_type='text/markdown'
)
