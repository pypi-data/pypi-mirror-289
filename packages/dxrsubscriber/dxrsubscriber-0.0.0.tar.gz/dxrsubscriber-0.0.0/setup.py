#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 8:55
# @Author  : wangqinggang
# @Email   : wqg1993@qq.com
# @File    : setup.py
import setuptools
import os
import re

# Read the version from the package
def read_version():
    init_file_path = os.path.join(os.path.dirname(__file__), "dxrsubscriber", "__init__.py")
    with open(init_file_path, "r", encoding="utf-8") as fp:
        for line in fp:
            match = re.match(r"^__version__ = ['\"]([^'\"]*)['\"]", line)
            if match:
                return match.group(1)
    raise RuntimeError("Unable to find version string.")
setuptools.setup(
    name="dxrsubscriber",
    version=read_version(),
    author="Your Name",
    author_email="your.email@example.com",
    description="A ZMQ subscriber for receiving and decoding video streams.",
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/zmq_subscriber",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pyzmq",
        "av",
        "opencv-python==4.5.1.48"
    ],
)
