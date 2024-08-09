from pathlib import Path

from setuptools import find_packages, setup


def readme():
    with Path("README.md").open() as f:
        return f.read()


def parse_requirements(filename):
    with Path(filename).open() as file:
        return file.read().splitlines()


setup(
    name="gmfy",
    version="0.0.1",
    author="Evgeny Izvekov, Yuriy Belotserkovskiy",
    author_email="evgeny.izvekov@redcollar.ru, yuriy.belotserkovskiy@redcollar.ru",
    description="This is a simple library for working with the gmfy api.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://gitlab.rdclr.ru/gmfy/python-gmfy_sdk",
    packages=find_packages(),
    install_requires=parse_requirements("requirements/production.txt"),
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
    ],
    keywords="gmfy API gamification",
    project_urls={
        "GitLab": "https://gitlab.rdclr.ru/gmfy/python-gmfy_sdk",
    },
    python_requires=">=3.12",
)
