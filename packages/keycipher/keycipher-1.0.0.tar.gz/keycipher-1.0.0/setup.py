from setuptools import setup, find_packages

setup(
    name="keycipher",
    version="1.0.0",
    description="A Python package for AES-GCM encryption and decryption with a key.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="imparth",
    url="https://github.com/imparth7/keycipher-py",
    packages=find_packages(),
    install_requires=[
        "cryptography>=3.4.7",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords=["encryption", "decryption", "AES-GCM", "cryptography"],
    project_urls={
        "Source": "https://github.com/imparth7/keycipher-py",
        "Bug Reports": "https://github.com/imparth7/keycipher-py/issues",
        "Homepage": "https://github.com/imparth7/keycipher-py#readme",
    },
)
