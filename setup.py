#!/usr/bin/env python
from sslyze import (
    __author__,
    __email__,
    __license__,
    __version__,
    PROJECT_DESC,
    PROJECT_URL
)

SSLYZE_SETUP = {
    'author': __author__,
    'author_email': __email__,
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: French',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: System :: Networking'
    ],
    'description': PROJECT_DESC,
    'entry_points': {
        'console_scripts': ['sslyze = sslyze.__main__:main']
    },
    'extras_require': {
        ':python_version < "3.4"': ['enum34'],
        ':python_version < "3.5"': ['typing']
    },
    'install_requires': [
        'cryptography',
        'nassl>=0.16.0,<0.17.0'
    ],
    'license': __license__,
    'name': 'SSLyze',
    'package_data': {
        'sslyze.plugins.utils.trust_store': ['pem_files/*.pem']
    },
    'packages': [
        'sslyze',
        'sslyze.cli',
        'sslyze.plugins',
        'sslyze.plugins.utils',
        'sslyze.plugins.utils.trust_store',
        'sslyze.utils'
    ],
    'url': PROJECT_URL,
    'version': __version__,
}

if __name__ == "__main__":
    # test that what you need from requirements.txt is satisfied
    try:
        import tls_parser
    except ImportError:
        from os.path import dirname, realpath
        exit('\nError: missing library packages. please run this first:\n\n\
    pip install -r {file_path:}/requirements.txt --target {file_path:}/lib\n'.format(
            file_path=dirname(realpath(__file__))
        ))

    # Importing setuptools here because setup_py2exe also
    # imports SSLYZE_SETUP but needs to use distutils
    from setuptools import setup

    setup(**SSLYZE_SETUP)
