import pandas as pd
import numpy as np
import pickle
import shutil
import os


class Well_solver:
    def __init__(self,name,papka_with_models='wellmodels/',archive_path='wellmodels.zip'):
        self.papka_with_models = papka_with_models
        self.name = name
        self.archive_path=archive_path

        well_name=self.name
        path = self.papka_with_models+'wellmodel_'+well_name+'.pickle'
        check_file = os.path.isfile(path)
        if not check_file:
          path=self.papka_with_models+'wellmodel_'+well_name+'.pickle'
          shutil.unpack_archive(self.archive_path,'wellmodels', 'zip')

        


        path=self.papka_with_models+'norm.pickle'

        

        with open(path, "rb") as file:
          self.normalizer = pickle.load(file)
        
        # if self.name =='"896Б"':
        #   well_name='_896Б_'
        # if self.name =='896Б':
        #   well_name='_896Б_'

  

        
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
