from data_center import *
from algo_center import *
from simulated_portfolio import *
import numpy as np
from sys import argv

dc = data_center("AMD") #Change the sting to the required ticker
sp = simulated_portfolio()
ac = algo_center()

data_close = dc.view_data('close')
data_open = dc.view_data('open')
data_high = dc.view_data('high')
data_low = dc.view_data('low')

np_ar_close = np.array(data_close) #Ta-lib functions require numpy arrays.
#np_ar_open = np.array(data_open)  
#np_ar_high = np.array(data_high)  #Minimizing wasteful memory usage
#np_ar_low = np.array(data_low)

last_order = False #If last order is true, then last order was a buy order, inverse for sell.

for day_numb in range(0,len(data_close) - 1): #Altering data stream to prevent unintentional forsight

	if day_numb == 0:
		continue

	if (ac.bare_mr(np_data[0:day_numb]) == True) and (last_order == False): #if algoriths indicates a purchase, make sure you have not already exausted capital into previous purchases.
		sp.buy(data[day_numb])
		last_order = True

	elif (ac.bare_mr(np_data[0:day_numb]) == False) and (last_order == True): #if algoriths indicate a sell, check a previous buy order exists and has not already been sold. 
		sp.sell(data[day_numb])
		last_order = False
