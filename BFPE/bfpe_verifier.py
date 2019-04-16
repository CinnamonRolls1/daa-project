import sys
import random
import pandas as pd
import os

#importing from other folders

sys.path.insert(0, '../INC')
from inc import INC

sys.path.insert(0, '../HOR')
from hor import HOR


sys.path.insert(0, '../Greedy')
from greedy import GRE

sys.path.insert(0, '../BFPE')

def generator(n):

	u=0
	e=0
	t=0
	l=0

	K=0
	U=[]
	E=[]
	T=[]
	L=[]
	sigma=[[]]
	mu_E=[[]]
	mu_C=[[]]
	
	ui=0
	ei=0
	ti=0
	li=0
	f=0
	fnames=[]
	while e<=n:

		u+=random.randint(1,4) #u should preferably grow fastest
		
		e_inc=random.randint(1,3)
		e+=e_inc
		
		t+=random.randint(1,e_inc) #t should preferably grow slower than e
		
		l+=e_inc #l should grow at the same rate as e
		
		K+=random.randint(1,e_inc) #k should always be less than e

		for i in range(ui,u):
			U.append('u'+str(i))
		ui=u
		
		for i in range(ei,e):
			E.append('e'+str(i))
		ei=e
		for i in range(ti,t):
			T.append('t'+str(i))
		ti=t
		for i in range(li,l):
			L.append('loc'+str(i))
		li=l


		for k in range(len(sigma)):
			for i in range(len(sigma[k]),len(T)):
				sigma[k].append(round(random.uniform(0,1),1))

		for k in range(len(mu_C)):
			for i in range(len(mu_C[k]),len(T)):
				mu_C[k].append(round(random.uniform(0,1),1)) 

		for k in range(len(mu_E)):
			for i in range(len(mu_E[k]),len(E)):
				mu_E[k].append(round(random.uniform(0,1),1))
				

		for i in range(len(sigma),len(U)):
			sigma.append([round(random.uniform(0,1),1) for k in range(len(T))])

		for i in range(len(mu_C),len(U)):
			mu_C.append([round(random.uniform(0,1),1) for k in range(len(T))])

		for i in range(len(mu_E),len(U)):
			mu_E.append([round(random.uniform(0,1),1) for k in range(len(E))])
		


		print("K:",K)
		print("U:",U)
		print("E:",E)
		print("T:",T)
		print("L:",L)
		print("Sigma:", sigma)
		print("mu_E:", mu_E)
		print("mu_C:", mu_C)

		inputs={
			"K:":K,
			"U:":U,
			"E:":E,
			"T:":T,
			"L:":L,
			"Sigma:": sigma,
			"mu_E:": mu_E,
			"mu_C:": mu_C
		}
		sampler=pd.DataFrame({key:pd.Series(value) for key, value in inputs.items()})
		while os.path.exists("inputs_%s.csv" % f):
		 		f+=1
		fname="inputs_"+str(f)+".csv"
		sampler.T.to_csv(fname)
		fnames.append(fname)


		#gre_object = GRE(U, E , T , L ,sigma,mu_E,mu_C)

		#inc_object.generate_assignment()
		#gre_object.greedy_alg(K)
		print("---------------------------------------------------------")
		
	print("Files written: ")
	for name in fnames:
		print(name, end=' ')
	
		




if __name__ == '__main__':
	generator(int(input("Enter maximum number of events: ")))


