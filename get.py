import wget
from netCDF4 import Dataset

username = 'simone.vogel%40student.uni-tuebingen.de' 
password = '%2FDenker94'
fileName = 'chess_pet_wwg_196101.nc'
protectedURL = 'https://' + username + ':' + password + '@catalogue.ceh.ac.uk/datastore/eidchub/8baf805d-39ce-4dac-b224-c926ada353b7/pet/' + fileName
print(protectedURL)
wget.download(protectedURL)

root = Dataset("chess_pet_wwg_196101.nc", "w", format="NETCDF4")
print('\n')
print(root.data_model)

#do stuff here
root.close()
