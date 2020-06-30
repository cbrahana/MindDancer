#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:04:53 2020

@author: collinbrahana
"""

import sqlite3

def createDATABASE(tgt_database):
    conn = sqlite3.connect(tgt_database) #N0000009
    c = conn.cursor()

    str_two = """CREATE TABLE IF NOT EXISTS NODE (
    "NIN"        INTEGER,
    "PIN"        INTEGER  NOT NULL,
    "NAME"       TINYTEXT,
    "NODETYPE"   INTEGER  NOT NULL,
    "DATA"       BLOB,

    PRIMARY KEY (NIN)
    );

    CREATE TABLE IF NOT EXISTS LINK (
            "LINK_ONE"   INT  NOT NULL,
            "LINK_TWO"   INT  NOT NULL,
            "LINKTYPE"  INT NOT NULL,
    
    PRIMARY KEY (LINK_ONE,LINK_TWO,LINKTYPE)
    );
    """
    
    c.executescript(str_two)
    return conn
#%%
class interfaceDATABASEnode:
    def __init__(self,tgt_database_file):
        self.tgt_database_file = tgt_database_file
        self.connection = sqlite3.connect(self.tgt_database_file)
        self.c = self.connection.cursor()
    
    def checkNODEexistance(self,tgt_UUID):
        t = (tgt_UUID,)
        self.c.execute("SELECT * FROM NODE WHERE NIN = ?",t)
        if self.c.fetchone() == None:
            return 0
        else:
            return 1

    def exportNODE(self,NIN,PIN,NODETYPE,NAME,DATA):
        t = (NIN,PIN,NODETYPE,NAME,DATA)
        self.c.execute("INSERT INTO NODE VALUES (?,?,?,?,?)",t)
        self.connection.commit()
        return 0
    

faust = interfaceDATABASEnode("testdatabase.db")
print(faust.exportNODE(0,0,0,"Hello","HiThere"))
#print(faust.checkNODEexistance(0))
#%%