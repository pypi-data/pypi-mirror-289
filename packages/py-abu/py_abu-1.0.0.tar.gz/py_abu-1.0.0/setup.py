# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 18:36
# @Author  : Chris
# @Email   : 10512@qq.com
# @File    : setup.py
# @Software: PyCharm


from distutils.core import setup

setup(
    name='py-abu',
    version='1.0.0',
    description='abu API',
    long_description='Private API for abu',
    author='Chris',
    author_email='10512@qq.com',
    url='https://github.com/ChrisYP/abu',
    install_requires=[],
    license='MIT',
    packages=["abu"],
    package_dir={'abu': 'abu'},
    platforms=["all"],
    include_package_data=True,
    zip_safe=False,
    keywords='abu',
)
