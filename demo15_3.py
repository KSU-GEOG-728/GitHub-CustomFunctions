#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo15_3.py
    Author: Shawn Hutchinson
    Description:  Example script for listing fields using a function in a custom module
    Date created: November 27, 2023
    Python Version: 3.9.16
"""

# Import required modules
import arcpy, mytools

# Set environment(s)
arcpy.env.workspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"

# Create a list of names of string fields in a table or feature class
fieldNames = mytools.listFieldNames("KonzaTreatments") 
print(fieldNames)