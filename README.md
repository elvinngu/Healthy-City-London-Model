# parsePlaces

parsePlaces is a function for obtaining places of interest from the google placesx API. This function overcomes the limits of google API where only a maximum of 60 results is returned when using google places API.

## How it works

[Google places API](https://developers.google.com/places/web-service/intro) allows the retrieval of 60 results from a circle of %x radius with centre (x-coordinate,y-coordinate). 

This function loops google places API as many time as it needs to get unlimited results within a square area. 

## Usage

```python
apiKey = "xxxxxxxxxxxxxxxxxxxxxxxx"

# the following three inputs will determine the area of search:
centre_lat = 51.495227 # centre of square
centre_long = -0.138546 
width = 3000 # width of square

innerwidth = 1000 #the maximum width of one inner square (read 'How it works' section for more information)
type_ = 'restaurant' 

parsePlaces3(centre_lat,centre_long,width,type_,squarewidths)
```

## Usage Recommendations



## Limitations

Every page requests (20 results) from google API is delayed by 2 seconds. Hence, to obtain many results may take a long time

Due to the overlapping area of cirlces as seen in figure 1, some results may duplicate. This causes some inefficiencies within the search process but it is unavoidable. 

The function do not automatically select the most suitable innerwidth to start with. The innerwidth input is chosen intuitively and the most optimal innerwidth is 

