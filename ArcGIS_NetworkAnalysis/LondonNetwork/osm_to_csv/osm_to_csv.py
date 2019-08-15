import xml.etree.ElementTree as ET
import os
import pandas as pd


def nodesandlinks(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    results = []
    for child in root:
        result=[]
        if child.tag == 'node':
            try:
                result.append(child.get('id'))
            except:
                result.append('no id')
            try:
                result.append(child.get('lat'))
            except:
                result.append('no lat')
            try:
                result.append(child.get('lon'))
            except:
                result.append('no lon')
            n = 0
            for attr in child:
                if attr.get('k') == 'crossing' or attr.get('k') == ' highway' or attr.get('k') == 'traffic_calming':
                    result.append(attr.get('v'))
                    n += 1
            for i in range(0,3-n):
                result.append('none')
            
            results.append(result)
            
    
    DATA_DIR = os.path.join(os.getcwd())
    with open(os.path.join(DATA_DIR, filename + "NODES.csv"),"w",newline="",encoding="utf-8") as df:
            results = pd.DataFrame(results,columns = ['NodeID','Latitude','Longtitude','Crossing','Highway','TrafficCalming'])
            results.to_csv(df)
    
    results = []
    for child in root:
        result=[]
        if child.tag == 'way':
            
            # Checking if it is a highway
            highway = False
            for attr in reversed(child):
                if attr.tag == 'tag':
                    if attr.get('k') == 'highway':
                        highway = True
                        if attr.get('v') == 'cycleway' or attr.get('v') == 'pedestrian' or attr.get('v') == 'footway' or attr.get('v') == 'steps' or attr.get('v') == 'track' or attr.get('v') == 'path':
                            highway = False
                        elif attr.get('v') == 'proposed' or attr.get('v') == 'bridleway' or attr.get('v') == 'elevator' or attr.get('v') == 'corridor' or attr.get('v') == 'escalator':
                            highway = False
                        
                        
            if highway:
            
                
                try:
                    result.append(child.get('id'))
                except:
                    result.append('no id')
                
                n = 0
                # get highway term
                for attr in reversed(child):
                    if attr.tag == 'tag':
                        if attr.get('k') == 'highway':
                            result.append(attr.get('v'))
                            n += 1
                    else:
                        break
                    
                # get highway code
                for attr in reversed(child):
                    if attr.tag == 'tag':
                        if attr.get('k') == 'highway':
                            if attr.get('v') == 'primary' or attr.get('v') == 'primary_link':
                                result.append(2)
                            elif attr.get('v') == 'tertiary' or attr.get('v') == 'tertiary_link':
                                result.append(4)
                            elif attr.get('v') == 'unclassified':
                                result.append(0)
                            elif attr.get('v') == 'residential' or attr.get('v') == 'living_street' or attr.get('v') == 'road':
                                result.append(5)
                            elif attr.get('v') == 'cycleway':
                                result.append(11)
                            elif attr.get('v') == 'pedestrian':
                                result.append(21)
                            elif attr.get('v') == 'footway':
                                result.append(22)
                            elif attr.get('v') == 'steps':
                                result.append(23)
                            elif attr.get('v') == 'track':
                                result.append(24)
                            elif attr.get('v') == 'service':
                                result.append(6)
                            elif attr.get('v') == 'trunk' or attr.get('v') == 'trunk_link':
                                result.append(1)
                            elif attr.get('v') == 'secondary' or attr.get('v') == 'secondary_link':
                                result.append(3)
                            elif attr.get('v') == 'motorway' or attr.get('v') == 'motorway_link':
                                result.append(1)
                            else:
                                result.append(-1)
                            
                
                # get maxspeed term
                for attr in reversed(child):
                    if attr.tag == 'tag':
                        if attr.get('k') == 'maxspeed':
                            string = attr.get('v')
                            try:
                                result.append([int(s) for s in string.split() if s.isdigit()][0])
                            except:
                                try:
                                    number_str = ''
                                    string = [s for s in list(attr.get('v')) if s.isdigit()]
                                    for num in string:
                                        number_str += num
                                    result.append(int(number_str))
                                except:
                                    result.append(0)
                                    print(attr.get('v'))
                            n += 1
                    else:
                        break
                if n == 1:
                    result.append(0)
                    n += 1
                    
                # get sidewalk term
                for attr in reversed(child):
                    if attr.tag == 'tag':
                        if attr.get('k') == 'sidewalk':
                            result.append(1)
                            n += 1
                    else:
                        break
                if n == 2:
                    result.append(0)
                    
                    
                    
                ii = 0
                for attr in child:
                    if attr.tag == 'nd':
                        result.append(attr.get('ref'))
                        ii += 1
                    else:
                        break
                for ii in range(0,300-ii):
                    result.append(0)
                
                results.append(result)
                
    DATA_DIR = os.path.join(os.getcwd())
    with open(os.path.join(DATA_DIR, filename + "LINKS.csv"),"w",newline="",encoding="utf-8") as df:
        columns = ['id','highwaytype','highwaycode','maxspeed','sidewalk']
        for ii in range(0,300):
            columns.append('refnode' + str(ii))
        results = pd.DataFrame(results, columns = columns)
        results.to_csv(df)
        
        
    

        
    


    

if __name__ == "__main__":
    nodesandlinks('london.osm')

                
            
