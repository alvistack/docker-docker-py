# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='docker',
    version='7.1.0',
    description='A Python library for the Docker Engine API.',
    maintainer_email='"Docker Inc." <no-reply@docker.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    install_requires=[
        'pywin32>=304; sys_platform == "win32"',
        'requests>=2.26.0',
        'urllib3>=1.26.0',
    ],
    extras_require={
        'dev': [
            'coverage==7.2.7',
            'pytest-cov==4.1.0',
            'pytest-timeout==2.1.0',
            'pytest==7.4.2',
            'ruff==0.1.8',
        ],
        'docs': [
            'myst-parser==0.18.0',
            'sphinx==5.1.1',
        ],
        'ssh': [
            'paramiko>=2.4.3',
        ],
        'websockets': [
            'websocket-client>=1.3.0',
        ],
    },
    packages=[
        'docker',
        'docker.api',
        'docker.context',
        'docker.credentials',
        'docker.models',
        'docker.transport',
        'docker.types',
        'docker.utils',
    ],
)
