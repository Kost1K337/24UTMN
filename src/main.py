from ima.model import Solver

shema = {
    0: {'d_j':[], 'm_j':[2], 'p': 1, 'q' : 1, 'name': '105'},
    1: {'d_j':[], 'm_j':[2], 'p' : 1, 'q' : 1, 'name': '1075'},
    2: {'d_j':[0,1], 'm_j':[3], 'p' : 1, 'q' : 0},
    3: {'d_j':[2,4], 'm_j':[5], 'p' : 1, 'q' : 0},
    4: {'d_j':[], 'm_j':[3], 'p' : 1, 'q' : 1, 'name': '1087'},
    5: {'d_j':[4], 'm_j':[], 'p' : 1, 'q' : 0}
}

solver = Solver(shema, 20, '01.01.2023')
solver.solv()