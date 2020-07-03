#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creted on Sat Jun  6 14:01:23 2020

@author: collinbrahana
"""
#Necessary imports here
from NODEdata import NODEdata
import uuid
import ProjectErrors
import interfaceDATABASE as iDB
import sqlite3

class Node: 
    def __init__(self,createtype): #N0000012 
        self.dc = NODEdata(0,0,"","",[]) #Create instance of Node Dataclass for storage internally
        self.connectDATABASE()
        iDB.createTABLES()
        if createtype != 0: #Looking for a NIN here
            if self.checkNODEexistance(createtype) == 1: #Makes sure node in DB exists
                temp_node_tuple = self.fetchNODEfromDATABASE(createtype)
                self.dc.NIN = temp_node_tuple[0]
                self.ChangeNODETYPE(temp_node_tuple[1])
                self.ChangeNAME(temp_node_tuple[2])
                return None
            else:
                raise ProjectErrors.DATABASEretrivalERROR
        else:
            self.dc.NIN = self.makeNIN()
            self.exportNODEtoDATABASE()
            return None
    
    #Memory Structures      
    def makeNIN(self): #N0000006
        if self.dc.NIN == 0:
            self.dc.NIN = uuid.uuid4()
        else:
            raise ProjectErrors.IDENTIFIERassignmentERROR 
   
    def AddLinks(self,LINK): #N0000004 N0000005
        self.dc.LINKS.append(LINK)
        return None
    
    def ChangeNAME(self,new_name):
        self.dc.NAME = new_name
        #self.exportNODEtoDATABASE() #This needs to be update
        return None
    
    def ChangeNODETYPE(self,new_type): 
        self.dc.NODETYPE = new_type
        #self.exportNODEtoDATABASE() #This needs to be update
        return None
    
    def returnNIN(self):
        return self.dc.NIN
    
    #Database Structures       
    def DeleteLINK(self,tgt_NIN_1,tgt_NIN_2,tgt_NODETYPE):
        #look in node for (NIN_1,NIN_2,NODETYPE) and (NIN_2,NIN_1, -1*NODETYPE)
        #If it exists, perform deletion operation. If neither exist, raise an error.
        pass
    
    def fetchNODEfromMEMORY(self,tgt,tgt_type):
        pass
    
    #Database Access
    def connectDATABASE(self):
        self.connection = sqlite3.connect("Minddancer.db")
        self.cursor = self.connection.cursor()
        return None
    
    def checkNODEexistance(self,tgt_NIN):
        t = (tgt_NIN,)
        self.cursor.execute("SELECT * FROM NODE WHERE NIN = ?",t)
        if self.cursor.fetchone() == None:
            return 0
        else:
            return 1
    
    def exportNODEtoDATABASE(self): #Only call this to make a new node, NOT TO UPDATE
        t = (self.dc.NIN,self.dc.NODETYPE,self.dc.NAME,self.dc.DATA)
        self.cursor.execute("INSERT INTO NODE VALUES (?,?,?,?)",t)
        self.connection.commit()
        if self.checkNODEexistance(self.dc.NIN) != 1:
            raise ProjectErrors.DATABASEexportERROR
        return None
    
    def fetchNODEfromDATABASE(self,tgt_NIN):
        t = (tgt_NIN,)
        output = self.cursor.execute("SELECT * FROM NODE WHERE NIN=?",t) #N0000011
        outtuple = output.fetchone()
        self.dc.NIN = outtuple[0]
        self.dc.NODETYPE = outtuple[1]
        self.dc.NAME = outtuple[2]
        self.dc.DATA = outtuple[3]
        return None
    
    def closeDATABASE(self):
        self.connection.close()
        return None

errortest = Node(0)