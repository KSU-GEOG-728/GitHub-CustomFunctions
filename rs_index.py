# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: rs_index.py
    Author: Shawn Hutchinson
    Description:  Module with example function to calculate NDVI from Landsat 8 image
    Date created: December 1, 2025
    Python Version: 3.11.11
"""

def ndvi(inLandsat8):  #after Rouse et al., 1974
    import arcpy
    arcpy.CheckOutExtension("Spatial")
    num = arcpy.sa.Float(inLandsat8 + "\\Band_5") - arcpy.sa.Float(inLandsat8 + "\\Band_4")
    denom = arcpy.sa.Float(inLandsat8 + "\\Band_5") + arcpy.sa.Float(inLandsat8 + "\\Band_4")
    ndvi = arcpy.sa.Divide(num, denom)
    return ndvi
    arcpy.CheckInExtension("Spatial")
  
if __name__ == "__main__":

    # Import required module(s)
    import arcpy, os, rs_index

    # Define local variable(s)
    inLandsat8 = "LANDSAT8_20170513"  ##Choices:  "LANDSAT8_20150609" "LANDSAT8_20160510" "LANDSAT8_20170513"
    inputWorkspace = r"D:\Teaching\GEOG728_Projects\GitHub-Rasters\GitHub-Rasters\ExerciseData.gdb"
    outputWorkspace = r"D:\Teaching\GEOG728_Projects\GitHub-Rasters\GitHub-Rasters\scratch.gdb"

    #Set environment(s) 
    arcpy.env.workspace = inputWorkspace
    arcpy.env.overwriteOutput = True

    #Perform geoprocessing and save output
    desc = arcpy.Describe(inLandsat8)
    myNdvi = rs_index.ndvi(inLandsat8)
    myNdvi.save(os.path.join(outputWorkspace, desc.basename + "_NDVI3"))