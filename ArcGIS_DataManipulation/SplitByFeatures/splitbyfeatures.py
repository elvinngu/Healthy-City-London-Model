# Name: splitbyfeatures.py
# Description: Split vegetation layer into separate feature classes for each climate zone
# Author: ESRI

# import system modules 
import arcpy 

# Set environment settings
arcpy.env.workspace = 'H:\ArcGIS\Default1.gdb'

# Split layer by boroughs, write to Output.gdb
splitData = 'H:\ArcGIS\Default1.gdb\Households\Households.shp'
splitFeatures = "H:\ArcGIS\Default1.gdb\LondonBorough.shp"
splitField = "ctyua15nm"
outWorkspace = "H:\ArcGIS\Default1.gdb\Households"
clusterTol = "1 Meters"
arcpy.Split_analysis(splitData, splitFeatures, splitField, outWorkspace, clusterTol)
