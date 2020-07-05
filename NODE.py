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
# ^^^ Move this to main when we start transistion over
import sqlite3


class DBapi:
    def __init__(self):
        pass

    def connectDATABASE(self):
        self.connection = sqlite3.connect("Minddancer.db")
        self.cursor = self.connection.cursor
        return None

    def checkNODEexistance(self, tgt_NIN):
        t = (tgt_NIN,)
        self.cursor.execute("SELECT * FROM NODES WHERE NIN = ?", t)
        if self.cursor.fetchone == None:
            return 0
        else:
            return 1

    def exportNODEtoDATABASE(self):  #Only call this to make a new node, NOT TO UPDATE
        t = (self.dc.NIN, self.dc.NODETYPE, self.dc.NAME, self.dc.DATA,)
        self.cursor.execute("INSERT INTO NODES VALUES (?,?,?,?)", t)
        self.connection.commit
#        if self.checkNODEexistance(self.dc.NIN) == 1:
#            raise ProjectErrors.DATABASEexportERROR
        return None

    def fetchNODEfromDATABASE(self, tgt_NIN):
        self.connectDATABASE
        t = (tgt_NIN,)
        output = self.cursor.execute("SELECT * FROM NODES WHERE NIN=?", t) #N0000011
        outtuple = output.fetchone
        self.dc.NIN = outtuple[0]
        self.dc.NODETYPE = outtuple[1]
        self.dc.NAME = outtuple[2]
        self.dc.DATA = outtuple[3]
        self.closeDATABASE
        return outtuple

    def fetchLINKLISTfromDATABASE(self, tgt_NIN):
        self.connectDATABASE
        t = (tgt_NIN, )
        cmd = "SELECT * FROM NODES WHERE NIN_ONE=?"
        self.cursor.execute(cmd, t)
        print(self.cursor.fetchall())
        
    def updateNODES(self, NT, NA, D, NIN):
        self.connectDATABASE
        t = (NT, NA, D, NIN, )
        cmd = "UPDATE NODES SET NODETYPE=?, NAME=?, DATA=? WHERE NIN=?"
        self.cursor.execute(cmd, t)
        self.connection.commit
        self.closeDATABASE
    
    def updateLINKS(self,N1,N2,LT):
        self.connectDATABASE
        LT2 = -1*LT
        t = (N1,N2,LT)
        t2 = (N2,N1,LT2)
        cmd = "UPDATE LINKS SET LINK_ONE=?, LINK_TWO=?, LINKTYPE=?"
        self.cursor.execute(cmd, t)
        self.cursor.execute(cmd, t2)
        self.connection.commit
        self.closeDATABASE

    def closeDATABASE(self):
        self.connection.close
        return None


class Node(DBapi):
    def __init__(self, createtype):  #N0000012
        self.dc = NODEdata("", 0, "", "", []) #Create instance of Node Dataclass for storage internally
        iDB.createTABLES # I should move this to startup, we don't need to run it for every node, just an existance check
        self.connectDATABASE
        if createtype != 0:  #Looking for a string NIN here
            if self.checkNODEexistance(createtype) == 1: #Makes sure node in DB exists                
                temp_node_tuple = self.fetchNODEfromDATABASE(createtype)
                self.dc.NIN = temp_node_tuple[0]
                self.changeNODETYPE(temp_node_tuple[1])
                self.changeNAME(temp_node_tuple[2])
                self.closeDATABASE
            else:
                self.closeDATABASE
                raise ProjectErrors.DATABASEretrivalERROR
        else:
            self.makeNIN
            self.dc.NIN = str(self.dc.NIN)
            self.exportNODEtoDATABASE
            self.closeDATABASE
        return None

    # Memory Structures
    def makeNIN(self):  # N0000006
        if self.dc.NIN == "":
            self.dc.NIN = uuid.uuid4
        else:
            raise ProjectErrors.IDENTIFIERassignmentERROR

    def AddLinks(self, LINK):  # N0000004 N0000005
        self.dc.LINKS.append(LINK)
        return None

    def changeNAME(self, new_name):
        self.dc.NAME = new_name
        self.updateNODES(self.dc.NODETYPE, self.dc.NAME, self.dc.DATA, self.dc.NIN)
        return None

    def changeNODETYPE(self, new_type): 
        self.dc.NODETYPE = new_type
        self.updateNODES(self.dc.NODETYPE, self.dc.NAME, self.dc.DATA, self.dc.NIN)
        return None

    def returnNIN(self):
        return self.dc.NIN

    def DeleteLINK(self, tgt_NIN_1, tgt_NIN_2, tgt_NODETYPE):
        # look in node for (NIN_1,NIN_2,NODETYPE) and (NIN_2,NIN_1, -1*NODETYPE)
        # If it exists, perform deletion operation. If neither exist, raise an error.
        pass

    def fetchNODEfromMEMORY(self):
        pass

node = Node(0)