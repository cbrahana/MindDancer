#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:36:31 2020

@author: collinbrahana
"""

from dataclasses import dataclass
@dataclass
class NODEdata:
    NIN: int
    NODETYPE: int
    NAME: str
    DATA: str
    LINKS: list

@dataclass
class LINKdata:
    NIN_1: str
    NIN_2: str
    LINKTYPE: int #N0000008