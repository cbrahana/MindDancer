#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creted on Sat Jun  6 14:01:23 2020

@author: collinbrahana
"""
#Necessary imports here
from NODEdata import NODEdata
import UUID
import ProjectErrors

class Node: 
    def __init__(self):
        self.NODE = NODEdata()
        
    def AddLinks(self,NIN_1,NIN_2,LINKTYPE): #N0000004 N0000005
        pass 
    
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
           
    def DeleteLink(self,tgt_NIN_1,tgt_NIN_2,tgt_NODETYPE):
        #look in node for (NIN_1,NIN_2,NODETYPE) and (NIN_2,NIN_1, CONVERT_NODETYPE)
        #If it exists, perform deletion operation. If neither exist, raise an error.
        pass
    
    def UpdateNode(self): #N0000003
        pass
    
    def newNIN(self): #N0000006
        if self.NODE.NIN == 0:
            self.NODE.NIN = UUID.uuid4()
        else:
            raise ProjectErrors.IDENTIFIERassignmentERROR
    
                

