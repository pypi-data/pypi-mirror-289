# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 18:36
# @Author  : Chris
# @Email   : 10512@qq.com
# @File    : setup.py
# @Software: PyCharm


from distutils.core import setup
from pkg_resources import parse_requirements

from setuptools import find_packages

# with open("./requirements.txt", encoding="utf-8") as fp:
#     install_requires = [str(requirement) for requirement in parse_requirements(fp)]

setup(
    name='py-abu',
    version='1.0.4',
    description='abu API',
    long_description='Private API for abu',
    author='Chris',
    author_email='10512@qq.com',
    url='https://github.com/ChrisYP/abu',
    license='MIT',
    packages=find_packages(where='src'),
    py_modules=['abu'],
    package_dir={'': 'src'},
    install_requires=[],
    platforms=["all"],
    include_package_data=True,
    zip_safe=False,
    keywords='abu',
)
