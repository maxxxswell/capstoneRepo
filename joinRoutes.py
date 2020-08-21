# Author: Max McDonald
# Name: joinRoutes
# Description: Walks through files in gdb and merges all
# files that are polylines before saving merged files to 
# a new location

# import arcpy and os modules
import arcpy
import os

# set environments
arcpy.env.workspace = r"myRoutes.gdb"

# create an empty list
featureClasses = []

# walk through gdb files
for dirpath, dirnames, filenames in arcpy.da.Walk(arcpy.env.workspace, datatype="FeatureClass", type="Polyline"):
    for filename in filenames:
        # describe the current feature class
        desc = arcpy.Describe(os.path.join(dirpath, filename))
        # if describe shapetype is polyline...
        if desc.shapeType == "Polyline":
            # add it to list
            featureClasses.append(os.path.join(dirpath, filename))

# merge all feature classes in list 
arcpy.Merge_management(featureClasses, r"myDestination/myFileName)
