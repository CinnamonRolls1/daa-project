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



file = open("input_set_0.txt", "r")
k =  int(file.read(1))
file.read(1)
U = list(file.readline().split(' '))
U = U[:-1]
#print(U)
E = list(file.readline().split(' '))
E = E[:-1]
T = list(file.readline().split(' '))
T = T[:-1]
L = list(file.readline().split(' '))
L = L[:-1]

print(E)
print(T)
print(L)
print(U)
print(k)
sigma = []

mu_E = []
temp = list(file.readline().split(' '))
temp = temp[:-1]
temp = list(map(float,temp))
print(temp)

for i in range(len(U)) :

	sigma.append([])


	for j in  range(len(T)) :
		sigma[i].append(temp[j])


for i in range(len(U)) :

	mu_E.append([])

	for j in  range(len(E)) :
		mu_E[i].append(temp[j])

mu_C = []

for i in range(len(U)) :

	mu_C.append([])
	temp = list(file.readline().split(' '))
	temp = temp[:-1]
	temp = list(map(float,temp))

	for j in  range(len(T)) :
		mu_C[i].append(temp[j])

print(sigma)
print(mu_E)
print(mu_C)
















gre_object = GRE(U, E , T , L ,sigma,mu_E,mu_C)