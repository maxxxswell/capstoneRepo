# import modules
import arcpy
import os

# set workspace for all routes
arcpy.env.workspace = r"myRoutes.gdb"

# create an empty list
featureClasses = []

# walk through geodatabase for filename in filenames
for dirpath, dirnames, filenames in arcpy.da.Walk(arcpy.env.workspace, datatype="FeatureClass", type="Polyline"):
    for filename in filenames:
        # describe it 
        desc = arcpy.Describe(os.path.join(dirpath, filename))
        # if describe shapetype is polyline
        if desc.shapeType == "Polyline":
            # add it to list
            featureClasses.append(os.path.join(dirpath, filename))

# merge all list items to destination
arcpy.Merge_management(featureClasses, r"myDestination/myFileName)
