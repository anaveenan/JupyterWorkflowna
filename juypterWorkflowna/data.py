import os
from urllib.request import urlretrieve
import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
def get_fremont_data(filename='Fremont.csv',url=FREMONT_URL,forceDownload=False):
    """
    Author : Naveenan Arjunan
    Parameters
    __________
    filename:string(optional)
        location to save the data
    url:string(optional)
        weblocation of the data
    forceDownload:bool(optional)
        if True,force redownload data
    Returns
    __________
    data: pandas.DataFrame
    Fremont bridge dataset

    """
    if forceDownload or not os.path.exists(filename):
        urlretrieve(FREMONT_URL,'Fremont.csv')

    #data=pd.read_csv('Fremont.csv',index_col='Date',parse_dates=True)

    data=pd.read_csv('Fremont.csv',index_col='Date').drop(['Fremont Bridge Total'],axis=1)
    try:
        data.index=pd.to_datetime(data.index,format='%m/%d/%Y %I:%S:%M %p')
    except TypeError:
        data.index=pd.to_datetime(data.index)


    data.columns=['East','West']
    data=data.assign(Total=lambda x:x['East']+x['West'])
    
    return data
