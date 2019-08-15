import arcpy
import pandas as pd

nodes = pd.read_csv(r'H:\ArcGIS\london.osmNODES.csv')
links = pd.read_csv(r'H:\ArcGIS\london.osmLINKS.csv')
output = r"H:/ArcGIS/londonDRIVE.shp"

# A list of features and coordinate pairs
results = []

for ii in range(0,len(links)):
    result = []
    jj = 0
    for field in links.iloc[ii]:
        jj += 1
        if field == 0:
            pass
        else:
            node = []
            if jj >= 7:
                coord = nodes.loc[nodes['NodeID'] == field]
                lat = coord['Latitude']
                lon = coord['Longtitude']
                node.append(float(lon))
                node.append(float(lat))
                result.append(node)
    results.append(result)

feature_info = results

# A list that will hold each of the Polyline objects
features = []

# Obtain spatial reference for WGS 1984
spatial_reference = arcpy.SpatialReference(4326)

for feature in feature_info:
    # Create a Polyline object based on the array of points
    # Append to the list of Polyline objects
    features.append(
        arcpy.Polyline(
            arcpy.Array([arcpy.Point(*coords) for coords in feature]),spatial_reference))


# Persist a copy of the Polyline objects using CopyFeatures
arcpy.CopyFeatures_management(features, output)

#input_fc = "H:/ArcGIS/polylines.shp"

#with arcpy.da.SearchCursor(input_fc,['SHAPE@']) as s_cur:
#                          for row in s_cur:
#                              polyline = row[0]
#                              for feature in polyline:
#                                  for point in feature:
#                                      print point



