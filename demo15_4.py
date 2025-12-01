# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo15_4.py
    Author: Shawn Hutchinson
    Description:  Example script using SA functions to compute NDVI
    Date created: December 1, 2025
    Python Version: 3.11.11
"""

# Import required modules
import arcpy, os

# Define local variable(s)
inputGrid = "LANDSAT8_20150609"
inputWorkspace = r"D:\Teaching\GEOG728_Projects\GitHub-Rasters\GitHub-Rasters\ExerciseData.gdb"
outWorkspace = r"D:\Teaching\GEOG728_Projects\GitHub-Rasters\GitHub-Rasters\scratch.gdb"

# Set environment(s)
arcpy.env.workspace = inputWorkspace
arcpy.env.overwriteOutput = True

# Use try-except block to capture errors
try:
    # Check for required extension(s) and perform calculations
    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")

    # Use map algebra with SA functions to compute NDVI        
        num = arcpy.sa.Float(inputGrid + "\\Band_5") - arcpy.sa.Float(inputGrid + "\\Band_4")
        denom = arcpy.sa.Float(inputGrid + "\\Band_5") + arcpy.sa.Float(inputGrid + "\\Band_4")
        ndvi = arcpy.sa.Divide(num, denom)

        #Describe output and write custom output raster
        desc = arcpy.Describe(inputGrid)
        ndvi.save(os.path.join(outWorkspace, desc.baseName + "_NDVI"))

        # Check in required extension(s)
        arcpy.CheckInExtension("Spatial")
    else:
        print("Required Spatial Analyst extension is not available!")

# Trap geoprocessing errors
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))

# Trap remaining errors	
except Exception as e:
    print("General Error: {0}".format(str(e)))