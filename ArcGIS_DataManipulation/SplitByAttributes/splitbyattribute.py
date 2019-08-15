import arcpy

arcpy.env.workspace = 'H:\ArcGIS\Default1.gdb'

import os
 
dirpath = os.getcwd()
print("current directory is : " + dirpath)

# SplitbyAttriutes
in_feature_class = 'H:\ArcGIS\Default1.gdb\HygieneData.shp'
target_workspace = 'H:\ArcGIS\Default1.gdb\HygieneData'
fields = ['Busines_Ty']
arcpy.SplitByAttributes_analysis(in_feature_class, target_workspace, fields)
list = arcpy.ListFeatureClasses()
