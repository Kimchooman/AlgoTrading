import talib

class algo_center:
	
	def __init__(self):

		_ = None
			
	def bare_mr(self,data):

		rsi = talib.RSI(data, timeperiod=14)

		if rsi[-1] >= 70:
			return False

		elif rsi[-1] <= 30:
			return True

	def stationary_ar(self,data):

		n = 0
		rtn = []
		for point in data:

			if point == data[0]:
				pass

			else:
				rtn.append(point-data[n]) 
				n += 1

		return rtn
