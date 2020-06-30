#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creted on Sat Jun  6 14:01:23 2020

@author: collinbrahana
"""
#Necessary imports here
from NODEdata import NODEdata, LINKdata
import uuid
import ProjectErrors
import sqlite3

class Node: 
    def __init__(self,tgt,tgt_type):
        inDB = 0#bool check if given UUID exists in database
        if inDB == 1:
            self.NODE = NODEdata(retreiveNODE(1,1))
        else:
            self.NODE = NODEdata(0,0,0,"","",[])
        
    def AddLinks(self,LINK): #N0000004 N0000005
        self.NODE.LINKS.append(LINK)
        return 0
    
    def ChangeNAME(self,new_name):
        self.NODE.NAME = new_name
        #UpdateNode()
    
    def ChangeNODETYPE(self,new_type): 
        self.NODE.NODETYPE = new_type
        #UpdateNode()
    
    def ChangePIN(self,new_PIN): #N0000007
        if self.NODE.PIN == 0:
            self.NODE.PIN = new_PIN
        else:
            raise ProjectErrors.IDENTIFIERassignmentERROR
           
    def DeleteLINK(self,tgt_NIN_1,tgt_NIN_2,tgt_NODETYPE):
        #look in node for (NIN_1,NIN_2,NODETYPE) and (NIN_2,NIN_1, -1*NODETYPE)
        #If it exists, perform deletion operation. If neither exist, raise an error.
        pass
    
    def newNIN(self): #N0000006
        if self.NODE.NIN == 0:
            self.NODE.NIN = uuid.uuid4()
        else:
            raise ProjectErrors.IDENTIFIERassignmentERROR
    
    def updateDATABASE(self):
        pass
    
    def retreiveNODE(self,tgt,tgt_type):
        pass

