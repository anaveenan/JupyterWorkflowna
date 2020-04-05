import os
from urllib.request import urlretrieve
import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
def get_fremont_data(filename='Fremont.csv',url=FREMONT_URL,forceDownload=False):
    """
    Parameters
    __________
    filename:string(optional)
        location to save the data
    url:string(optional)
        weblocation of the data
    forceDownload:bool(optional)
        if True,force redownload data
    Returns
    _______
    data: pandas.DataFrame
    Fremont bridge dataset

    """
    if forceDownload or not os.path.exists(filename):
        urlretrieve(FREMONT_URL,'Fremont.csv')

    data=pd.read_csv('Fremont.csv',index_col='Date',parse_dates=True).drop(['Fremont Bridge Total'],axis=1)
    data.columns=['East','West']
    data=data.assign(Total=lambda x:x['East']+x['West'])
    
    return data
