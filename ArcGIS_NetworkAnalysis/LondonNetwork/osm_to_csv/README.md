# osm_to_csv

osm_to_csv is a function that converts a osm file from [OpenStreetMap](https://www.openstreetmap.org/export#map=13/51.5548/0.0647) to a csv file that contains information of the roads in the osm file. 

### How it works?

1. The user will input the osm filename into the function and run it. 

2. The code reads the OSM file and pass it into two csv file that contain the following information:  
(i) map.osmNODES.csv (node reference number, latitude, longitude)  
(ii) map.osmLINKS.csv (highway reference number, highway type, maxspeed, linked node reference numbers that are connected to form the roads)  

note: the code may take a considerable amount time (approx 30 minutes) if the osm file size is above 1GB. 

### Example Usage

```python

# Ensure the osm file is in the same folder as your python code before running the following line. 
nodesandlinks('map.osm') # 'map.osm' is your osm filename that you have downloaded.

```

### FAQ

1. What is an OSM file?  
An OSM file is essentially a XML file that contains information regarding the roads, buildings etc. in a geographic region. 
An OSM file can be downloaded from [OpenStreetMap](https://www.openstreetmap.org/export#map=13/51.5548/0.0647). 
You can choose the bounded region for which you want the network information. 

2. There is an error ('You have requested too many nodes. limit is 5000') when I select a region. How do I export a larger area?  
You can use the overpass API below the export button on [OpenStreetMap](https://www.openstreetmap.org/export#map=13/51.5548/0.0647).

3. Is there any software that can help me and osm to shapefile conversion ?  
Yes, but the ones that I can find are not free. There is a free ArcGIS open source tool but that requires ArcGIS 10.1 version.

4. What are the CSV files for?  
The CSV files created here are needed as inputs for the csv_to_shape.py python code. Refer to the csv_to_shape README documentation for further information.


### Help

Contact: elvinngu@gmail.com
