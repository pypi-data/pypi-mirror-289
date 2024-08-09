from setuptools import setup, find_packages

setup(
    name="python-xAPI",
    version="0.1",
    description="A simple python package that post tweets using X.com API Free Tier",
    long_description=open('README.md').read(),
    author="Redian Marku",
    author_email="redian@topnotch-programmer.com",
    url="https://github.com/redianmarku/python-xAPI",
    packages=find_packages(),
    install_require=[
        "requests-oauthlib",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]

)