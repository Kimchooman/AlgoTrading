import talib

#Durig and after the development of new strategies,
#this class will be a full object that contains
#funcions that return buy and sell requests based on 
#the given time-series data

class algo_center:
	
	def __init__(self):
		_ = None
			
	def bare_mr(self,data):
		rsi = talib.RSI(data, timeperiod=14)

		if rsi[-1] >= 70:
			return False
		elif rsi[-1] <= 30:
			return True
