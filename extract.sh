# Read CSV file with site locations
mapfile -t site_lat_lon < ../sitelocations.csv

# Set DGVM
DGVM='CABLE-POP'

# Set var
var='evapo'

# Split each line of CSV into site name, lat, lon
# Ignore first line (column names)
for line in "${site_lat_lon[@]:1}"; do
    site=$(echo $line | cut -d, -f1)
    lat=$(echo $line | cut -d, -f2 | bc)
    lon=$(echo $line | cut -d, -f3 | bc)
    
    # Extract coords
    echo ${site}
    echo ${lat}
    echo ${lon}
    cdo -L -b F64 -selvar,${var} -remapnn,lon=${lon}_lat=${lat} \
        ${DGVM}_S3_${var}.nc ${var}/${DGVM}_S3_${site}.nc
done
