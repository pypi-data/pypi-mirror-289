from setuptools import setup, find_packages

setup(
    name="x-posting-api",
    version="0.1",
    description="A simple Python library for posting tweets using new X API v2.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Redian Marku",
    author_email="redian@topnotch-programmer.com",
    url="https://github.com/redianmarku/x-posting-api",
    packages=find_packages(),
    install_requires=[
        'requests-oauthlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
