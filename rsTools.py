#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: rs_index.py
    Author: Shawn Hutchinson
    Description:  Module with example custom class and function to calculate NDVI from Landsat OLI or TM sensors
    Date created: November 27, 2023
    Python Version: 3.9.16
"""

class Landsat(object):
    
    def __init__(self, sensorType, rasterIn):
        self.sensorType = sensorType
        self.rasterIn = rasterIn

    def ndvi(self):  #after Rouse et al., 1974
        import arcpy
        arcpy.CheckOutExtension("Spatial")
        if self.sensorType == "OLI":
            num = arcpy.sa.Float(self.rasterIn + "\\Band_5") - arcpy.sa.Float(self.rasterIn + "\\Band_4")
            denom = arcpy.sa.Float(self.rasterIn + "\\Band_5") + arcpy.sa.Float(self.rasterIn + "\\Band_4")
        else:
            num = arcpy.sa.Float(self.rasterIn + "\\Band_4") - arcpy.sa.Float(self.rasterIn + "\\Band_3")
            denom = arcpy.sa.Float(self.rasterIn + "\\Band_4") + arcpy.sa.Float(self.rasterIn + "\\Band_3")
        ndvi = arcpy.sa.Divide(num, denom)
        return ndvi
        arcpy.CheckInExtension("Spatial")
        
if __name__ == "__main__":

    import arcpy, os, rsTools
    arcpy.env.workspace = "D:/GitHub/GitHub-Rasters/ExerciseData.gdb"
    arcpy.env.overwriteOutput = True

    sensorType = "TM"
    inputGrid = "LANDSAT5_20110801"  #Choices: "LANDSAT5_20110801" "LANDSAT8_20150609" "LANDSAT8_20160510" "LANDSAT8_20170513"
    outputWorkspace = "D:/GitHub/GitHub-Rasters/scratch.gdb"

    desc = arcpy.Describe(inputGrid)
    myImage = rsTools.Landsat(sensorType, inputGrid)
    myNdvi = myImage.ndvi()
    myNdvi.save(os.path.join(outputWorkspace, desc.basename + "_NDVI5"))