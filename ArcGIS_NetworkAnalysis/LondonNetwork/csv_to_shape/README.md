# csv_to_shape

csv_to_shape is a script that converts the csv file made from the osm_to_csv.py python code into an ESRI polyline shapefile. This polyline shapefile can then be used to create a network database for further network analysis.

### How it works? 

1. The user first input the path link of the csv file created from osm_to_csv.py python code. 

```python
nodes = pd.read_csv(r'H:\ArcGIS\map.osmNODES.csv')
links = pd.read_csv(r'H:\ArcGIS\map.osmLINKS.csv')
``` 

2. The script will return a shapefile to the folder specified by the the user with the name also specified by the user. Hence, the user will also have to specify the output folder's path.  
```python
output = r"H:/ArcGIS/map.shp"
```

note: This code may take serveral hours if there are many links in the csv file. A 20mb LINK.csv file takes approximately 15 minutes. 

### FAQ
1. Is there any software that can help me and osm to shapefile conversion ?  
Yes, but the ones that I can find are not free. There is a free ArcGIS open source tool but that requires ArcGIS 10.1 version.

2. Where can I get the requried csv files?
Please refer to the osm_to_csv documentation in this same github repository. 

### Help

Contact: elvinngu@gmail.com
