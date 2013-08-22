from setuptools import setup, find_packages

setup(
    name='cloudstorage',
    version='0.65',
    description='',
    author='Google',
    packages = find_packages('src'),
    package_dir={'': 'src'},
)
