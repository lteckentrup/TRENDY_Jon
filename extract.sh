# Read CSV file with site locations
mapfile -t site_lat_lon < ../sitelocations.csv

# Split each line of CSV into site name, lat, lon
for line in "${site_lat_lon[@]}"; do
    site=$(echo $line | cut -d, -f1)
    lat=$(echo $line | cut -d, -f2 | bc)
    lon=$(echo $line | cut -d, -f3 | bc)
    
    # Extract coords
    echo ${site}
    echo ${lat}
    echo ${lon}
    cdo -L -b F64 -selvar,evapo -remapnn,lon=${lon}_lat=${lat} \
        CABLE-POP_S3_evapo.nc evapo/CABLE-POP_S3_${site}.nc
done
