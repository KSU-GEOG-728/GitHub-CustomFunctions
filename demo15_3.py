# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo15_3.py
    Author: Shawn Hutchinson
    Description:  Example script for listing fields using a function in a custom module
    Date created: December 1, 2025
    Python Version: 3.11.11
"""

# Import required modules
import arcpy, mytools

# Set environment(s)
arcpy.env.workspace = r"D:\Teaching\GEOG728_Projects\GitHub-Rasters\GitHub-Rasters\ExerciseData.gdb"

# Create a list of names of string fields in a table or feature class
fieldNames = mytools.listFieldNames("KonzaTreatments") 
print(fieldNames)