#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creted on Sat Jun  6 14:01:23 2020

@author: collinbrahana
"""
#Necessary imports here
from NODEdata import NODEdata
from interfaceDATABASE import interfaceDATABASEnode
import uuid
import ProjectErrors

class Node: 
    def __init__(self,createtype,interface_object): #N0000012 
        self.dc = NODEdata() #Create instance of Node Dataclass for storage internally
        self.interface_obj = interface_object
        if createtype != 0: #Looking for a NIN here
            if self.interface_obj.checkNODEexistance(createtype) == 1: #Makes sure node in DB exists
                temp_node_tuple = self.interface_obj.fetchNODE(createtype)
                self.dc.NIN = temp_node_tuple[0]
                self.ChangeNODETYPE(temp_node_tuple[1])
                self.ChangeNAME(temp_node_tuple[2])
            else:
                raise ProjectErrors.DATABASEretrivalERROR
        else:
            self.dc.NIN = self.newNIN()
                
   #Memory Structures      
   def newNIN(self): #N0000006
        if self.dc.NIN == 0:
            self.dc.NIN = uuid.uuid4()
        else:
            raise ProjectErrors.IDENTIFIERassignmentERROR 
   
   def AddLinks(self,LINK): #N0000004 N0000005
        self.dc.LINKS.append(LINK)
        return 0
    
    def ChangeNAME(self,new_name):
        self.dc.NAME = new_name
        #UpdateNode()
    
    def ChangeNODETYPE(self,new_type): 
        self.dc.NODETYPE = new_type
        #UpdateNode()
    
    def retriveNIN(self):
        return self.dc.NIN
    
    #Database Structures       
    def DeleteLINK(self,tgt_NIN_1,tgt_NIN_2,tgt_NODETYPE):
        #look in node for (NIN_1,NIN_2,NODETYPE) and (NIN_2,NIN_1, -1*NODETYPE)
        #If it exists, perform deletion operation. If neither exist, raise an error.
        pass
    
    def updateDATABASE(self):
        pass
    
    def retreiveNODE(self,tgt,tgt_type):
        pass
    
    #Database Access

