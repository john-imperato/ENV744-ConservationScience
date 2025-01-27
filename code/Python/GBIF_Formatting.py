# set paths 
GBIF_file = r"C:\Conservation Science\Fish\LCT\GBIF_occurrence\0000681-250127130748423.csv"
table = r"C:\Conservation Science\Project Proposal\Default.gdb\LCT_GBIF"
fc = r"C:\Conservation Science\Project Proposal\Default.gdb\LCT_Occurrence_GBIF"

arcpy.env.overwriteOutput = True

# create standalone table from GBIF .csv download
arcpy.management.CopyRows(GBIF_file, table)

# make point feature class from XY coordinates in table
arcpy.management.XYTableToPoint(in_table = table,
                               out_feature_class = fc,
                               x_field = "decimalLongitude",
                               y_field = "decimalLatitude",
                               coordinate_system = arcpy.SpatialReference(4326))
