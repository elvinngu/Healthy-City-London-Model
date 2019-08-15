import arcpy
from arcpy import env
import pandas as pd
FID=range(0,101,1)
env.workspace=r'\\icnas1.cc.ic.ac.uk\jyl17\ArcGIS'
env.overwriteOutput=True
inNetworkDataset=r'\\icnas1.cc.ic.ac.uk\jyl17\ArcGIS\Useful\TQ_RoadLinkWalk_ND.ND'
outNALayerName='BarkingandDagenhamAnalysis'
impedanceAttribute='Minutes'
outNALayer=arcpy.na.MakeServiceAreaLayer(inNetworkDataset,outNALayerName,impedanceAttribute,"TRAVEL_FROM",'15',"SIMPLE_POLYS")
outNALayer=outNALayer.getOutput(0)
sublayerNames=arcpy.na.GetNAClassNames(outNALayer)
facilitiesLayerName=sublayerNames['Facilities']
NumHldMem=[]
NumVeh=[]
HldIncome=[]
PostcodeOut=[]
PostcodeIn=[]
FareZone=[]
resrating=[]
respl=[]
NumRes=[]
librating=[]
NumLib=[]
parkrating=[]
NumPark=[]
schrating=[]
NumSch=[]
hltrating=[]
NumHlt=[]
hygrating=[]
for a in FID:
    whereclause='"FID"={}'.format(a)
    arcpy.Select_analysis('Barking and Dagenham',r'\\icnas1.cc.ic.ac.uk\jyl17\ArcGIS\onehousehold.shp',whereclause)
    inFacilities=r'\\icnas1.cc.ic.ac.uk\jyl17\ArcGIS\onehousehold.shp'
    arcpy.na.AddLocations(outNALayer,facilitiesLayerName,inFacilities,'','','','','',"CLEAR")
    arcpy.na.Solve(outNALayer)
    arr=arcpy.da.TableToNumPyArray('onehousehold',('hresnon','hvehnan','hincome','hhpcout','hhpcin','hhfarezn'))
    NumHldMem.append(float(arr['hresnon']))
    NumVeh.append(float(arr['hvehnan']))
    HldIncome.append(float(arr['hincome']))
    outp=arr['hhpcout'][0]
    inp=arr['hhpcin'][0]
    outp=outp.encode('utf-8')
    inp=inp.encode('utf-8')
    PostcodeOut.append(outp)
    PostcodeIn.append(inp)
    FareZone.append(int(arr['hhfarezn']))
    restaurantsinrange=arcpy.SelectLayerByLocation_management('FullRestaurantData',"WITHIN","BarkingandDagenhamAnalysis\Polygons")
    try:
        arr=arcpy.da.TableToNumPyArray('FullRestaurantData',('RATING','PRICE_LEVE'))
        calrating=0
        calpl=0
        kk=0
        jj=0
        for k in arr['RATING']:
            if k!=0:
                calrating+=k
            else:
                kk+=1
        for j in arr['PRICE_LEVE']:
            if j!=0:
                calpl+=j
            else:
                jj+=1
        calrating=calrating/(len(arr['RATING'])-kk)
        calpl=calpl/float(len(arr['RATING'])-jj)
                   
        resrating.append(calrating)
        respl.append(calpl)
        NumRes.append(len(arr['RATING']))
    except:
        resrating.append('No restaurants available')
        respl.append('No restaurants available')
        NumRes.append('No restaurants available')
    librariesinrange=arcpy.SelectLayerByLocation_management('Libraries',"WITHIN","BarkingandDagenhamAnalysis\Polygons")
    try:
        arr=arcpy.da.TableToNumPyArray('Libraries',('RATING'))
        calrating=0
        kk=0
        for k in arr['RATING']:
            if k!=0:
                calrating+=k
            else:
                kk+=1
        calrating=calrating/(len(arr['RATING'])-kk)           
        librating.append(calrating)
        NumLib.append(len(arr['RATING']))
    except:
        librating.append('No libraries available')
        NumLib.append('No libraries available')
    parksinrange=arcpy.SelectLayerByLocation_management('Parks',"WITHIN","BarkingandDagenhamAnalysis\Polygons")
    try:
        arr=arcpy.da.TableToNumPyArray('Parks',('RATING','PRICE_LEVE'))
        calrating=0
        kk=0
        for k in arr['RATING']:
            if k!=0:
                calrating+=k
            else:
                kk+=1
        calrating=calrating/(len(arr['RATING'])-kk)
        calpl=calpl/(len(arr['RATING'])-jj)
                   
        parkrating.append(calrating)
        NumPark.append(len(arr['RATING']))
    except:
        parkrating.append('No parks available')
        NumPark.append('No parks available')
    schoolssinrange=arcpy.SelectLayerByLocation_management('FullPrimarySchoolData',"WITHIN","BarkingandDagenhamAnalysis\Polygons")
    try:
        arr=arcpy.da.TableToNumPyArray('FullPrimarySchoolData',('Meet_GOV'))
        calrating=0
        kk=0
        for k in arr['Meet_GOV']:
            if k!=0:
                calrating+=k
            else:
                kk+=1
        calrating=calrating/float(len(arr['Meet_GOV'])-kk)
        schrating.append(calrating)
        NumSch.append(len(arr['Meet_GOV']))
    except:
        schrating.append('No primary schools available')
        NumSch.append('No primary schools available')
    healthcareservicesinrange=arcpy.SelectLayerByLocation_management('CQCfulldata',"WITHIN","BarkingandDagenhamAnalysis\Polygons")
    try:
        arr=arcpy.da.TableToNumPyArray('CQCfulldata',('RATING'))
        calrating=0
        kk=0
        for k in arr['RATING']:
            if k!=0:
                calrating+=k
            else:
                kk+=1
        calrating=calrating/float(len(arr['RATING'])-kk)
        hltrating.append(calrating)
        NumHlt.append(len(arr['RATING']))
    except:
        hltrating.append('No healthcare services available')
        NumHlt.append('No healthcare services available')
    restaurantsinrange=arcpy.SelectLayerByLocation_management('HygieneData',"WITHIN","BarkingandDagenhamAnalysis\Polygons")
    try:
        arr=arcpy.da.TableToNumPyArray('HygieneData',('FHRS_RATIN','Business_T'))
        calrating=0
        jj=0
        interest=[7843,7844,1]
        for j in arr['Business_T']:
            if j in interest:
                for k in arr['FHRS_RATIN']:
                    if k!=0:
                        calrating+=k
                        jj+=1
                    else:
                        pass
            else:
                pass
        calrating=calrating/float(jj)                
        hygrating.append(calrating)
    except:
        hygrating.append('No hygiene ratings available')
df=pd.DataFrame()
df['Number of Household Members']=NumHldMem
df['Number of Vehicles Owned']=NumVeh
df['Household Income']=HldIncome
df['Outer Postcode']=PostcodeOut
df['Inner Postcode']=PostcodeIn
df['Fare Zone']=FareZone
df['Number of Restaurants']=NumRes
df['Average Rating of Restaurant']=resrating
df['Average Price Level of Restaurant']=respl
df['Average Hygiene Rating of Restaurant']=hygrating
df['Number of Libraries']=NumLib
df['Average Rating of Library']=librating
df['Number of Parks']=NumPark
df['Average Rating of Parks']=parkrating
df['Number of Primary Schools']=NumSch
df['Average Percentage of Students Meeting the Government Test Standard']=schrating
df['Number of Healthcare Centers']=NumHlt
df['Average Rating of Healthcare Centers']=hltrating
df.to_csv('BarkingandDagenham_1.csv')
