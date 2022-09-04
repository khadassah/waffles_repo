import iris
# to store multi dimensional data called cubes
import glob as glob
# to find all pathnames matching .nc
import esmvalcore.preprocessor as pp
# to perform cube operations in the script in a centralized and efficient way
# import extract_shape

import warnings

warnings.filterwarnings('ignore')

nino_cube = iris.load('/work/bd1083/b381616/Causal_6months/SPI/ERA/ERA5.cvdp_data.1979-2014.nc', 'nino34')
print(nino_cube)
pp.save(nino_cube, "/work/bd1083/b381616/Causal_6months/SPI/ERA/Result/" + "nino_SPI_cube.nc")

spi_global = iris.load_cube('/work/bd1083/b381616/Causal_6months/SPI/ERA/native6_ERA5_reanaly_v1_Amon_spi_1979-2014.nc')
#print(spi_global)

# monkey patch preprocessors
pp._area.SHAPE_ID_KEYS = ('Acronym', 'id')
print(pp._area.SHAPE_ID_KEYS)
spi_global = pp._shared.guess_bounds(spi_global, ["latitude", "longitude"])
shape_file = "/work/bd1083/b381616/Causal_6months/SPI/ERA/ar6_regions/IPCC-WGI-reference-regions-v4.shp"

#reg_list

#reg_list = ['GIC', 'NWN', 'NEN', 'WNA', 'CNA', 'ENA', 'NCA', 'SCA',
#            'NWS', 'NSA', 'NES', 'SAM', 'SWS', 'SES', 'SSA', 'NEU',
#            'WCE', 'EEU', 'MED', 'SAH', 'WAF', 'CAF', 'NEAF', 'SEAF',
#            'WSAF', 'ESAF', 'MDG', 'WSB', 'ESB', 'RFE', 'WCA', 'ECA',
#            'TIB', 'EAS', 'ARP', 'SAS', 'SEA', 'NAU', 'CAU', 'EAU',
#            'SAU', 'NZ', 'EAN', 'WAN', 'ARO']

reg_list = ['GIC', 'NWN', 'WNA', 'CNA', 'ENA', 'SAU',
            'NWS', 'NSA', 'NES', 'SES', 'SSA', 'NEU',
            'WCE', 'EEU', 'MED', 'SAH', 'WAF', 'CAF',
            'MDG', 'WSB', 'ESB', 'RFE', 'WCA', 'ECA',
            'EAS', 'SAS', 'SEA', 'NAU', 'CAU', 'EAU']

#reg_list = ['GIC', 'EAS', 'NSA', 'NAU', 'NES', 'SES', 'EAS',
#            'SEA', 'CAU', 'EAU', 'SAU', 'SAS']
            
#reg_list = ['ENA', 'SES', 'SAS', 'SAU', 'EAU', 'SEA', 'ECA']

for regstr in reg_list:
    try:
       regcube = pp.extract_shape(spi_global, shape_file, ids = [regstr])
    except ValueError:
       print("WARNING, non working region excluded")
       print(regstr)
       continue
    print(regcube.shape)
    regcube = regcube.collapsed(['latitude', 'longitude'], iris.analysis.MEAN)
    print(regcube.shape)
    pp.save([regcube], "/work/bd1083/b381616/Causal_6months/SPI/ERA/Result/" + regstr + "_cube.nc")
