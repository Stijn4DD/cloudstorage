from setuptools import setup, find_packages

setup(
    name='cloudstorage',
    version='0.127',
    description='',
    author='Google',
    packages = find_packages('src'),
    package_dir={'': 'src'},
)
