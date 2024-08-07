"""
Functions to import package data.

Most of the data files included in stroke-maps are useful
in many other places, so these functions provide a quick way
to get at the data.
"""
import pandas as pd
from importlib_resources import files


# #########################
# ##### REGION LOOKUP #####
# #########################

def stroke_unit_region_lookup():
    """
    Import data linking stroke units to geographical regions.
    """
    # Relative import from package files:
    path_to_file = files('stroke_maps.data').joinpath(
        'stroke_units_regions.csv')
    df = pd.read_csv(path_to_file)
    return df


def lsoa_region_lookup():
    """
    Import data linking LSOA to geographical regions.

    This file contains only LSOA to SICBL (England) and LHB (Wales).
    To link those to other regions, import the region lookup file
    using the function region_lookup().
    """
    # Relative import from package files:
    path_to_file = files('stroke_maps.data').joinpath(
        'regions_lsoa_ew.csv')
    df = pd.read_csv(path_to_file)
    return df


def region_lookup():
    """
    Import data linking geographical regions.

    The index is a multiindex of region (SICBL/LHB) name and code.
    """
    # Relative import from package files:
    path_to_file = files('stroke_maps.data').joinpath(
        'regions_ew.csv', index_col=[0, 1])
    df = pd.read_csv(path_to_file)
    return df


# ########################
# ##### TRAVEL TIMES #####
# ########################

def travel_time_matrix_lsoa():
    """
    Import travel time matrix for each LSOA to each stroke unit.

    Each column is a postcode of a stroke team and
    each row is an LSOA name (LSOA11NM).
    """
    # Relative import from package files:
    path_to_file = files('stroke_maps.data').joinpath(
        'lsoa_travel_time_matrix_calibrated.csv', index_col='LSOA')
    df = pd.read_csv(path_to_file)
    return df


def travel_time_matrix_units():
    """
    Import travel time matrix for each stroke unit to each other.

    Each row index is a postcode of a stroke team and
    each column name is a stroke team.
    """
    # Relative import from package files:
    path_to_file = files('stroke_maps.data').joinpath(
        'inter_hospital_time_calibrated.csv', index_col='from_postcode')
    df = pd.read_csv(path_to_file)
    return df


# #####################
# ##### GEOGRAPHY #####
# #####################

def stroke_unit_coordinates():
    """
    Import stroke unit coordinates.

    Index: postcode.
    Columns: BNG_E, BNG_N, Longitude, Latitude.
    """
    # Relative import from package files:
    path_to_file = files('stroke_maps.data').joinpath(
        'unit_postcodes_coords.csv')
    df = pd.read_csv(path_to_file, index_col='postcode')
    return df

# TO DO - disentangle the geojson import and provide a function here. --------------------------------------------------
