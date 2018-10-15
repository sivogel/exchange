import wget
from netCDF4 import Dataset

fileName = 'chess_pet_wwg_196101.nc'
protectedURL = 'https://password:test:user:test@catalogue.ceh.ac.uk/datastore/eidchub/8baf805d-39ce-4dac-b224-c926ada353b7/'
wget.download(protectedURL + 'pet/' + fileName)

root = Dataset("chess_pet_wwg_196101.nc", "w", format="NETCDF4")
print(root.data_model)

#do stuff here
root.close()
