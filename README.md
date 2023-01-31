# TRENDY_Jon

Get site data from TRENDY v8. grab_data.sh is the download script,
extract.sh a bash script to pull individual site locations from netCDF.
extract.py does the same but is written in python.

For example, to get npp per site from CABLE-POP run with bash run

```sh extract.sh CABLE-POP npp```

if python is used then run

``` python extract.py --DGVM 'CABLE-POP' --var 'npp' ``` 
