# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo15_6.py
    Author: Shawn Hutchinson
    Description:  Example script for calling an external custom function
    Date created: December 1, 2025
    Python Version: 3.11.11
"""

# Import required module(s)
import arcpy, os, rs_index

# Define local variable(s)
inputGrid = "LANDSAT8_20160510"     ##Choices:  "LANDSAT8_20150609" "LANDSAT8_20160510" "LANDSAT8_20170513"
inputWorkspace = r"D:\Teaching\GEOG728_Projects\GitHub-Rasters\GitHub-Rasters\ExerciseData.gdb"
outputWorkspace = r"D:\Teaching\GEOG728_Projects\GitHub-Rasters\GitHub-Rasters\scratch.gdb"

#Set environment(s)
arcpy.env.workspace = inputWorkspace
arcpy.env.overwriteOutput = True

# Use try-except block to capture errors
try:
	# Check for required extension(s) and perform calculations
	if arcpy.CheckExtension("Spatial") == "Available":
		arcpy.CheckOutExtension("Spatial")

		# Use custom function to calculate NDVI
		ndvi = rs_index.ndvi(inputGrid)

		# Describe output and write custom output raster
		desc = arcpy.Describe(inputGrid)
		ndvi.save(os.path.join(outputWorkspace, desc.baseName + "_NDVI4"))

		# Check in required extension(s)
		arcpy.CheckInExtension("Spatial")
		
	else:
		print("Required Spatial Analyst extension is not available!")

except arcpy.ExecuteError:
    # Print level 2 severity geoprocessing messages
    print(arcpy.GetMessages(2))