import sys
import random

#importing from other folders

sys.path.insert(0, '../INC')
from inc import INC

sys.path.insert(0, '../HOR')
from hor import HOR


sys.path.insert(0, '../Greedy')
from greedy import GRE

sys.path.insert(0,'../HOR_I')
from HOR_I_Template import HOR_I

sys.path.insert(0, '../BFPE')



'''
K=3
U = ['u1','u2']
S = []
A = []
E = ['e1','e2','e3','e4']
T = ['t1','t2']
L = ['Stage 1', 'Stage 1', 'Stage 2', 'Room A']

Sigma = [[0.8, 0.5],[0.5, 0.7]]
mu_E = [[0.9, 0.3, 0, 0.6],[0.2, 0.6, 0.1, 0.6]]
mu_C = [[0.8, 0.3],[0.4, 0.7]]
'''
'''
K=3
U= ['u0', 'u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9', 'u10', 'u11']
E= ['e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11']
T= ['t0', 't1', 't2', 't3', 't4', 't5']
L= ['loc0', 'loc1', 'loc2', 'loc3', 'loc4', 'loc5', 'loc6', 'loc7', 'loc8', 'loc9', 'loc10', 'loc11']
Sigma= [[0.7, 0.8, 0.8, 0.6, 0.7, 0.5], [0.4, 0.5, 0.7, 0.5, 0.1, 0.2], [1.0, 0.3, 0.2, 0.6, 0.1, 0.8], [0.8, 0.3, 0.9, 0.2, 0.7, 0.1], [0.9, 0.4, 0.2, 0.6, 0.3, 0.3], [0.9, 0.9, 0.4, 0.8, 0.4, 0.2], [0.8, 0.8, 0.3, 0.6, 0.2, 0.7], [0.8, 0.6, 0.9, 0.6, 0.8, 1.0], [0.2, 0.3, 0.1, 0.4, 0.5, 0.5], [0.5, 0.3, 0.3, 0.2, 0.4, 0.5], [0.2, 0.8, 0.4, 0.5, 0.2, 0.7], [0.1, 0.4, 0.2, 0.9, 0.6, 0.6]]
mu_E= [[1.0, 0.4, 0.1, 0.5, 0.8, 0.6, 0.4, 0.1, 0.8, 0.2, 0.6, 0.5], [0.2, 0.7, 0.5, 0.9, 0.8, 0.2, 0.2, 0.2, 0.1, 0.1, 0.6, 0.9], [0.1, 0.8, 0.1, 0.6, 0.8, 0.6, 0.3, 0.2, 0.5, 0.7, 0.8, 0.8], [0.2, 0.1, 0.6, 0.5, 0.8, 0.8, 0.2, 0.8, 0.3, 1.0, 0.4, 0.9], [0.3, 0.4, 0.5, 0.1, 0.9, 0.2, 0.2, 0.8, 0.7, 0.3, 0.1, 0.5], [0.9, 0.9, 0.8, 0.2, 0.3, 0.8, 0.8, 0.9, 0.9, 0.2, 1.0, 0.9], [1.0, 0.2, 0.8, 0.4, 0.4, 0.4, 0.7, 0.2, 0.4, 0.5, 0.9, 0.5], [0.5, 0.2, 1.0, 0.2, 0.7, 0.8, 0.8, 0.3, 0.8, 0.3, 0.3, 0.6], [0.8, 0.5, 0.5, 0.6, 0.2, 0.9, 0.8, 0.6, 0.9, 0.7, 0.5, 0.7], [0.4, 0.9, 0.3, 0.4, 0.6, 0.7, 0.6, 0.3, 0.5, 0.2, 0.9, 0.4], [0.7, 0.3, 0.7, 0.4, 0.9, 0.8, 0.6, 1.0, 0.5, 0.5, 1.0, 0.4], [0.8, 0.4, 0.3, 0.7, 0.8, 1.0, 1.0, 0.4, 0.7, 1.0, 0.2, 0.5]]
mu_C= [[0.7, 0.2, 0.4, 0.4, 0.7, 0.2], [0.1, 0.4, 0.7, 0.3, 0.5, 0.8], [0.6, 0.1, 0.2, 0.6, 0.5, 0.4], [0.8, 0.5, 0.6, 0.1, 1.0, 0.2], [0.1, 0.3, 0.8, 0.6, 0.9, 0.8], [0.6, 1.0, 0.7, 0.5, 0.8, 0.1], [0.4, 0.7, 0.2, 0.7, 0.9, 0.3], [0.3, 0.6, 0.7, 0.3, 0.5, 0.1], [0.9, 0.3, 0.2, 0.7, 0.6, 0.8], [1.0, 0.4, 0.9, 0.8, 0.2, 0.6], [0.4, 0.9, 0.8, 0.2, 0.8, 0.4], [0.5, 0.7, 0.9, 0.8, 0.1, 0.5]]
'''









gre_object = GRE(U, E , T , L ,Sigma,mu_E,mu_C)
gre_object.greedy_alg(K)

inc_object = INC(K,U, E , T , L ,Sigma,mu_E,mu_C)
inc_object.generate_assignment()
inc_object.INC_algo()


hor_object = HOR(K,U, E , T , L ,Sigma,mu_E,mu_C)
hor_object.hor_algorithm()

hor_i_object = HOR_I(K,U, E , T , L ,Sigma,mu_E,mu_C)
hor_i_object.hor_i__algo()



print("\n\n\n")
print("_________GREEDY ALGORITHM___________")
gre_object.status_log(gre_object.S)
print("\n_________INCREMENTAL UPDATE ALGORITHM___________")
inc_object.status_log(inc_object.S)
print("\n_________HORIZONTAL UPDATE ALGORITHM___________")
hor_object.status_log(hor_object.S)
print("\n_________HORIZONTAL INCREMENTAL UPDATE ALGORITHM___________")
hor_i_object.status_log(hor_i_object.S)