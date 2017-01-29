from setuptools import setup

setup(
    name="DataStore",
    version='0.0.1',
    packages=["DataStore"],
    install_requires=['requests'],
    package_data={},
    author="cyberpirate",
    author_email="",
    description="A client for the DataStore api",
    license="None",
    keywords=["DataStore"],
    url="http://192.168.1.6:3000/cyberpirate/DataStoreLib.py",
    long_description="A client for the DataStore api",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
    ],
)