
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.preprocessing import PolynomialFeatures
import os
import pickle
import shutil


class plast():
  def __init__(self, date, well, press_zab):
    self.well = well
    self.date = date
    self.press_zab = press_zab

    if self.well == '"896Б"':
      self.well = '_896Б_'

    with open(f"models/{self.well}", "rb") as file:
      self.loaded_models = pickle.load(file)


  def predict(self):
    date_sec = datetime.strptime(self.date, "%d.%m.%Y").timestamp()
    np_arr = np.array(date_sec)
    poly = PolynomialFeatures(degree=3, include_bias=False)
    poly_features = poly.fit_transform(np_arr.reshape(-1, 1))
    predict = self.loaded_models.predict(poly_features)
    # print(predict)
    pressure_plast = predict[0][0]
    coef = predict[0][1]

    return self.Q(coef, pressure_plast)

  def Q(self, coef, pressure_plast):
    Q = -coef*self.press_zab+pressure_plast

    return Q
