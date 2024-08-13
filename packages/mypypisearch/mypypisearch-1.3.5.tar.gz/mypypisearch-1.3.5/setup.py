import setuptools

from mypypisearch import __version__ as version


with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

with open("requirements.txt", "r", encoding="utf-8") as file:
    requirements = file.read().splitlines()

setuptools.setup(
    name="mypypisearch",
    version=version,
    author="tct123",
    author_email="tct1234@protonmail.com",
    description="Replacement of temporarily deprecated pip search command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shidenko97/pypisearch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "mypypisearch=mypypisearch.__main__:main",
        ],
    },
)
