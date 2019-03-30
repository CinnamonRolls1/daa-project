from assignment_object import Assignment
from itertools import product

U = ['u1','u2']
S = []
A = []



sigma = [[0.8, 0.5],[0.5, 0.7]]
mu_E = [[0.9, 0.3, 0, 0.6],[0.2, 0.6, 0.1, 0.6]]
mu_C = [[0.8, 0.3],[0.4, 0.7]]



def score(event, time_interval, S) :

	net_score = 0

	for u in range(len(U)) :

		p = prob_e_t_u(event, time_interval, u, S)

		net_score += p

	return net_score



def prob_e_t_u(event, time_interval, u, S) :

	print("for user ",U[u])

	mu_u_e = mu_E[u][event]

	print("mu_u_e: ", mu_u_e)

	sigma_u_t = sigma[u][time_interval]

	print("sigma_u_t: ",sigma_u_t)

	mu_u_c = 0
	for c in range(len(mu_C[u])) :

		if c == time_interval :
			mu_u_c += mu_C[u][c]

	print("mu_u_c: ",mu_u_c)

	mu_u_p = 0
	for p in S :

		if p.time_interval == time_interval :
			mu_u_p += mu_E[u][p.event]

	print("mu_u_p: ",mu_u_p)

	p = sigma_u_t * (mu_u_e / (mu_u_c + mu_u_p))

	print("p: ",p)

	print()

	return p


def update_assignment(A, best_assignment):
	
	for i in A :

		if i.time_interval == best_assignment.time_interval :
			i.score = update_score(i,best_assignment)



def update_score(assignment,best_assignment) :

	assignment.score = score(assignment.event,assignment.time_interval, S+[assignment]) - assignment.score
	return assignment.score


for j in range(2) :
	for i in range(4) :

		a = Assignment(time_interval =j, event = i,)
		a.score = score(i,j,S+[a])
		A.append(a)
		#print()
		#print()



for i in A :
	print("event: ",i.event, "time_interval: ",i.time_interval, "score: ", i.score)

a = Assignment(1,3)
S.append(a)


update_assignment(A,a)

print()
print()

for i in A :
	print("event: ",i.event, "time_interval: ",i.time_interval, "score: ", i.score)
  

def remove_assignment(A,best_assignment):
	#removing best assignment from assignment list
	A.remove(best_assignment)

	#removing any clashing assignments
	for assignment in A:
		if (assignment.location==best_assignment.location and assignment.time_interval==best_assignment.time_interval) or assignment.name==best_assignment.name:
			A.remove(assignment)


def combinations(a,b):
	c=list(product(a,b))
	return c



def main():
	scheduled=[]
	events=input("Enter the no. of events to schedule: ")
	events=events.split()
	events=[int(i) for i in events]
	candidate=input("The number of candidate events: ")
	candidate=candidate.split()
	candidate=[int(i) for i in candidate]
	n=int(input("no. of time intervals"))
	t=[]
	for i in range(n):
	t.append(input())
	n=int(input("enter the number of users:"))
	usocial=[[]*len(t)]*len(n)
	print("social activity probability for the user at time t:")
	for i in range(n):
		for j in range(len(t)):
			usocial[i][j]=float(input())
	affinity=[[]*len(events)]*n
	print("affinity probability for users over events")
	for i in range(n):
		for j in range(len(events)):
			affinity[i][j]=float(input())
	
	
	

