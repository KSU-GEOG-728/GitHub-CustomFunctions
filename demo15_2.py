# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo15_2.py
    Author: Shawn Hutchinson
    Description:  Example script for listing fields in a table using an embedded function
    Date created: December 1, 2025
    Python Version: 3.11.11
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
arcpy.env.workspace = r"D:\Teaching\GEOG728_Projects\GitHub-Rasters\GitHub-Rasters\ExerciseData.gdb"

# Create a list of names of string fields in a table or feature class
fieldNames = listFieldNames("KonzaTreatments") 
print(fieldNames)