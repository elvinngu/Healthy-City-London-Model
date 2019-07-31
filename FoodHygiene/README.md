# Scraping Food Hygiene Ratings(FHRS) from Food Standard Agency

This code is **only for *London*!** This code scrapes food hygiene ratings for all business types, including hotels, retailers, restaurants and etc with respect to the borough the business is located at. London is divided into 33 boroughs(technically 32 boroughs and 1 city). Along with the FHRS, we can also obtain details with respect to the business, notably the **Business Name, Business Type, Business Type ID, Address, Geocode(Latitude,Longitude).** In the context of our tasks, we are only interested in the aforementioned attributes of the business. 

### Limitations

The url doesn't seem to have a pattern if the user requires data from other counties. Hence, the only way to tackle this is to visit the website https://ratings.food.gov.uk/open-data/en-GB, then click on the county or borough that the user is interested in, copy the url and paste it to the code.

### How it works
### 1) Collecting the Complete Set of Data

Unlike Google Places API, there is no limit to how many results that can be retrieved at any instance. The code will repeat the scrape for each borough and results for all businesses in all 33 boroughs should be collected.  

The endpoint url is http://ratings.food.gov.uk/OpenDataFiles/. Adding FHRS501en-GB.xml will allow user to scrape fhrs data for the first borough (boroughs are arranged in alphabetical orders), hence, Barking and Dagenham. The code will replace '01' with numbers from '01' to '33' for each loop and thus, collecting all of the data for all boroughs.

```python
fhrsurl ="http://ratings.food.gov.uk/OpenDataFiles/FHRS5%xen-GB.xml"
a=list(range(1,34))
b = ["%02d" % n for n in a]
results=[]


for i in b:
    url = fhrsurl.replace("%x",str(i))
    response= requests.get(url)
    response.encoding= 'utf-8'
    JsonD = json.dumps(response.text)
    JsonL = json.loads(JsonD)
    mydict = xmltodict.parse(JsonL)
    a = list(list(mydict.items()))[0][1]['EstablishmentCollection']['EstablishmentDetail']
```

### 2) Collecting Certain Attributes of the Business

Moving forward from the data scraped above, user can now collect specific attributes of the business using the following lines of codes. The example below shows how to collect the business name of the business using the try and except function. User can repeat the function as many times as necessary to collect data of different attributes of the business. 

```python
for i in list(range(0,len(a))):
        result = []
        add=[]
         
        try:
            result.append(a[i]['BusinessName'])
        except:
            result.append("No Business Name")
        try:
            result.append(a[i]['BusinessType'])
        except:
            result.append("No Business Type")
```

A thing to note that is when getting the address of a business, user must consider different cases to collect the full address of the business. There are four address line for a certain business, however not all business has four lines of address, they may have one, two or three lines instead. Hence, the following code is designed such a way that the full address of a business can be collected.

```python
        try:
            AL1=(a[i]["AddressLine1"])
        except:
            AL1=''
        if AL1 is not '':
            AL1=AL1+','
            
        try:
            AL2=(a[i]["AddressLine2"])
        except:
            AL2=''
        if AL2 is not '':
            AL2=AL2+','
            
        try:
            AL3=(a[i]["AddressLine3"])
        except:
            AL3=''
        if AL3 is not '':
            AL3=AL3+','
            
        try:
            AL4=(a[i]["AddressLine4"])
        except:
            AL4=''
        if AL4 is not '':
            AL4=AL4+','
            
        add=AL1+AL2+AL3+AL4
        add=add[:-1]
        result.append(add)    
        results.append(result)
```
After the completion of each attribute collection, the data should be appended to the list 'result'. Before the loop restarts, the result should be appended to another list, for example 'full results'. Result should return to an empty list before the start of each loop, and Full results should contain all of the data for each result in each loop.

### 3) Writing the data into a CSV file

For the ease of retrieving as well as visualising the data, user can write the data of the full results into a csv file using the last few lines of the code. This is an optional step, subject to what the user needs the data to be saved in.

### Help 
Contact: jia.lim17@imperial.ac.uk