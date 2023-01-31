#!/bin/bash

### DGVMS available:
# CABLE-POP
# CLASS-CTEM
# CLM5.0_Corrected
# DLEM
# ISAM
# ISBA-CTRIP-UPDATE
# JSBACH
# JULES-ES-1.0
# LPJ-GUESS
# LPX-Bern
# OCN
# ORCHIDEE
# ORCHIDEE-CNP
# SDGVM ! take version 9
# VISIT

### Pass which DGVM
DGVM='CLM5.0_Corrected'

echo $password | sftp hostname@server <<EOF
get /output/${DGVM}/S3/*evapotrans.nc
get /output/${DGVM}/S3/*evapotranspft.nc
get /output/${DGVM}/S3/*transpft.nc
get /output/${DGVM}/S3/*evapo.nc
get /output/${DGVM}/S3/*shflxpft.nc
get /output/${DGVM}/S3/*rnpft.nc
get /output/${DGVM}/S3/*npp.nc
get /output/${DGVM}/S3/*npppft.nc
get /output/${DGVM}/S3/*landCoverFrac.nc
get /output/${DGVM}/S3/*lai.nc
quit
EOF
