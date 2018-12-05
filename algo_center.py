from data_center import *
from portfolio_center import *

class algo_center:

  def __init__(self):
  
    self.timerunning = False
    
    
  def data_hopper(self, data, crrnt_day):
    tmp_ar = data
    future_data = tmp_ar
    prst_pst_data = []
    
    pst_days = range(0,crrnt_day)
    
    for i in future_data:
      if future_data[i] == future_data[pst_days]:
        prst_pst_data.append(future_data[i])
      
      return prst_pst_data
    
  #def runtime(self, running):
