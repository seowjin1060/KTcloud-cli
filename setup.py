from setuptools import setup, find_packages

setup_requires = []


install_requires = []

dependency_links = []
setup(
    name = 'ucloudcli',
    version = '0.1',
    description = 'ucloud command line interface',
    author = 'WonJinSeo',
    author_email = 'seowjin1060@naver.com',
    packages = find_packages(),
    include_package_data = True,
    install_requires=install_requires,
    setup_requires = setup_requires,
    dependency_links=dependency_links,
    #scripts=['manage.py'],
    entry_points={
        'console_scripts': [],
        'egg_info.writers':[],
        }
    

    )
