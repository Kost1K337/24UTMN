import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle
import os

class plast_predict_IPR():
  def __init__(self, date, well, Pzab):
    self.well = well
    self.date = date
    self.Pzab = Pzab

    with open (f"models/{self.well}", 'rb') as model:
      self.models = pickle.load(model)
    
  def predict(self):
    pred_date = np.array(datetime.strptime(self.date, "%d.%m.%Y").timestamp()).reshape(-1,1)
    pred = models_list[self.well].predict(pred_date)
    Pplast = pred[0][0]
    kro = pred[0][1]
    return self.make_IPR(Pplast, kro)

  def make_IPR(self, kro, Pplast):
    make_IPR = -kro*self.Pzab+Pplast
    return make_IPR
