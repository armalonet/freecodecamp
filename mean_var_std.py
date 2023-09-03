import numpy as np


def calculate(list):
   
   if len(list) != 9:
       try:
           print("List is not complete")
       except ValueError:
           print("List must contain nine numbers.")   
    
   c = np.array([list]).reshape(3, 3)
       
   calculations = ({
      'mean': [c.mean(axis = 0), c.mean(axis = 1), c.mean()],
      'variance': [c.var(axis = 0), c.var(axis = 1), c.var()],
      'standard deviation': [c.var(axis = 0) , c.var(axis = 1), c.var()],
      'max': [c.max(axis = 0), c.max(axis = 1), c.max()],
      'min': [c.min(axis = 0), c.min(axis = 1), c.min()],
      'sum': [c.sum(axis = 0), c.sum(axis = 1), c.sum()]
    })


   return calculations
