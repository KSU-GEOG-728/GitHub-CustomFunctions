# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo15_1.py
    Author: Shawn Hutchinson
    Description:  Example script for listing fields in a table
    Date created: November 27, 2025
    Python Version: 3.11.11
"""

# Import required modules
import arcpy

# Set environment(s)
arcpy.env.workspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"

# Create local variable(s)
nameList = []

# Create a list of names of string fields in a table or feature class
fields = arcpy.ListFields("KonzaTreatments", "", "String")
for field in fields:
    nameList.append(field.baseName)
print(nameList)