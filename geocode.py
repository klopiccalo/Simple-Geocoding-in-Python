from geopy import geocoders
from geopy import distance
import time
import csv
import pprint


def main():
    
    count = 0
    g = geocoders.GoogleV3()
    
    coordinates = []
    
  
    
    addresses = []
    
           
    for address in addresses:
        place, (lat, lng) = g.geocode(address)
        #This pauses between addresses, so as not to overload Google's API
        time.sleep(1)

        x = "%.5f %.5f" % (lat, lng)
        #This counter tests that the address went through OK, 
        #Sometimes there are mistakes in the format, and the code
        #barks at you, so you need a good way to figure out which one it was
        #Although, there might be a more parsimonious solution
        count = count + 1
        print count, "OK"
        
        x.strip
        coordinates.append(x)
        
    print(' ' + ' '"\n".join(coordinates) + '')
  
        
        
if __name__=="__main__":
    main()

 