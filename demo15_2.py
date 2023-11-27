#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo15_2.py
    Author: Shawn Hutchinson
    Description:  Example script for listing fields in a table using an embedded function
    Date created: November 27, 2023
    Python Version: 3.9.16
"""

# Function definition in the same script
def listFieldNames(table):
    fields = arcpy.ListFields(table, "", "String")
    nameList = []
    for field in fields:
        nameList.append(field.baseName)
    return nameList

# Import required modules
import arcpy

# Set environment(s)
arcpy.env.workspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"

# Create a list of names of string fields in a table or feature class
fieldNames = listFieldNames("KonzaTreatments") 
print(fieldNames)