#--------Libraries--------#
from  numpy import *
from pandas import *
#--------coding-----------# 
ClassicCars = Series({'2003':1484785.29,'2004':1762257.09,'2005':675273.28})
Motorcycles = Series({'2003':370895.58,'2004':560545.23,'2005':234947.53})
Planes = Series({'2003':272257.60,'2004':502671.80,'2005':200074.17})
Ships = Series({'2003':244821.09,'2004':341437.97,'2005':128178.07})
Trains = Series({'2003':72802.29,'2004':116523.85,'2005':36917.33})
TruckandBuses = Series({'2003':420429.93,'2004':529302.89,'2005':178057.02})
VintageCars = Series({'2003':650987.76,'2004':911423.77,'2005':340739.31})

df = DataFrame({'ClassicCars':ClassicCars,'Motorcycles':Motorcycles,
                'Planes':Planes,'Ships':Ships,
            'Trains':Trains,'Truck and Buses':TruckandBuses,
            'Vintage Cars':VintageCars})

df.plot(kind='bar')
print(df)
print('Finish...')
print('---------------------------')



