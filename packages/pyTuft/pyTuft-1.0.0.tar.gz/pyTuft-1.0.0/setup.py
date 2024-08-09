from setuptools import setup, find_packages

setup(
    name="pyTuft",
    version="1.0.0",
    description="A Truffle-like tool for Python smart contracts",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/OmneDAO/pyTuft",
    packages=find_packages(),
    install_requires=[
        "requests",
        "argparse",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
