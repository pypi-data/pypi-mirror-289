#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
# from __future__ import absolute_import, print_function, division
# ----------------------------------------------------------------
# File Name:        __init__.py
# Author:           Jiwei Huang
# Version:          0.0.1
# Created:          2012/01/01
# Description:      Main Function: gxusthjw包的__init__.py。
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
from . import axs
from . import commons
from . import data
from . import findpeaks
from . import fitykers
from . import fityks
from . import fsd
from . import ftir
from . import genetic
from . import ma
from . import mathematics
from . import matlab
from . import nmr
from . import origins
from . import peakfits
from . import raman
from . import spectrum
from . import statistics
from . import ta
from . import units
from . import xps
from . import xrd
from . import zhxyao

# 定义 ============================================================
__version__ = "0.0.1"

__author__ = "Jiwei Huang"

__doc__ = """
the python libraries of gxusthjw.
"""

# noinspection DuplicatedCode
__all__ = [
    'axs',
    'commons',
    'data',
    'findpeaks',
    'fitykers',
    'fityks',
    'fsd',
    'ftir',
    'genetic',
    'ma',
    'mathematics',
    'matlab',
    'nmr',
    'origins',
    'peakfits',
    'raman',
    'spectrum',
    'statistics',
    'ta',
    'units',
    'xps',
    'xrd',
    'zhxyao',
]
# ==================================================================
