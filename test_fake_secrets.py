# Synthetic test file for the secret scan workflow.
# Every value below is fake. Commit this to a personal test repo only.
# The workflow should fail with 7 or more findings.
 
from arcgis.gis import GIS
import arcpy
 
gis = GIS("https://gis.example.gov/portal", "svc_user", "Summer2026!")
gis2 = GIS(url="https://www.arcgis.com", username="me", password="Hunter22")
arcpy.SignInToPortal("https://gis.example.gov/portal", "svc_user", "Winter2026")
API_KEY = "AAPK1a2b3c4d5e6f7g8h9i0jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"
url = "https://gis.example.gov/server/rest/services/x/FeatureServer/0/query?where=1=1&token=abcDEF123456ghiJKL789012mnoPQR345678"
client_secret = "0123456789abcdef0123"