#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:47:53 2020

@author: collinbrahana
"""
#IMPORTS TO MAIN
import sqlite3
from os import path
import uuid

#IMPORTS TO OTHER FILES

#Modules
from database_start import connectDatabase
from nodeclass import Node

testnode = Node()

#Initilization Variables (MOVE TO INIT FILE)
current_database = "MindDancer.db"

