# General Matching Hygiene Ratings Data and Google Places Data

This code is to match restaurants in both datasets and create a new dataset that contains the necessary attributes of a restaurant, as well as the google ratings and hygiene ratings.

### Limitations

User might notice that the geocode, address as well as the business name are different when comparing the data collected using FHRS API and Google Places API. This introduced a problem when matching the two datasets.

On the other hand, due to Google Places limitations, user might need to collect restaurant data in a borough with different coordinates, resulting in more than one file of a restaurant data collected sing Google Places API. The following code is to concatenate all results into one dataframe for the convenience of matching the two datasets.

```python
dfh1=pd.read_csv('Your first Google ratings results of the region.csv')
#dfh2=pd.read_csv('Your second Google ratings results of the region.csv')
#dfh3=pd.read_csv('Your third Google ratings results of the region.csv')
dfh=pd.concat([dfh1,dfh2,dfh3],ignore_index=True)
```

### Tackling the difference in Two data sets

The code is designed in such a way that there are three checks to make sure the restaurant that match in both data sets are accurate. A sequential filter also allows the code to run faster as the data sets are reduced in size after each filter. The first step is to check if the restaurant has the same business address. This will filter out the majority of the restaurants that don't match. However, if the address obtained from Google Places API is generic (usually a one word address, for instance 'Barking'), you might get several results from hygiene data sets that match with the google data sets. 

After the first filter, the code will compute the difference in the latitude and longitude between two data sets and if the difference is more than 0.01, the data is then removed. However, if two restaurants are located in the same coordinates(this will occur if both restaurants are in a shopping mall and one is just above of the other), these two restaurants will still be matched to a single restaurant. 

The final step of the filter is to check if the name is similar in both data sets. This can be done using .split() function to check if one of the element in the name matches the name in the other data set. 

### Help
Contact: jia.lim17@imperial.ac.uk
