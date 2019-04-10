import requests
import json

class data_center:

	def __init__(self,ticker): #Defining json url, and using %s for dynamic inputs.
		self.ticker = ticker
		self.url = 'https://api.iextrading.com/1.0/stock/%s/chart/5y'
		self.data = self.download_data()

	def download_data(self): #Getting Raw data, subclasses included.
		my_url = self.url %(self.ticker)
		response = requests.get(my_url)
		data = json.loads(response.text)

		return data

	def view_data(self, key): #Viewing individual data sets.
		rtn = []
		for daily in self.data:
			rtn.append(daily[key])

		return rtn
