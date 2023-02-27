from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="benqr-action-tests",
    version="0.0.1",
    author="Ben Gregory",
    author_email="ben.gregory@quickreleaseinc.com",
    maintainer="Ben Gregory",
    description="Test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ben-qr/benqr-action-tests",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
)
