import requests
import os
import time
import utm
import pandas as pd
import math
import json


DATA_DIR=os.path.join(os.getcwd(),"results")
GOOGLE_URL="https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%x, %y&radius=%d&keyword=%t&key=AIzaSyBsEcSDpfh5mcprCLTUk7eOPW3VoumhBpA"
TOKEN_URL="https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=%t&key=AIzaSyBsEcSDpfh5mcprCLTUk7eOPW3VoumhBpA"


if not os.path.isdir(DATA_DIR):
    os.makedirs(DATA_DIR)

class coordinates_box(object):
    """Initialise a coordinates box class which will hold the produced coordinates"""
    
    def __init__(self):
        self.coordset = []
        self.coordset2 = []
        
        
    def createcoordinates(self, centre_lat, centre_lon, width_m, radius_m,j):
        # Based on the input radius this tesselates a 2D space with circles in
        # a hexagonal structure:
        self.radius = radius_m
        centre_x,centre_y,self.zone_number,self.zone_letter = utm.from_latlon(centre_lat,centre_lon)
        southeast_x = centre_x - width_m/2
        southeast_y = centre_y - width_m/2
        northwest_x = centre_x + width_m/2
        northwest_y = centre_y + width_m/2
    
        x_start = southeast_x
        y_start = southeast_y
        
        y_level = 1
        x = x_start
        y = y_start
        
        while True:
            if (x <= northwest_x + radius_m) & (y <= northwest_y + radius_m):
                self.coordset.append([x,y])
            if y > northwest_y + radius_m:
                break
            elif x > northwest_x + radius_m:
                y_level += 1
                y += radius_m + radius_m *math.sin(math.radians(30))
                if y_level % 2 != 0:
                    x = x_start
                else:
                    x = x_start - radius_m*math.cos(math.radians(30))
            else:
                x += 2 * radius_m*math.cos(math.radians(30))
        
        # convert coordset back to latitude longtitude
        for coords in self.coordset:
            coords[0],coords[1] = utm.to_latlon(coords[0],coords[1],self.zone_number,self.zone_letter)
        
        
        print('InnerSquare %d: parsing with %d circles' % (j,len(self.coordset)))
        
    def createcoordinates2(self, centre_lat, centre_lon, width,squarewidths):
        # Based on the input width, this tesselates a 2D space dividing the space to squares
        # It gives the centre coordinates of the squares within the 2D space
        centre_x2,centre_y2,self.zone_number2,self.zone_letter2 = utm.from_latlon(centre_lat,centre_lon)
        southeast_x2 = centre_x2 - width/2
        southeast_y2 = centre_y2 - width/2
        northwest_x2 = centre_x2 + width/2
        northwest_y2 = centre_y2 + width/2
        
        x_start2 = southeast_x2 + squarewidths/2
        y_start2 = southeast_y2 + squarewidths/2
        
        y_level2 = 1
        x2 = x_start2
        y2 = y_start2
        
        while True:
            if (x2 < northwest_x2 + squarewidths/2) & (y2 < northwest_y2 + squarewidths/2):
                self.coordset2.append([x2,y2])
            if y2 >= northwest_y2 + squarewidths/2:
                break
            elif x2 >= northwest_x2 + squarewidths/2:
                y_level2 += 1
                y2 += squarewidths
                x2 = x_start2
            else:
                x2 += squarewidths
        
        # convert coordset2 back to latitude longtitude
        for coords in self.coordset2:
            coords[0],coords[1] = utm.to_latlon(coords[0],coords[1],self.zone_number2,self.zone_letter2)
            
        print('Searching area of %d km2:\nMain square is divided into %d inner squares to be searched.\n' %(width,len(self.coordset2)))
        
        

        
        
def parsePlaces3(centre_lat,centre_lon,width,type_,squarewidths):
    start = time.time()
    fullresults2 = []
    
    if width > squarewidths:
        
        set2 = coordinates_box()
        set2.createcoordinates2(centre_lat, centre_lon, width,squarewidths)
        
        j = 0
        for coords in set2.coordset2:
            j += 1
            fullresults = parsePlaces2(coords[0],coords[1],squarewidths,type_,j)
            fullresults2.extend(fullresults)
            
        
    else: 
        j = 1
        fullresults2 = parsePlaces2(centre_lat,centre_lon,width,type_,j)
        
    with open(os.path.join(DATA_DIR, type_+str(centre_lat)+str(width)+".csv"),"w",newline="",encoding="utf-8") as df:
        fullresults2 = pd.DataFrame(fullresults2,columns = ['Latitude','Longtitude','Name','Rating','Total User Ratings','Price Level','Address'])
        df.drop_duplicates(inplace=True)
        fullresults2.reset_index(inplace=True)
        fullresults2.drop('index',axis=1,inplace=True)
        fullresults2.to_csv(df)

        
    
    end = time.time()
    print('\nTime taken = %d seconds' %(end-start))
        
    
        
    

def parsePlaces2(lat, long, width, type_,j):
        
        radius = width/2.45
        i = 0
        fullresults=[]
        while True:
            
            # initialise coordinates of points to be parsed
            set1 = coordinates_box()
            set1.createcoordinates(lat,long,width,radius,j)

            
            # run search for all coordinates 
            for coords in set1.coordset:
                api = GooglePlaces(apiKey)
                places = api.search_places_by_coordinate(str(coords[0])+","+str(coords[1]),str(radius),type_)
                fullresults.extend(places)
                
                i += 1
                k = len(places)
                if k == 60:
                    print('Repeat Innersquare %d: results at circle no. %d > 60, try with more circles' %(j,i))
                    radius = radius/1.5
                    i = 0
                    fullresults=[]
                    break
            
            # check if all coords are run
            if i == len(set1.coordset):
                break
          
        return fullresults
    

 
          
class GooglePlaces(object):
    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = apiKey
 
    def search_places_by_coordinate(self, location, radius, types):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'types': types,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        fullresults=[]
        for i in places:
            result=[]
            try:
                result.append(i['geometry']['location']['lat'])
                result.append(i['geometry']['location']['lng'])
            except:
                result.append('no geometry')
            try:
                result.append(i['name'])
            except:
                result.append('no name')
            try:
              result.append(i['rating'])
            except:
              result.append('no rating')
            try:
              result.append(i['user_ratings_total'])
            except:
              result.append('no total user ratings')
            try:
              result.append(i['price_level'])
            except:
              result.append('no price level')
            try:
                result.append(i['vicinity'])
            except:
                result.append('no_vicinity')
                
            fullresults.append(result)

        
        return fullresults
      


if __name__=="__main__":
    apiKey = 'AIzaSyA1RXqm3NDnfq33SRgp9uU4ZzeIKQYhYuY'
    centre_lat = 51.596110
    centre_long = 0.204146
    width = 1000
    squarewidths = 1000 #the maximum width of one square
    type_ = 'restaurant'
    parsePlaces3(centre_lat,centre_long,width,type_,squarewidths)
    
    
