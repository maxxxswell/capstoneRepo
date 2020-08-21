import arcpy
import os

arcpy.env.workspace = r"d:/PennState/CapstoneProject/TrainAccessibility.gdb/"

featureClasses = []

for dirpath, dirnames, filenames in arcpy.da.Walk(arcpy.env.workspace, datatype="FeatureClass", type="Polyline"):
    for filename in filenames:
        desc = arcpy.Describe(os.path.join(dirpath, filename))
        if desc.shapeType == "Polyline":
            featureClasses.append(os.path.join(dirpath, filename))

arcpy.Merge_management(featureClasses, r"d:/PennState/CapstoneProject/Access.gdb/mergedTrainRoutes")
