# -*- coding: utf-8 -*-
# file: setup.py
# author: JinTian
# time: 12/02/2021 12:16 PM
# Copyright 2022 JinTian. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------

from setuptools import setup, find_packages

version_file = 'wanwu/version.py'


def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


setup(name='wanwu',
      version=get_version(),
      keywords=['deep learning', 'script helper', 'tools'],
      description='Wanwu: Everything can have intelligence',
      long_description='''
      wanwu enables fastest inference on your target device by intelli switch TensorRT, OpenVINO, tvm etc automatically.
      also provides many model inference out-of-box without any further dependecies or development.
      ''',
      license='GPL-3.0',
      packages=[
          'wanwu.core',
          'wanwu.core.backends',
          'wanwu.det',
          'wanwu.seg',
          'wanwu.kps',
          'wanwu.cls',
          'wanwu.utils',
          'wanwu.track',
          'wanwu.base',
          'wanwu'
      ],
      entry_points={
          'console_scripts': [
              'wanwu = wanwu.wanwu:main'
          ]
      },
      author="Lucas Jin",
      author_email="jinfagang19@163.com",
      url='https://github.com/jinfagang/wanwu',
      platforms='any',
      install_requires=['colorama', 'requests', 'numpy', 'future', 'onnx',
                        'deprecated', 'alfred-py', 'onnxruntime', 'tabulate']
      )
