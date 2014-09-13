#!/usr/bin/env python
# -*- coding: utf-8 -*

from distutils.core import setup
import os

def get_packages(package):
    """
    Return root package & all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]

def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

setup(
    name='Twittos',
    version='0.0.1',
    packages=get_packages('module'),
    package_data=get_package_data('module'),
    description='Python lib for twitter API',
    author='Mysterie pdfpeaceful',
    author_email='kajusska@gmail.com',
    license='N/A',
    long_description='https://github.com/Mysterie/Twittos',
    install_requires=['BeautifulSoup'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ]
)
