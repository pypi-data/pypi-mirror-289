# encoding: utf-8
from setuptools import setup, find_packages


setup(
    name='mrweb',
    version='1.9',
    packages=find_packages(),
    license='MIT',
    author='vboxvm512',
    author_email='vboxvm512@gmail.com',
    description='Join @mrwebservice For API  Mrweb Library is python library to use easy channel api',
    long_description=__doc__,
    long_description_content_type='text/markdown',
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'requests',
	'urllib3'
    ]
)
