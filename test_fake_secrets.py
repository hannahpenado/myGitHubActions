# Synthetic test file for the secret scan and lint workflow.
# Every value below is fake. Commit this to a personal test repo only.
#
# Lint test: the "lint" job should FAIL with exactly 6 Ruff findings, one per
# line marked "EXPECT" below. Everything in PART 1 is normal ArcPy code that
# ruff.toml is set up to allow, so it should produce no findings.

import os

import arcpy
from arcgis.gis import GIS

gis = GIS("https://gis.example.gov/portal")

# ---------------------------------------------------------------------------
# PART 1: ArcPy patterns that should NOT be flagged
# ---------------------------------------------------------------------------

# Extension checkout before the wildcard import (E402 is ignored).
arcpy.CheckOutExtension("Spatial")
from arcpy.sa import *  # wildcard import is allowed (F403 is ignored)

arcpy.env.workspace = r"C:\GIS\Data\Example.gdb"
arcpy.env.overwriteOutput = True


def steep_areas(dem):
    """Spatial Analyst names come from the builtins list in ruff.toml."""
    slope = Slope(dem, "DEGREE")
    steep = Con(slope > 15, 1, 0)
    steep.save("steep_areas")
    return steep


# ---------------------------------------------------------------------------
# PART 2: real mistakes that SHOULD be flagged
# ---------------------------------------------------------------------------


def buffer_layers(layers, distance, results=[]):  # EXPECT B006: mutable default
    for fc in layers:
        arcpy.analysis.Buffer(fc, fc + "_buf", distance)
        results.append(fc + "_buf")
    return results


def count_rows(fc):
    total = 0
    with arcpy.da.SearchCursor(fc, ["OID@"]) as cursor:
        for _row in cursor:
            total += 1
    return totl  # EXPECT F405: typo, "totl" is not defined


def delete_scratch(path):
    try:  # EXPECT SIM105: try/except/pass can be contextlib.suppress
        arcpy.management.Delete(path)
    except:  # EXPECT E722: bare except hides every error
        pass


def report(fc):
    count = arcpy.management.GetCount(fc)  # EXPECT F841: never used
    if os.path.exists(fc) == True:  # EXPECT E712: compare with "is True" or drop it
        arcpy.AddMessage(fc)
