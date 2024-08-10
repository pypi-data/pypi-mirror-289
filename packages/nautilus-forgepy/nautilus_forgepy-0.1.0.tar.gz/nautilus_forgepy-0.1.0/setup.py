# setup.py

from setuptools import setup, find_packages

setup(
    name="nautilus-forgepy",
    version="0.1.0",
    packages=find_packages(),  # Automatically find and include packages
    install_requires=[
        "algorand-python>=1.3.0"
    ],
    author="Nicholas Shellabarger",
    author_email="enshellapypi@gmail.com",
    description="Algorand Python Smart Contract Library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/NautilusOSS/forgepy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

