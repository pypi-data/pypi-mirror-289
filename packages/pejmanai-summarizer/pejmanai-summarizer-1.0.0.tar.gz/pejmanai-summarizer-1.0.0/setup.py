from setuptools import setup, find_packages

setup(
    name="pejmanai-summarizer",  # Package name on PyPI
    version="1.0.0",
    author="Pejman",
    author_email="pejman.ebrahimi77@gmail.com",
    description="A simple text summarizer package using transformers and BART.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/arad1367/pejmanai-summarizer",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch"  
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
