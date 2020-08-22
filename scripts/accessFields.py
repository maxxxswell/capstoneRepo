# Author: Max McDonald
# Name: accessFields.py
# Description: inserts two new fields for ID and Accessibility Index
# calcualtes those fields with counter and sql equation

# import the arcpy module
import arcpy

# set environments
arcpy.env.workspace  = r"/myRouteWorkspace.gdb/"

# local variables
featureList = arcpy.ListFeatureClasses()
fieldName = "ID"
fieldType = "DOUBLE"
# I compared two different transportation modes 
fieldName2 = "DriveAccessIndex"
fieldName3 = "TrainAccessIndex"
# aligns with accumulators in solveRoutes.py but equation is user designed (yours may differ)
expressionDrive = "[Total_Miles] + [Total_Hours] * ([Total_Domestic_Price] * 2)"
expressionTrain = "[Total_T_Miles] + [Total_T_Hours] * ([Total_T_Cost] + [Total_T_Domestic_Price])"
counter = 1

# loop through featureList
for feature in featureList:
    # Add fieldName to feature; set fieldType
    arcpy.AddField_management(feature, fieldName, fieldType)
    print("Field name " + fieldName + " added to " + feature) # debugger
    # Add fieldName2 to feature; set fieldType
    arcpy.AddField_management(feature, fieldName3, fieldType) # could be fieldName2
    print("Field name " + fieldName3 + " added to " + feature) # debugger
    # calculate the fieldName
    arcpy.CalculateField_management(feature, fieldName, counter)
    print(feature + "'s " + fieldName + " field calculated: " + str(counter)) # debugger
    # calculate the fieldName3
    arcpy.CalculateField_management(feature, fieldName3, expressionTrain) # could be fieldName2 and expressionDrive
    print(feature + "'s " + fieldName3 + " field calculated")  # debugger
    # increase counter
    counter += 1
