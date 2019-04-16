import sys
import random

#importing from other folders

sys.path.insert(0, '../INC')
from inc import INC

sys.path.insert(0, '../HOR')
from hor import HOR


sys.path.insert(0, '../Greedy')
from greedy import GRE

sys.path.insert(0, '../BFPE')




K= 4
U= ['u0', 'u1', 'u2', 'u3', 'u4', 'u5', 'u6']
E= ['e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6']
T= ['t0', 't1', 't2', 't3', 't4']
L= ['loc0', 'loc1', 'loc2', 'loc3', 'loc4', 'loc5', 'loc6']
Sigma= [[0.4, 0.9, 0.7, 0.9, 0.9], [0.3, 0.6, 0.2, 0.7, 0.6], [0.0, 0.5, 0.4, 0.3, 1.0], [0.5, 0.4, 0.0, 0.8, 1.0], [1.0, 0.8, 0.5, 0.6, 0.3], [0.9, 0.3, 0.3, 0.2, 0.8], [0.4, 0.3, 0.5, 0.1, 0.5]]
mu_E= [[0.5, 0.1, 0.3, 0.2, 0.8, 0.6, 0.1], [0.4, 0.3, 0.2, 0.4, 0.8, 0.4, 0.4], [0.5, 1.0, 0.9, 1.0, 0.7, 0.8, 0.2], [0.5, 1.0, 0.8, 0.5, 0.7, 0.8, 0.9], [1.0, 0.5, 0.9, 0.7, 0.7, 0.4, 0.5], [0.2, 0.7, 0.9, 0.6, 0.4, 0.8, 0.5], [0.6, 0.3, 0.1, 0.6, 0.0, 0.5, 0.9]]
mu_C= [[0.8, 0.0, 0.2, 0.8, 0.0], [0.7, 0.2, 0.3, 0.1, 0.7], [0.1, 0.6, 0.7, 0.7, 0.1], [0.7, 0.3, 1.0, 0.2, 0.3], [0.1, 0.1, 0.0, 0.4, 0.6], [0.6, 0.7, 0.9, 0.5, 0.1], [1.0, 0.7, 0.3, 0.9, 0.6]]






gre_object = GRE(U, E , T , L ,Sigma,mu_E,mu_C)
gre_object.greedy_alg(K)