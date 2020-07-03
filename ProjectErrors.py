#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:49:38 2020

@author: collinbrahana
"""
class ERROR(Exception):
    pass

class IDENTIFIERassignmentERROR(ERROR):
    def __init__(self):
        return """Attempted to create new identifier for node that already had one.
          This is catastrophic. Don't even think it. If you are attempting
          something allowable under the datastructure design, try doing
          it differently to avoid database conflicts."""

class DATABASEretrivalERROR(ERROR):
    def __init__(self):
        return """That NIN could not be found, or something else went wrong in the database."""

class DATABASEexportERROR(ERROR):
    def __init__(self):
        return None#"""Commit to Database failed for some reason."""