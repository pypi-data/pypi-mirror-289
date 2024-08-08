'''
Author: qingfeng
Date: 2024-01-11 20:34:49
LastEditTime: 2024-01-18 20:16:29
FilePath: /sinatools/setup.py
Description: setup
'''
from setuptools import setup, find_packages
setup(name='sinaSearchTools',
      version='6.4.0',
      description='sina搜索常用的函数',
      author='qingfeng',
      author_email='qingfeng7@staff.sina.com.cn',
      requires=['numpy',
                'requests',
                'prettytable',
                'PyYAML',
                'pandas'],
      packages=find_packages(),  # 系统自动从当前目录开始找包
      # 如果有的文件不用打包，则只能指定需要打包的文件
      license="apache 3.0"
      )
