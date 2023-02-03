import xarray as xr
import argparse

### Pass DGVM and var as argument from command line
parser = argparse.ArgumentParser()
parser.add_argument('--DGVM', type=str, required=True)
parser.add_argument('--var', type=str, required=True)
args = parser.parse_args()

### Compare total NPP with NPP per PFT
def pft_test(DGVM,var):

    try:
        ### Total NPP
        ds_total = xr.open_dataset(DGVM+'/'+var+'/'+DGVM+'_S3_AR-SLu.nc',decode_times=False)

        ### NPP per PFT
        ds_pft = xr.open_dataset(DGVM+'/'+var+'pft/'+DGVM+'_S3_AR-SLu.nc',decode_times=False)

        ### Landcover Fraction
        ds_LCF = xr.open_dataset(DGVM+'/landCoverFrac/'+DGVM+'_S3_AR-SLu.nc',decode_times=False)

        print('Total NPP ='+str(ds_total.npp.values[0].sum()))
        print('Sum over NPP per PFT ='+str(ds_pft.npppft.values[0].flatten().sum()))

        ### CLASS-CTEM and JULES-ES have LCFs that don't match carbon flux PFTs
        if DGVM == 'CLASS-CTEM':
            mul = ds_pft[var+'pft'].values[0] * \
                ds_LCF.landCoverFrac[0][:-1].values
        elif DGVM == 'JULES-ES':
            mul = ds_pft[var+'pft'].values[0] * \
                ds_LCF.landCoverFrac[0][:-4].values
        else:
            mul = ds_pft[var+'pft'].values[0] * \
                ds_LCF.landCoverFrac[0].values
            
        print('Sum over NPP per PFT multiplied with landcover fraction='+str(mul.flatten().sum()))

    except FileNotFoundError:
        print(DGVM+' does not provide '+var+' per PFT')

pft_test(args.DGVM,args.var)
