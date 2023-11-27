#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: mytools.py
    Author: Shawn Hutchinson
    Description:  Module containing a custom function for listing fields in a table
    Date created: November 27, 2023
    Python Version: 3.9.16
"""

# Function definition
def listFieldNames(table):
    import arcpy
    fields = arcpy.ListFields(table, "", "String")
    nameList = []
    for field in fields:
        nameList.append(field.baseName)
    return nameList