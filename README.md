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
squarewidths = 1000 #the maximum width of one square
type_ = 'restaurant'
parsePlaces3(centre_lat,centre_long,width,type_,squarewidths)
```

## Limitations




## License
[MIT](https://choosealicense.com/licenses/mit/)
