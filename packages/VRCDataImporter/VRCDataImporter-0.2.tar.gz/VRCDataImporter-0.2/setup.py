from setuptools import setup, find_packages

with open('readme.md', 'r') as f:
    description = f.read()


setup(
    name="VRCDataImporter",
    version='0.2',
    packages=find_packages(),
    install_requires=['pandas>=2.2.0'],
    long_description=description,
    long_description_content_type='text/markdown'


)