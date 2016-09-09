# Data-Plotting-on-map
A python program that takes multiple locations from a list as input and plots them on a map

Overview:

This python program takes as input a list of locations. For each location the program creates a request and sends it to the Google Maps API.
The data is retrieved from the API in JSON format. This data is then mined to retrieve the latitude, Longitude and the Name of the location.
This is done for all the locations in the list.
The output is 3 lists for Latitude, Longitude and Name respectively.
These Lists are then passed to the basemap function which will plot the data points on the map along with label for each point.

Steps:

Step 1: Read the file which contains the list of locations

Step 2: For each location, create a request for the API and then send the request to the Google Maps API. 

Step 3: The Data is received in JSON format. So, we can easily work with the data. The data is mined to retrieve only the information regarding Latitude, Longitude and Name.

Step 4: The information is stored in a List. So there are 3 separate lists for latitude, longitude and Name respectively.

Step 5: These Lists are passed to the basemap function which plots the data points on a map.
