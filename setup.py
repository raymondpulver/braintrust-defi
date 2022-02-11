import setuptools

requirements = [
    "appdirs==1.4.4",
    "atomicwrites==1.4.0",
    "attrdict==2.0.1",
    "attrs==19.3.0",
    "base58==2.0.1",
    "certifi==2020.4.5.2",
    "chardet==3.0.4",
    "cytoolz==0.10.1",
    "distlib==0.3.0",
    "dydx-python==0.10.4",
    "eth-abi==2.1.1",
    "eth-account==0.4.0",
    "eth-hash==0.2.0",
    "eth-keyfile==0.5.1",
    "eth-keys==0.2.4",
    "eth-rlp==0.1.2",
    "eth-typing==2.2.1",
    "eth-utils==1.9.0",
    "filelock==3.0.12",
    "hexbytes==0.2.1",
    "idna==2.8",
    "importlib-metadata==0.23",
    "ipfshttpclient==0.4.13.2",
    "jsonschema==2.6.0",
    "lru-dict==1.1.6",
    "more-itertools==8.3.0",
    "multiaddr==0.0.9",
    "netaddr==0.7.19",
    "packaging==20.4",
    "parsimonious==0.8.1",
    "pluggy==0.13.1",
    "protobuf==3.15.0",
    "py==1.8.1",
    "pycryptodome==3.9.7",
    "pyparsing==2.4.7",
    "pytest==4.6.11",
    "requests==2.22.0",
    "requests-mock==1.6.0",
    "rlp==1.2.0",
    "six==1.12.0",
    "toml==0.10.1",
    "toolz==0.10.0",
    "tox==3.13.2",
    "urllib3==1.25.9",
    "varint==1.0.2",
    "virtualenv==20.0.21",
    "wcwidth==0.2.4",
    "web3==5.0.0",
    "websockets==7.0",
    "zipp==3.1.0",
]


with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
        name="braintrust_defi",
        version="0.0.3",
        author="Raymond Pulver IV",
        author_email="raymondpulver@my.uri.edu",
        description="Braintrust DeFi adapter",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/raymondpulver/braintrust-defi",
        install_requires=requirements,
        packages=setuptools.find_packages(include=["braintrust_defi"]),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.6",
    )
