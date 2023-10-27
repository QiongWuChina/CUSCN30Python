# Qiong Wu@20221126
import arcpy
import os
from arcpy import env
from arcpy.sa import *

# Please enter the path of the unzipped dataset.zip, i.e. E:/CurveNumber/dataset
env.workspace = "Enter your path of the unzipped dataset.zip here"

arcpy.CheckOutExtension("Spatial")
outworkspace = os.path.dirname(env.workspace) + "/ARCI"
if not os.path.exists(outworkspace):
    os.makedirs(outworkspace)
    print("Create folder: {outworkspace}")
else:
    print("Folder already exists: {outworkspace}")

raster_list = arcpy.ListRasters("*","tif")
print (raster_list)

# Save the output
for CNraster in raster_list:
    print (CNraster)
    Outraster = outworkspace + "/" + CNraster
    print (Outraster)
    rasterout = Raster(CNraster) - (20 * (100 - Raster(CNraster)) /(100 - Raster(CNraster) + Exp(0.0636 * (100 - Raster(CNraster)))))
    rasterout.save(Outraster)

print("Done")
