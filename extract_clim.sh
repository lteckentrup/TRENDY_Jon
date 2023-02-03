# Read CSV file with site locations
mapfile -t site_lat_lon < ../sitelocations.csv

# Set var from command line argument
var_cru=$1

# Set var from command line argument
var_DGVM=$2

# Aggregation method
var_agg=$3

# Split each line of CSV into site name, lat, lon
# Ignore first line (column names)

for line in "${site_lat_lon[@]:1}"; do
    site=$(echo $line | cut -d, -f1)
    lat=$(echo $line | cut -d, -f2 | bc)
    lon=$(echo $line | cut -d, -f3 | bc)
    
    ### Can set to 32 to speed up
    seq 1980 2018 | xargs -n 1 -I {} -P 8 bash -c \
        "year={}; cdo -L -b F64 -chunit,'mm/6h','kg/m^2/s' -chname,${var_cru},${var_DGVM} -mon${var_agg} \
            -divc,86400 -daysum -selvar,${var_cru} -remapnn,lon=${lon}_lat=${lat} \
            ../../CRUJRA/${var_cru}/crujra.v2.0.5d.${var_cru}.\${year}.365d.noc.nc \
            ${var_DGVM}/CRUJRA_S3_${site}_\${year}.nc"
done

cdo -L -b F64 -mergetime ${var_DGVM}/*${site}* ${var_DGVM}/CRUJRA_S3_${site}.nc

for line in "${site_lat_lon[@]:1}"; do
    rm ${var_DGVM}/*_${site}_*
