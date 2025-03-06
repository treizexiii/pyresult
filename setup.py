from setuptools import setup, find_packages

setup(
    name="pyresult",
    version="0.1.0",
    description="Un package implémentant les types Result et Option en Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ton Nom",
    author_email="ton.email@example.com",
    url="https://github.com/tonrepo/core_utils",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pytest>=7.0",
        "pytest-cov>=4.0"
    ]
)