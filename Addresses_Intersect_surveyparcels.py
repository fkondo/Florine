import arcpy

print "start"
#variables
x = arcpy.GetParameterAsText(0)
y = arcpy.GetParameterAsText(1)

sde_connection = r"C:\Users\kondof\AppData\Roaming\ESRI\Desktop10.3\ArcCatalog\1kondof MERCATOR2 @ 10.252.50.113.sde"
default_gdb_connection = r"C:\Users\kondof\Documents\ArcGIS\Default.gdb"
spatial_ref_location = r"C:\Users\kondof\AppData\Roaming\ESRI\Desktop10.3\ArcMap\Coordinate Systems\NAD 1983 UTM Zone 12N.prj"

arcpy.env.workspace = default_gdb_connection#sde_connection
arcpy.env.overwriteOutput=True # to overwrite feature classes if they already exist. 

#need to add arcpy.parameterastext for point xy input

#----Section 1: Reads Input ----##


point_test = arcpy.Point(x, y) #x,y variables go here
ptGeometry = arcpy.PointGeometry(point_test)

#create point featureclass
arcpy.CopyFeatures_management(ptGeometry, "point3")

# Make a layer from the survey feature class
survey_parcels=sde_connection + r"\MERCATOR2.DBO.CADASTRAL_REFERENCE\MERCATOR2.DBO.SURVEY_PARCELS"
arcpy.MakeFeatureLayer_management(survey_parcels,"survey_parcels_lyr")


#select survey parcels that intersect point
arcpy.SelectLayerByLocation_management('survey_parcels_lyr', 'intersect', 'point3')

#create survey parcel feature class from the selection
arcpy.CopyFeatures_management('survey_parcels_lyr', 'Select_Parcel2')

#create a featureset
feature_set = arcpy.FeatureSet('Select_Parcel2')

print "end"
