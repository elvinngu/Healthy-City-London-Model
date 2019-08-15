# BUILDING SERVICE AREA NETWORK ANALYST

A service area analysis layer is useful in determining the area of accessibility within a given cutoff cost from a facility location (ESRI, 2016). In this case, the facility location is the location of each household. This code is designed in such a way that all data points within the polygon layer centered at each household will be selected and recorded in respective arrays. The final execution of the code is to create a data frame whereby all of the mean value of the attributes will be calculated and recorded in the data frame. After running the code sucessfully, user should be able to gather information regarding the desired data points with respect to the household for every household point in the area.

*Note that this code runs only in the ArcGIS python window.

### How the function works
1) Set FID to desired range of numbers
2) Edit Line 7 to Line 13 accordingly to make service area layer. Note that the inNetworkDataset must be built before executing the MakeServiceAreaLayer command.
3) Create empty variables for desired attributes
4) Create loop function which makes service area layer for the household with respect to the FID. During each loop, a polygon will be drawn and data points within the polygon will be selected layer by layer. Data will be appended to respective numpy arrays.
5) A data frame is created to record the mean value of each attributes with respect to the household. It is then saved as a csv file.

### Editing the code
The code creates the polygon with a 15 minutes walk boundary. This can be varied according to your needs as below. For detailed documentation on how to utilise the 'MakeServiceAreaLayer' function, visit http://desktop.arcgis.com/en/arcmap/10.3/tools/network-analyst-toolbox/make-service-area-layer.htm

Example:
```python
import arcpy
from arcpy import env
import pandas as pd
FID=range(601,801,1)
env.workspace=r'\\icnas1.cc.ic.ac.uk\jyl17\ArcGIS'
env.overwriteOutput=True
inNetworkDataset=r'\\icnas1.cc.ic.ac.uk\jyl17\ArcGIS\Useful\WalkingMinutes.ND'
outNALayerName='BarkingandDagenhamAnalysis'
impedanceAttribute='Minutes'
outNALayer=arcpy.na.MakeServiceAreaLayer(inNetworkDataset,outNALayerName,impedanceAttribute,"TRAVEL_FROM",'15',"SIMPLE_POLYS")
outNALayer=outNALayer.getOutput(0)
sublayerNames=arcpy.na.GetNAClassNames(outNALayer)
```
As aformentioned, the inNetworkDataset must be built before executing this code. For this case, the desired attribute is the time taken in minutes to walk on the specific road. If the desired attribute is seconds, the network dataset should be built in a way that the impedance attribute is seconds. If the 'Seconds' column is not in the shapefile which is then to be used to build the network dataset, user should add a field to the table of the shapefile and use field calculator to calculate the time taken in seconds to travel on the specific path. The number '15' in line 28 limits the area to be a 15-minutes-walk area.

Reminder:
Before executing the code, ensure arcgis is in Edit mode. This can be enabled through selecting 'Customize' then 'Toolbars' then 'Editor'. The reason being the code will run a lot faster if executed in edit mode. 

Limitations:
Even though I have tried to reduce the cost of the code as much as possible, the runtime is still significantly long to produce a service area layer for all the households in one borough. For instance, for Barking and Dagenham with 1057 household points, it took 13 hours to collect all of the data. 
For future reference, I would suggest that, if possible, the center of each ward can be used as the facility location instead of the household, the coordinates of the full postcode would be preferred as well. However, this is restricted by the purpose of the user running the analysis. 

### Help
Contact jyl17@ic.ac.uk (Jia Yong LIM) 
