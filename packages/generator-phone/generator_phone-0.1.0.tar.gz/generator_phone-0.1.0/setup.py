# -*- coding: utf-8 -*-
# Time : 2024-08-07 15:42
# Author : zhangxingchen
# contanct : zxcser@163.com
# File : setup.py
# Software: PyCharm


from setuptools import setup, find_packages


filepath = 'README.md'



setup(
    name="generator_phone",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        'Faker==4.18.0'
    ],

    author="zhangxingchen",
    author_email="zxcser@163.com",
    description="first patch commit",
    long_description=open(filepath, encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zhangdongxuan0227/generatorutils.git",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)

