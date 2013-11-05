from setuptools import setup, find_packages

setup(
    name='cloudstorage',
    version='r127',
    description='',
    author='Google',
    packages = find_packages('src'),
    package_dir={'': 'src'},
)
