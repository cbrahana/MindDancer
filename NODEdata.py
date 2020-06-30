#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:36:31 2020

@author: collinbrahana
"""

from dataclass import dataclass
@dataclass
class NODEdata:
    NIN: int
    PIN: int
    NODETYPE: int
    NAME: str
    DATA: str
    LINKS: list
