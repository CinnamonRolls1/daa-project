import sys
import random
import pandas as pd
import os
from measure_time import measureGRE, measureINC, measureHOR, measureHOR_I
import math
import seaborn as sns


#importing from other folders



def generator(n):

	u=0
	e=0
	t=1
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
	t_gre=[]
	t_inc=[]
	t_hor=[]
	t_hor_i=[]
	e_list=[]
	pperc=0
	print("Generating...")
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
				sigma[k].append(round(random.uniform(0.1,1),1))

		for k in range(len(mu_C)):
			for i in range(len(mu_C[k]),len(T)):
				mu_C[k].append(round(random.uniform(0.1,1),1)) 

		for k in range(len(mu_E)):
			for i in range(len(mu_E[k]),len(E)):
				mu_E[k].append(round(random.uniform(0.1,1),1))
				

		for i in range(len(sigma),len(U)):
			sigma.append([round(random.uniform(0.1,1),1) for k in range(len(T))])

		for i in range(len(mu_C),len(U)):
			mu_C.append([round(random.uniform(0.1,1),1) for k in range(len(T))])

		for i in range(len(mu_E),len(U)):
			mu_E.append([round(random.uniform(0.1,1),1) for k in range(len(E))])
		


		#print("K:",K)
		#print("U:",U)
		#print("E:",E)
		#print("T:",T)
		#print("L:",L)
		#print("Sigma:", sigma)
		#print("mu_E:", mu_E)
		#print("mu_C:", mu_C)
		e_list.append(e)
		t_gre.append(measureGRE(K,U,E,T,L,sigma,mu_E,mu_C,False))
		t_inc.append(measureINC(K,U,E,T,L,sigma,mu_E,mu_C,False))
		t_hor.append(measureHOR(K,U,E,T,L,sigma,mu_E,mu_C,False))
		t_hor_i.append(measureHOR_I(K,U,E,T,L,sigma,mu_E,mu_C,False))

		#print("---------------------------------------------------------")

		perc=math.ceil((e/n)*100)

		while pperc!=perc:
			pperc+=1
			print("█", end='',flush=True)

	inputs={
		"No of events":e_list,
		"GRE":t_gre,
		"INC":t_inc,
		"HOR": t_hor,
		"HOR_I": t_hor_i,
	}
	sampler=pd.DataFrame({key:pd.Series(value) for key, value in inputs.items()})
	while os.path.exists("data_%s.csv" % f):
	 		f+=1
	fname="data_"+str(f)+".csv"
	sampler.to_csv(fname, index=False)
		
		
	print("\nFile written: ")
	print(fname, end=' ')
	

	df_GRE=sampler['No of events','GRE']
	df_INC=sampler['No of events','INC']
	df_HOR=sampler['No of events','HOR']
	df_HOR_I=sampler['No of events','HOR_I']


	print("Graphing...")

	#Graphing

	sns.set(style='whitegrid', font='Calibri',palette='Reds_r')
	GREplot=sns.lineplot(x='No of events',y='GRE', data=df_GRE)


	GREplot.set_title('Greedy')
	GREfig=GREplot.get_figure()
	GREfig.savefig('GRE.png')
	plt.clf()

	printer("████████████████████", end='')

	sns.set(style='whitegrid', font='Calibri',palette='Greens_r')
	INCplot=sns.lineplot(x='No of events',y='GRE', data=df_INC)


	INCplot.set_title('INC')
	INCfig=INCplot.get_figure()
	INCfig.savefig('INC.png')
	plt.clf()

	printer("████████████████████", end='')

	sns.set(style='whitegrid', font='Calibri',palette='Blues_r')
	HORplot=sns.lineplot(x='No of events',y='GRE', data=df_HOR)


	HORplot.set_title('HOR')
	HORfig=HORplot.get_figure()
	HORfig.savefig('HOR.png')
	plt.clf()

	printer("████████████████████", end='')

	sns.set(style='whitegrid', font='Calibri',palette='cubehelix')
	HOR_Iplot=sns.lineplot(x='No of events',y='GRE', data=df_HOR_I)


	HOR_Iplot.set_title('HOR_I')
	HOR_Ifig=HOR_plot.get_figure()
	HOR_Ifig.savefig('HOR_I.png')
	plt.clf()

	printer("████████████████████", end='')


		




if __name__ == '__main__':
	generator(int(input("Enter maximum number of events: ")))


