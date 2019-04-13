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


	while e<=n:

		u+=random.randint(1,4) #u should preferably grow fastest
		
		e_inc=random.randint(1,3)
		e+=e_inc
		
		t+=random.randint(1,e_inc) #t should preferably grow slower than e
		
		l+=random.randint(1,e_inc) #l should preferably grow at a pace similar to t
		
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


		#generating sigma
		for k in range(len(sigma)):
			for i in range(len(sigma[k]),len(T)):
				sigma[k].append(round(random.uniform(0,1),1))
				mu_E[k].append(round(random.uniform(0,1),1))
				mu_C[k].append(round(random.uniform(0,1),1)) 
		for i in range(len(sigma),len(U)):
			sigma.append([round(random.uniform(0,1),1) for k in range(len(T))])
			mu_E.append([round(random.uniform(0,1),1) for k in range(len(T))])
			mu_C.append([round(random.uniform(0,1),1) for k in range(len(T))])


		#generating mu_E
		#for mu_Ei in mu_E:
		#	for i in range(len(mu_Ei),len(T)):
		#		mu_Ei.append(round(random.uniform(0,1),1)) 
		#for i in range(len(mu_E),len(T)):
		#	mu_E.append([round(random.uniform(0,1),1) for k in range(len(T))])

		#generating mu_C
		#for mu_Ci in mu_C:
		#	for i in range(len(mu_Ci),len(T)):
		#		mu_Ci.append(round(random.uniform(0,1),1)) 
		#for i in range(len(mu_C),len(T)):
		#	mu_C.append([round(random.uniform(0,1),1) for k in range(len(T))])


		print("K:",K)
		print("U:",U)
		print("E:",E)
		print("T:",T)
		print("L:",L)
		print("Sigma:", sigma)
		print("mu_E:", mu_E)
		print("mu_C:", mu_C)
		print("---------------------------------------------------------")

		

		#inc_object = HOR(K, U, E , T , L ,sigma,mu_E,mu_C)

		#inc_object.generate_assignment()

		#inc_object.hor_algorithm()



if __name__ == '__main__':
	generator(int(input("Enter maximum number of events: ")))


