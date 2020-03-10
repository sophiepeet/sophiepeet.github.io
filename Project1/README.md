This is a project description markdown.
This project was created to find out where there is correlation between number of prisons and number of people incarcerated in the United
States. This project was created using QGIS3.10.

## **Vector Analysis**
- For the United States, state layer rendering there was data collected from prisonpolicy.org, on the number of people incarcerated
per state. This data was added to the attribute table, creating a new field, and using this to categorize the data, in a simple cloropleth
map layer.

- I retrieved a prison shapefile layer USGS ScienceBase, with all of the prison locations/areas in the United States. I then used the
centroid tool (Vector-Geometry tools) to create points for each of the prison polygons. 

## **Raster Analysis**
I used the centroid points from the previous vector conversion and used the Kernel Density Tool with a radius of 10 to create a heatmap
for the point layer, as a better representation spatially. I chose a Purple to Yellow "Virids" color scheme for this top the grays I used
for the chloropeth layer. I chose a transparency of 70% for this layer so you are able to draw conclusions by making connections between 
the two layers.
