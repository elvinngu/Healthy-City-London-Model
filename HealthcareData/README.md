# CQC_API

CQC_API is a script for obtaining all information regarding healthcare and social care organisations stored by the Care Quality Commission (CQC). The script will return a csv file containing information for each care organisation in the whole of United Kingdom (complete and accurate with respect to the Care Quality Commission's database). 

### How the script works

1. When the script is run (no inputs required), the function will retrieve all location IDs of all organisations in CQC's database using an [API provided by CQC](https://anypoint.mulesoft.com/exchange/portals/care-quality-commission-5/4d36bd23-127d-4acf-8903-ba292ea615d4/cqc-syndication-1/). The format of data is in json and passed into a list of IDs.

2. For each location ID in the list, a request is made to retrieve more information regarding that specific care organisation. The current code obtains the following information for each of the location:  
(i) Name  
(ii) Type of organisation  
(iii) Postal code  
(iv) Constituency    
(v) Location ID  
(vi) Location (Latitude and Longtitude)  
(vii) Overall ratings (click [here](https://www.nhs.uk/Scorecard/Pages/IndicatorFacts.aspx?MetricId=8175) for ratings description)  
(viii) Registration Status   
(ix) Inspection Directorate (Primary Medical Care, Hospital, Social Care, Mental Care etc.)  
(x) gacServicesType  

Note: if the user wants more information details, the user can refer to the relevant json file and edit the code accordingly. Refer for [CQC API](https://anypoint.mulesoft.com/exchange/portals/care-quality-commission-5/4d36bd23-127d-4acf-8903-ba292ea615d4/cqc-syndication-1/) for documentation.

3. The function returns a csv file with all the data retrieved (approx. 90,000 as of July 2019). Due the large amount of data and the need to parse through 90,000 json files, the process of running the script may take up to 10 hours. If internet speed is slow, time taken may significantly increase.

### How to use?
Open the script and press run. 

Alternatively, you can download the July 2019 csv file with 90,000 healthcare organistion's data from the same github folder. 

### Limitations

The code may take up to 10 hours to run to retrieve all 90,000 data points in CQC's database (this is true as of July 2019).

### Help
Contact: elvinngu@gmail.com
