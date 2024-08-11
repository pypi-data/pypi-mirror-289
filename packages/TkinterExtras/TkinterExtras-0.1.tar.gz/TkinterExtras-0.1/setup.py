from setuptools import setup, find_packages

setup(
    name="TkinterExtras",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "tkinter;platform_system=='Windows'",
        "tkinter;platform_system=='Darwin'",
        "python3-tk;platform_system=='Linux'"
    ],
    author="Marcus Collins",
    author_email="mjdj27123@gmail.com",
    description="Some extra classes and functions for tkinter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)