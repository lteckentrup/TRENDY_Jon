import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse

### Pass DGVM and var as argument from command line
parser = argparse.ArgumentParser()
parser.add_argument('--DGVM', type=str, required=True)
parser.add_argument('--var', type=str, required=True)
args = parser.parse_args()

def site_plot(var,DGVM):
    # directory containing the netcdf files
    path = DGVM+'/'+var

    # list of all netcdf files in the directory
    files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.nc')]

    # sort files
    files = sorted(files)

    # loop over each file and plot the timeseries of the variable
    for i, file in enumerate(files):
        ds = xr.open_dataset(file,decode_times=False)
        title = file.split("/")[-1].split("_")[-1].split(".")[0]

        if np.isnan(ds[var].values.flatten()).all() == True:
            print(title)
        else:
            pass

site_plot(args.var,args.DGVM)
