#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:04:53 2020

@author: collinbrahana
"""

import sqlite3


def createTABLES():
    conn = sqlite3.connect("Minddancer.db") #N0000009
    c = conn.cursor()

    str_two = """
    CREATE TABLE IF NOT EXISTS NODES (
    "NIN"        TEXT,
    "NODETYPE"   INTEGER NOT NULL,
    "NAME"       TEXT,
    "DATA"       BLOB,

    PRIMARY KEY (NIN)
    );

    CREATE TABLE IF NOT EXISTS LINKS (
            "LINK_ONE"   INT  NOT NULL,
            "LINK_TWO"   INT  NOT NULL,
            "LINKTYPE"  INT NOT NULL,
    
    PRIMARY KEY (LINK_ONE,LINK_TWO,LINKTYPE)
    );
    """
    
    c.executescript(str_two)
    conn.commit()
    conn.close()
    return None

def dropTABLES(tgt_database): #DEBUG ONLY, EXTREMELY RISKY, DO NOT USE WITHOUT BACKUP OF DATABASE!
    pass
    







