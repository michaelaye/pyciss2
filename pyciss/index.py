# AUTOGENERATED! DO NOT EDIT! File to edit: 05_index.ipynb (unless otherwise specified).

__all__ = ['get_index_dir', 'resonances', 'download_general_index', 'download_ring_summary_index',
           'read_cumulative_iss_index', 'ring_summary_index', 'read_ring_images_index', 'get_clearnacs_ring_images',
           'filter_for_ringspan', 'get_resonances_inside_radius', 'check_for_resonance', 'check_for_janus_resonance',
           'get_janus_phase']

# Cell
from pathlib import Path

import numpy as np
import pandas as pd

from planetarypy.pdstools.indexes import indexdb

from .ringutils import which_epi_janus_resonance, get_all_prime_resonances
from .io import config

# Cell
resonances = get_all_prime_resonances()

def get_index_dir():
    d = Path(config.archive_path) / "indexes"
    d.mkdir(exist_ok=True)
    return d

# Cell
def download_general_index():
    indexdb.download("cassini.iss.index")

# Cell
def download_ring_summary_index():
    indexdb.download("cassini.iss.ring_summary")

# Cell
def read_cumulative_iss_index():
    "Read in the whole cumulative index and return dataframe."
    index = indexdb.get("cassini.iss.index")

    df = index.df
    # replace PDS Nan values (-1e32) with real NaNs
    df = df.replace(-1.000000e32, np.nan)
    return df.replace(-999.0, np.nan)

# Cell
def ring_summary_index():
    index = indexdb.get('cassini.iss.ring_summary')

    df = index.df
    df = df.replace(-1.00000e32, np.nan)
    return df.replace(-999.0, np.nan)

# Cell
def read_ring_images_index():
    """Filter cumulative index for ring images.

    This is done by matching the column TARGET_DESC to contain the string 'ring'

    Returns
    -------
    pandas.DataFrame
        data table containing only meta-data for ring images
    """
    meta = read_cumulative_iss_index()
    ringfilter = meta.TARGET_DESC.str.contains("ring", case=False)
    return meta[ringfilter]

# Cell
def get_clearnacs_ring_images():
    df = read_ring_images_index()
    try:
        df = df.set_index("isotime")
    except KeyError:
        print("'isotime' column does not exist. Leaving index as it is.")
    ringimages = df.query("RINGS_FLAG=='YES'")
    ringimages = ringimages[ringimages.MAXIMUM_RING_RADIUS.notnull()]
    ringimages = ringimages[ringimages.MINIMUM_RING_RADIUS.notnull()]
    ringimages = ringimages.query(
        "MAXIMUM_RING_RADIUS < 1e90 and MINIMUM_RING_RADIUS > 0"
    )
    nac = ringimages[ringimages.INSTRUMENT_ID == "ISSNA"]
    clearnacs = nac.query('FILTER_NAME_1 == "CL1" and FILTER_NAME_2 == "CL2"')
    return clearnacs

# Cell
def filter_for_ringspan(clearnacs, spanlimit):
    "filter for covered ringspan, giver in km."
    delta = clearnacs.MAXIMUM_RING_RADIUS - clearnacs.MINIMUM_RING_RADIUS
    f = delta < spanlimit
    ringspan = clearnacs[f].copy()
    return ringspan

# Cell
def get_resonances_inside_radius(row):
    minrad = row["MINIMUM_RING_RADIUS"]
    maxrad = row["MAXIMUM_RING_RADIUS"]
    lower_filter = resonances["radius"] > (minrad)
    higher_filter = resonances["radius"] < (maxrad)
    insides = resonances[lower_filter & higher_filter]
    return insides


def check_for_resonance(row, as_bool=True):
    insides = get_resonances_inside_radius(row)
    return bool(len(insides)) if as_bool else len(insides)


def check_for_janus_resonance(row, as_bool=True):
    insides = get_resonances_inside_radius(row)
    # row.name is the index of the row, which is a time!
    janus = which_epi_janus_resonance("janus", row.name)
    moonfilter = insides.moon == janus
    return bool(len(insides[moonfilter]))


def get_janus_phase(time):
    return which_epi_janus_resonance("janus", time)