# Create a road network

The two sets of code can be used to create a road network (shapefile) of anywhere in the world as long as it is in OpenStreetMap's database.

# How?
Download a map.osm file from [OpenStreetMap](https://www.openstreetmap.org/export#map=12/51.5389/0.0803). The filetype is an OSM XML file. Use the osm_to_csv.py python code to convert the OSM XML file to a csv file. Then use the csv_to_shape.py python code to convert the csv file into a shapefile that contains polyline that connects roads/links on a map
