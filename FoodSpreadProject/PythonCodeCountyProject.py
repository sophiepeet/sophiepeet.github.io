#Python Code Chunks for a project using Food Store POINT layers, and County 
#Polygon layers
#Sophie Peet

#Clip Points to Individual County (Clip Vector Layers)
import processing #import processing toolbox
inpath3 = "C:/GES486/Project2/AllSmallGroceryCornerStores.shp" #input path, layer you want to clip
clippath3 = "C:/GES486/Project2/IndividualCounties/Moco.shp" #path for feature you want to clip TO
outpath3 = "C:/GES486/Project2/IndividualCounties/SGCSMOCO.shp"#path where output is saved
processing.run("native:clip", {'INPUT':inpath3, ' OVERLAY':clippath3, 'OUTPUT':outpath3})
iface.addVectorLayer(outpath3, '', 'ogr') #add layer to map

#Count Points in Individual County(COunt Points in Polygon)
import processing #import processing toolbox
Count4 = "C:/GES486/Project2/IndividualCounties/StoreCountMoCo.shp" #output path
polypath4 = "C:/GES486/Project2/IndividualCounties/CountAllFoodMoCo.shp" #polygon path you are counting points in
pointpath4 = "C:/GES486/Project2/IndividualCounties/PMMOCO.shp"#points to be counted
processing.run("native:countpointsinpolygon",{'CLASSFIELD':'', 'FIELD':'numPubMark', 'OUTPUT':Count4, 
'POINTS':pointpath4, 'POLYGONS':polypath4, 'WEIGHT' : '' } )
iface.addVectorLayer(Count4,'','ogr') #add new polygon layer with new count fields in attribute table

#Select By Expression(Select Vector Layer)
from qgis.core import QgsProject 
layer = QgsProject.instance().mapLayersByName("countycounts_new")[0] #choose layer to select from
iface.setActiveLayer(layer) #set this as your active layer
layer.selectByExpression('"COUNTY"=\'Howard\'',QgsVectorLayer.SetSelection) #use expression to select from active layer

#Save Shapefile to Permanent File and Add to Map
#same code as lines 22-25
from qgis.core import QgsProject

layer = QgsProject.instance().mapLayersByName("countycounts_new")[0]
iface.setActiveLayer(layer)
layer.selectByExpression('"COUNTY"=\'Howard\'',QgsVectorLayer.SetSelection)
layer = iface.activeLayer()
new_layer = layer.materialize(QgsFeatureRequest().setFilterFids(layer.selectedFeatureIds()))
QgsProject.instance().addMapLayer(new_layer)

#save to file 
save_options = QgsVectorFileWriter.SaveVectorOptions() #set saving options as variable
save_options.driverName = "ESRI Shapefile" #file type
save_options.fileEncoding = "UTF-8" #file encoding
transform_context = QgsProject.instance().transformContext()
error = QgsVectorFileWriter.writeAsVectorFormatV2(layer,"C:/GES486/Project2/IndividualCounties/HowardCo.shp",
transform_context,save_options) #path to save file
#print whether there was an error saving your new shapefile
if error[0] == QgsVectorFileWriter.NoError:
    print("success")
else:
  print(error)
#set file path as variable, and show on mine
hoco = "C:/GES486/Project2/IndividualCounties/HowardCo.shp"
iface.addVectorLayer(hoco,'','ogr')


#all code adapted from "open source options(youtube)" and "qgis python cheat sheet"
