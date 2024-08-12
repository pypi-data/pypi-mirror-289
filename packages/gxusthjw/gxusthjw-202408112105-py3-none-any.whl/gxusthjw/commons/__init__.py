#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        __init__.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: gxusthjw.commons包的__init__.py。
#                                  承载“常见的”函数和类。
#                   Outer Parameters: xxxxxxx
# Class List:       xxxxxxx
# Function List:    xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
#                   xxx() -- xxxxxxx
# History:
#        <author>        <version>        <time>        <desc>
#       Jiwei Huang        0.0.1         2012/01/01     create
#       Jiwei Huang        0.0.1         2023/10/30     revise
#       Jiwei Huang        0.0.1         2024/08/11     revise
# ----------------------------------------------------------------
# 导包 ============================================================
from .file_object import (get_file_encoding_chardet,
                          file_info,
                          get_file_info,
                          get_file_info_of_module,
                          get_file_object,
                          FileInfo,
                          FileObject)
from .unique_object import (random_string,
                            unique_string,
                            UniqueObject)

# 声明 ============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
The common functions and classes of the gxusthjw python libraries.
"""

__all__ = [
    'get_file_encoding_chardet',
    'file_info',
    'get_file_info',
    'get_file_info_of_module',
    'get_file_object',
    'FileInfo',
    'FileObject',
    'random_string',
    'unique_string',
    'UniqueObject',
]
# ==================================================================
