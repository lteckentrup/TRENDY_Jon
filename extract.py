import xarray as xr
import pandas as pd
import argparse

### Pass DGVM and var as argument from command line
parser = argparse.ArgumentParser()
parser.add_argument('--DGVM', type=str, required=True)
parser.add_argument('--var', type=str, required=True)
args = parser.parse_args()

### Read CSV with site names, lat and lon
df_sites = pd.read_csv('sitelocations.csv')

def grab_site_data(DGVM,var):
    ### Read in file
    fileIN = DGVM+'_S3_'+var+'.nc
    ds = xr.open_dataset(fileIN)
    encoding = {'time': {'dtype': 'double'},
                'latitude': {'dtype': 'double'},
                'longitude': {'dtype': 'double'},
                var: {'dtype': 'float32'}}

    ### Loop through all sites and write to separate netCDF
    for site,lat,lon in zip(df_sites.Site,df_sites.latitude,df_sites.longitude):
        ds_site = ds.sel(latitude=lat,longitude=lon,method='nearest')
        fileOUT = var+'/'DGVM+'_S3_'+var+'.nc'
            
        ds_site.to_netcdf(fileOUT, encoding = encoding)

### Grab data
grab_site_data(args.DGVM,args.var)
