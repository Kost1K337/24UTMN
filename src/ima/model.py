import numpy as np
import sys
# sys.path.append('..\\')
# print(sys.path)
from src.reservoir.model import plast
from src.well.model import Well_solver as well
# !pip install tensorflow
from src.tube.model import SSiTModel as ssit
from src.tube.controller import getPipesList



class Solver():
    def __init__(self, shema, P_sep, date):
        self.Q_sep = np.inf
        self.P_sep = P_sep
#         self.P_plast = P_plast
#         self.wells_dict = wells
        self.shema = shema
        self.shema[len(self.shema) - 1]['p'] = self.P_sep
        self.date = date
#         nodes = (len(self.shema)
#         self.P_nodes = np.zeros((nodes,nodes))
#         self.Q_nodes = np.zeros((nodes,nodes))
        
        self.Eps = 0.01
    
    def solv(self):
        water_cut = 0.75
        exit = 0
        while True:
            #Проходка вперёд
            for i in self.shema:
                if len(self.shema[i]['d_j']) == 0:
                     temple_well = well(self.shema[i]['name'])
                     self.shema[i]['p'] = temple_well.predict([self.shema[i]['q'], self.shema[i]['q']*10, self.shema[i]['p'], water_cut])
                     #дебет жидк, газ факт, давление, обводнёность
            for i in self.shema:
                if len(self.shema[i]['d_j']) == 0:
                     temple_plast = plast(self.date, self.shema[i]['name'], self.shema[i]['p'])
                     self.shema[i]['q'] = temple_plast.predict()
            for i in self.shema:
                if len(self.shema[i]['d_j']) > 0:
                     for j in self.shema[i]['d_j']:
                         self.shema[i]['q'] += self.shema[j]['q']
            #Обратная проходка
            for i in self.shema:
                temple_tube = ssit(getPipesList()[0])
                self.shema[i]['p'] = temple_tube.predict([[self.shema[i]['p'], water_cut, self.shema[i]['q'], self.shema[i]['q']*10]])
                #давление, обводненность, дебит жидкости, газовый фактор

            exit += 1
            if exit > 5:
            # if abs(self.Q_sep - self.shema[len(self.shema)]['q']) < self.Eps:
                return self.shema

            print(self.shema)

            self.Q_sep = self.shema[len(self.shema)-1]['q']
