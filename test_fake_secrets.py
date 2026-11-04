# Synthetic test file for the secret scan workflow.
# Every value below is fake. Commit this to a personal test repo only.
# The workflow should fail with 7 or more findings.
 
from arcgis.gis import GIS
import arcpy
 
gis = GIS("https://gis.example.gov/portal")
