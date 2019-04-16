from class_ses import SES
from HOR_I_Template import HOR_I
from HOR_I_Template import result
U = ['u1','u2']
S = []
A = []
E = ['e1','e2','e3','e4']
T = ['t1','t2']
location = ['Stage 1', 'Stage 1', 'Stage 2', 'Room A']

sigma = [[0.8, 0.5],[0.5, 0.7]]
mu_E = [[0.9, 0.3, 0, 0.6],[0.2, 0.6, 0.1, 0.6]]
mu_C = [[0.8, 0.3],[0.4, 0.7]]


hor_object = HOR_I(3, U, E , T , location ,sigma,mu_E,mu_C)

#hor_object.generate_assignment()
#hor_object.status_log()
#hor_object.status_log(hor_object.L_i[0])
#hor_object.status_log(hor_object.L_i[1])

hor_object.hor_algorithm()
#result(hor_object)         #just for verfying the final Schedule
#hor_object.status_log()
#hor_object.status_log(hor_object.S)


