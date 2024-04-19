import pandas as pd
import numpy as np
import pickle
class Well_solver:
    def __init__(self,name,papka_with_models='wellmodels/'):
        self.papka_with_models = papka_with_models
        self.name = name
        path=self.papka_with_models+'norm.pickle'

        with open(path, "rb") as file:
          self.normalizer = pickle.load(file)
        well_name=self.name
        if self.name =='"896Б"':
          well_name='_896Б_'
        if self.name =='896Б':
          well_name='_896Б_'
        path=self.papka_with_models+'wellmodel_'+well_name+'.pickle'
        with open(path, "rb") as file:
          self.model = pickle.load(file)
    #data is 'Дебит жидкости', 'Газовый фактор', 'Буферное давление','Обводненность'

    def predict(self,data):
        
        data=np.asarray(data)
        data=data.reshape(1,-1)
        
        data = self.normalizer.transform(data)
        
        
        davlenie = self.model.predict(data)
        return davlenie[0]
