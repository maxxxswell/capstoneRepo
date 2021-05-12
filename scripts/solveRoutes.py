# Author: Max McDonald
# Name: solveRoutes.py
# Description: Takes a set of network dataset stops
# solves the best route in a network dataset
# and saves it to a new location

# import the arcpy module
import arcpy

# check out the network analyst extension
arcpy.CheckOutExtension('network')

# set environments
arcpy.env.workspace = r'/myStops.gdb'

# local variables
networkDataset = r'/myNetworkDataset.gdb/myNetworkDataset'
impedanceField = 'Minutes'
inputOrder = 'USE_INPUT_ORDER'
preservation = 'PRESERVE_BOTH'
windows = 'NO_TIMEWINDOWS'
accumulators = 'Cost;Domestic_Price;Meters;Hours;Imported_Price;Kilometers;Minutes'
uTurnPolicy = 'ALLOW_UTURNS'
restrictions = ''
hierarchy = 'NO_HIERARCHY'
hierarchyRank = ''
pathShape = 'TRUE_LINES_WITH_MEASURES'
startDate = ''
unlocatedStops = 'SKIP'
solveError = 'TERMINATE'

# immutable variables
network = 'networkLayer'
routeLayer1 = 'routeLayer'
myStops = 'Stops'
routeLayer2 = routeLayer1
routeLayer3 = routeLayer2
routes = 'currentRoute'
routeLayers = 'selectedRouteLayers'
myStopsList = arcpy.ListFeatureClases()
counter = 0

# loop through each OD in myStopsList
for originDestination in myStopsList:
    # variables 
    route = r'/myRouteWorkspace.gdb/Route_' + str(counter).zfill(4)
    # make a temporary route layer
    arcpy.MakeRouteLayer_na(Network_ND, 
    network, impedanceField, inputOrder, preservation, windows, accumulators, 
    uTurnPolicy, restrictions, hierarchy, hierarchyRank, pathShape, startDate)
    # add the current OD to the network layer
    arcpy.AddLocations_na(routeLayer1, myStops, originDestination)
    # solve the route for the current OD pair
    arcpy.Solve_na(routeLayer2, unlocatedStops, solveError)
    # select the newly solved route
    arcpy.SelectData_management(routeLayer3, currentRoute)
    # make selection a feature layer
    arcpy.MakeFeatureLayer_management(routes, routeLayers)
    # save the selection as a feature class
    arcpy.CopyFeatures_management(routeLayers, route)
    # increase counter
    counter += 1
    # debugger
    print(route + 'saved')
    # delete temporary layers
    arcpy.Delete_management(network)
    arcpy.Delete_management(routeLayers)
