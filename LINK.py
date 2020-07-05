#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:46:51 2020

@author: collinbrahana
"""
from NODEdata import LINKdata
from NODE import DBapi


class LINK(DBapi):
    def __init__(self):
        self.ld = LINKdata("", "", 0)
        return None

    def setLINK(self,NIN1,NIN2,LINKTYPE):
        self.ld.NIN_1 = NIN1
        self.ld.NIN_2 = NIN2
        self.ld.LINKTYPE = LINKTYPE
        
