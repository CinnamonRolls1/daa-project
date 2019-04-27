import time
import sys
sys.path.insert(0, '../INC')
from inc import INC

sys.path.insert(0, '../HOR')
from hor import HOR

sys.path.insert(0, '../HOR_I')
from hor_i import HOR_I

sys.path.insert(0, '../Greedy')
from greedy import GRE

sys.path.insert(0, '../BFPE')

def measureGRE(K,U, E , T , L ,Sigma,mu_E,mu_C) :


	gre_object = GRE(U, E , T , L ,Sigma,mu_E,mu_C)
	t1 = time.time()
	gre_object.greedy_alg(K)
	t2 = time.time()

	dt = t2-t1

	return dt

def measureINC(K,U, E , T , L ,Sigma,mu_E,mu_C) :

	inc_object = INC(K,U, E , T , L ,Sigma,mu_E,mu_C)
	inc_object.generate_assignment()
	t1 = time.time()
	inc_object.INC_algo()
	t2 = time.time()

	dt = t2-t1

	return dt


def measureHOR(K,U, E , T , L ,Sigma,mu_E,mu_C) :
	hor_object = HOR(K,U, E , T , L ,Sigma,mu_E,mu_C)
	t1 = time.time()
	hor_object.hor_algorithm()
	t2 = time.time()

	dt = t2-t1

	return dt


def measureHOR_I(K,U, E , T , L ,Sigma,mu_E,mu_C) :
	hor_i_object = HOR_I(K,U, E , T , L ,Sigma,mu_E,mu_C)
	t1 = time.time()
	hor_i_object.hor_i__algo()
	t2 = time.time()

	dt = t2-t1

	return dt