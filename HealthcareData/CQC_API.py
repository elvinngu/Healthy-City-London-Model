import requests
import os
import pandas as pd



url = 'https://api.cqc.org.uk/public/v1/locations?page=1&perPage=100000&partnerCode=ImperialStudent'
response = requests.get(url=url)
response_locations = response.json()
results = []

for re in response_locations['locations']:
    url = 'https://api.cqc.org.uk/public/v1/locations/{}?partnerCode=ImperialStudent'.format(re['locationId'])
    response2 = requests.get(url=url)
    response_details = response2.json()
    
    
    result = []
    try:
        result.append(response_details['name'])
    except:
        result.append('no name')
    try:
        result.append(response_details['type'])
    except:
        result.append('no type')
    try:
        result.append(response_details['brandId'])
    except:
        result.append('no brandId')
    try:
        result.append(response_details['odsCode'])
    except:
        result.append('no odsCode')
    try:
        result.append(response_details['postalCode'])
    except:
        result.append('no postalCode')
    try:
        result.append(response_details['constituency'])
    except:
        result.append('no constituency')
    try:
        result.append(response_details['locationId'])
    except:
        result.append('no locationId')
    try:
        result.append(response_details['onspdLatitude'])
    except:
        result.append('no latitude')
    try:
        result.append(response_details['onspdLongitude'])
    except:
        result.append('no longitude')
    try:
        result.append(response_details['localAuthority'])
    except:
        result.append('no localAuthority')
    try:
        result.append(response_details['currentRatings']['overall']['rating'])
    except:
        result.append('no ratings')
    try:
        result.append(response_details['registrationStatus'])
    except:
        result.append('unspecified')
    try:
        result.append(response_details['inspectionDirectorate'])
    except:
        result.append('unspecified')
    try:
        result.append(response_details["gacServiceTypes"][0]['name'])
    except:
        result.append('unspecified')
    results.append(result)
    

    
    
DATA_DIR=os.path.join(os.getcwd())
with open(os.path.join(DATA_DIR, "CQCdata.csv"),"w",newline="",encoding="utf-8") as df:
    results = pd.DataFrame(results,columns = ['Name','Type','brandId','odsCode','postalCode','constituency','locationId','latitude','longtitude','localAuthority','ratings','Registration Status','InspectionDirectorate','gacServiceTypes' ])
    results.to_csv(df)
