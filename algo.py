import numpy as np
from data_center import *

class algo_center:

  def __init__(self):
    
    self.buy_hold = False
    self.sell = False
    self.complete_trans_ar = [] 
    self.current_hold = None
    self.net_returns = 0
    
    self.commision = 5
    self.tax = .87
    
    self.session = True                 #running is true
    
  def buy(self, current_price):
    self.current_hold = current_price
      
  def sell(self, sell_price):
    self.complete_trans_ar.append([self.current_hold,sell_price])
    self.current_hold = None
    
  def calculated_returns(self):
    returns = 0
    
    for trans in self.complete_trans_ar:
      purchase = trans[0]
      sell = trans[1]
      returns += sell - purchase
      
   self.net_returns = (returns - self.commision) * self.tax 
   
   return self.net_returns
      
      
