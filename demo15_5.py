# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo15_4.py
    Author: Shawn Hutchinson
    Description:  Example script for calling an embedded function to calculate NDVI from Landsat 8 image
    Date created: November 27, 2025
    Python Version: 3.11.11
"""

# Function definition for NDVI
def ndvi(inLandsat8):  #after Rouse et al., 1974
    import arcpy
    arcpy.CheckOutExtension("Spatial")
    num = arcpy.sa.Float(inLandsat8 + "/Band_5") - arcpy.sa.Float(inLandsat8 + "/Band_4")
    denom = arcpy.sa.Float(inLandsat8 + "/Band_5") + arcpy.sa.Float(inLandsat8 + "/Band_4")
    ndvi = arcpy.sa.Divide(num, denom)
    return ndvi
    arcpy.CheckInExtension("Spatial")

# Import required module(s)
import arcpy, os

# Define local variable(s)
inputGrid = "LANDSAT8_20150609"     ##Choices:  "LANDSAT8_20150609" "LANDSAT8_20160510" "LANDSAT8_20170513"
inputWorkspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"
outputWorkspace = "D:/GitHub/GitHub-Rasters/scratch.gdb"

# Set environment(s)
arcpy.env.workspace = inputWorkspace
arcpy.env.overwriteOutput = True

# Use try-except block to capture errors
try:
	# Check for required extension(s) and perform calculations
	if arcpy.CheckExtension("Spatial") == "Available":
		arcpy.CheckOutExtension("Spatial")

		# Use custom function to calculate NDVI
		ndvi = ndvi(inputGrid)

		# Describe output and write custom output raster
		desc = arcpy.Describe(inputGrid)
		ndvi.save(os.path.join(outputWorkspace, desc.basename + "_NDVI2"))

		# Check in required extension(s)
		arcpy.CheckInExtension("Spatial")
		
	else:
		print("Required Spatial Analyst extension is not available!")

# Trap geoprocessing errors
except arcpy.ExecuteError:
    # Print level 2 severity geoprocessing messages
    print(arcpy.GetMessages(2))

# Trap remaining errors	
except Exception as e:
    print("General Error: {0}".format(str(e)))