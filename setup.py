#!/usr/bin/env python
from setuptools import setup, find_packages

setup_requires = []
install_requires = []

dependency_links = []
setup(
    name = 'ucloudcli',
    version = '0.1',
    description = 'ucloud command line interface',
    author = 'WonJinSeo',
    author_email = 'seowjin1060@gmail.com',
    packages = find_packages(exclude = ("credit.txt",".DS")),
    include_package_data = True,
    install_requires=install_requires,
    setup_requires = setup_requires,
    dependency_links=dependency_links,
    license="Apache License 2.0",
    scripts=['bin/bash_setup'],
    #scripts=['manage.py'],
    entry_points={
        'console_scripts': [],
        'egg_info.writers':[],
        }
    )
