### Functions used in COVID Drivers project notebooks

import numpy as np
import pandas as pd
import os

import altair as alt

# Define path to raw data
path_raw = 'data/raw/'

# Create enumeration dictionary
enum_df = pd.read_excel('data/aux/enumeration_dictionary.xlsx')
enum_cols = enum_df.COLUMN.unique().tolist()
enum_dict = {}
for c in enum_cols:
    enum = enum_df.loc[enum_df['COLUMN']==c]
    tmp_dict = dict(zip(enum['VALUE'], enum['CONTENT'].str.strip()))
    enum_dict[c] = tmp_dict

# Define lists for storing file specifications
years = []
filepaths = []
filesizes = []
ncols = []
nrows = []

"""
Read the data using the path_in variable value 
and the folder, year, and dataset name (dsname) parameter values.

Append file specifications, including the year, full path,
file size in megabytes, number of rows, and number of columns
to global variable lists.
"""
def read_data(folder, year, dsname):
    global years
    global filepaths
    global filesizes
    global ncols
    global nrows

    filepath = path_raw + folder + '/' + dsname + '_' + year + '.csv'
    years.append(year)
    filepaths.append(path_raw + folder + '/' + dsname + '_' + year + '.csv')
    filesizes.append(round(os.path.getsize(filepath)/(1024 * 1024),2))
    tmp = pd.read_csv(filepath, low_memory = False)
    ncols.append(tmp.shape[1])
    nrows.append(tmp.shape[0])

    return tmp

def try_convert_series(df, c):
    """
    Attempts to convert a Pandas series to int, then float, then
    string, otherwise to an object.
    Handles potential issues like 'Int64' type for NaNs if needed,
    but this simpler version uses standard Python types.
    """
    try:
        # Try converting to integer
        df[c] = df[c].astype('int64')
        return df
    except (ValueError, TypeError):
        try:
            # If int fails, try converting to float
            df[c] = df[c].astype('float64')
            return df
        except (ValueError, TypeError):
            try:
                # If float fails, try converting to string
                df[c] = df[c].astype('string')
                return df
            except (ValueError, TypeError):
                # If all fail, convert to object
                #df[c] = [np.nan if str(x) in ['nan', '<NA>', ''] else x for x in df[c]]
                df[c] = df[c].astype('object')
                return df

def create_data_dict(df, enum_dict=None):

    dtypes = []
    nuniqs = []
    ranges = []
    misses = []
    enums = []

    df_cols = list(set(df.columns.tolist()))

    for c in df_cols:

        miss = df[c].isna().sum()

        miss_pct = round((miss/df.shape[0])*100,2)

        nuniq = df[c].nunique()

        uniq_ = df[c].unique().tolist()
        uniq = ['<NA>' if str(x)=='nan' else str(x) for x in uniq_]

        df2 = try_convert_series(df, c).copy()
        dtyp = df2[c].dtype.name

        # Append value to respective list
        dtypes.append(dtyp)
        nuniqs.append(nuniq)

        if dtyp in ['string', 'object'] and nuniq <= 15:
            ranges.append(', '.join(uniq))
        elif dtyp in ['string', 'object'] and nuniq > 15:
            ranges.append('; '.join(uniq[0:10]) + ';...')
        elif dtyp in ['int64', 'float64']:
            ranges.append('[' + str(df2[c].min()) + ', ' + str(df2[c].max()) + ']')
        else:
            ranges.append('None')
        misses.append(str(miss) + ' (' + str(miss_pct) + '%)')

        if enum_dict != None:
            if c in enum_dict:
                enums.append(enum_dict[c])
            else:
                enums.append(None)

    dd = pd.DataFrame({'Column':df_cols,
                       'Data Type':dtypes,
                       'Number of Unique':nuniqs,
                       'Missing':misses,
                       'Range/Unique':ranges,
                       'Enumeration':enums})

    return dd.sort_values(['Column']).copy()

"""
Create a line chart using Altair given the DataFrame (df)
and the horizontal (_x) and vertical (_y) columns.
"""
def line_chart(df, _x, _y):
    var_ = _y.replace('_', ' ').title()

    chart = alt.Chart(df).mark_line(point=True).encode( 
        x= _x, 
        y=_y
    ).properties(
        title=var_ + ' Over Time'
    )

    return chart

"""
Summarize the variable c of DataFrame (df) using groupby variables 
in grp_list and aggregate function in agg_func.
"""
def summarize(df, grp_list, c, key='CRN', agg_func='mean'):
    tmp = df.groupby(grp_list).\
        aggregate(summ_val=(c,agg_func)).\
        reset_index().\
        rename(columns={'summ_val':c + '_' + agg_func}).\
        copy()
    return tmp.loc[:,[c + '_' + agg_func]].copy()

"""
Summarize the variable c of DataFrame (df) using groupby variables 
in grp_list. Count the total number of crashes to use in
calculating the rate of indicator and flag variables.
"""
"""def summarize(df, grp_list, c, key='CRN', total='TOTAL_CRASHES', agg_func='sum'):
    tmp = df.groupby(grp_list).\
        aggregate(summ_val=(c,agg_func),
              TOTAL_CRASHES=(key,'count')).\
        reset_index().\
        rename(columns={'summ_val':c + '_' + agg_func}).\
        copy()
    if agg_func=='sum':
        tmp[c + '_rate'] = tmp[c + '_'+agg_func]/tmp[total]
        return tmp.loc[:,[c + '_rate']].copy()
    else:
        return tmp.loc[:,[c + '_' + agg_func]].copy()
"""