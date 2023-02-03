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
    
    # Create subset - sorry to lazy to do this nicely
    subset = files[:36]
    # subset = files[36:72]
    # subset = files[72:108]
    # subset = files[108:144]
    # subset = files[144:180]
    # subset = files[216:252]

    # create a subplot for each variable
    fig, axs = plt.subplots(nrows=6, ncols=6, figsize=(15, 10), squeeze=False)
    axs = axs.flatten()

    # loop over each file and plot the timeseries of the variable
    for i, file in enumerate(subset):
        print(i)
        ds = xr.open_dataset(file)
        var = list(ds.data_vars.keys())[0]
        ds[var].plot(ax=axs[i], label=file)

        title = file.split("/")[-1].split("_")[-1].split(".")[0]
        axs[i].set_title(title)
        axs[i].spines[['right', 'top']].set_visible(False)

        if i not in (30,31,32,33,34,35):
            axs[i].set_xticklabels([])
            axs[i].set_xlabel('')

        axs[i].set_ylabel('')

    yaxes = [0,6,12,18,24,30]

    for i in yaxes:
        axs[i].set_ylabel('NPP [kg m$^{-2}$ s$^{-1}$]')

    plt.tight_layout()
    plt.show()

site_plot(args.var,args.DGVM)
