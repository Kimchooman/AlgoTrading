class simulated_portfolio:

	def __init__(self):  #Defining object attributes.
		self.capital = 10000
		self.comission = 10
		self.current_hold = None
		self.pos_size = 0
		self.rtn = 0

	def buy(self, current_price):  #Calculating if suffient funds exist, then calculating position size
		if current_price < self.capital:
			self.pos_size = self.capital // current_price
			self.current_hold = current_price

		else:
			print("insuffient funds")

	def sell(self, sell_price): #Calculate return, then reseting positions to zero.
		self.rtn += ((self.current_hold - sell_price) * self.pos_size)
		self.current_hold = None
		self.pos_size = 0

	def calculated_returns(self): #Factoring in commision to final returns.
		net_outcome = (self.rtn - self.comission)

		return net_outcome

