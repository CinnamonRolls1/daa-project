
#-------------------IMPORTING LIBRARIES-------------
from assignment_object import Assignment
from itertools import product
from operator import attrgetter
#----------------------------------------------------

#-------------------------------DATA AND GLOBAL VARIABLES---------------------------

U = ['u1','u2']
S = []
A = []
E = ['e1','e2','e3','e4']
T = ['t1','t2']
location = ['Stage 1', 'Stage 1', 'Stage 2', 'Room A']

sigma = [[0.8, 0.5],[0.5, 0.7]]
mu_E = [[0.9, 0.3, 0, 0.6],[0.2, 0.6, 0.1, 0.6]]
mu_C = [[0.8, 0.3],[0.4, 0.7]]

#-------------------------------------------------------------------------------------


#------------------------------------SCORE CALCULATION-----------------------------------------------------------

def score(event, time_interval, S) :

	net_score = 0

	for u in range(len(U)) :

		p = prob_e_t_u(event, time_interval, u, S)

		net_score += p

	return net_score



def prob_e_t_u(event, time_interval, u, S) :

	#print("for user ",U[u])

	mu_u_e = mu_E[u][event]

	#print("mu_u_e: ", mu_u_e)

	sigma_u_t = sigma[u][time_interval]

	#print("sigma_u_t: ",sigma_u_t)

	mu_u_c = 0
	for c in range(len(mu_C[u])) :

		if c == time_interval :
			mu_u_c += mu_C[u][c]

	#print("mu_u_c: ",mu_u_c)

	mu_u_p = 0
	for p in S :

		if p.time_interval == time_interval :
			mu_u_p += mu_E[u][p.event]

	#print("mu_u_p: ",mu_u_p)

	p = sigma_u_t * (mu_u_e / (mu_u_c + mu_u_p))

	#print("p: ",p)

	#print()

	return p

def update_score(assignment,best_assignment) :

	new_score = 0 
	old_score = 0

	new_S = S + [assignment]

	for i in new_S :
		new_score += score(i.event, assignment.time_interval, new_S)

	for i in S :
		old_score += score(i.event, assignment.time_interval, S)

	#assignment.score = score(assignment.event,assignment.time_interval, S+[assignment]) - score(assignment.event, assignment.time_interval, S)
	assignment.score = new_score - old_score
	return assignment.score


#----------------------------------------------------------------------------------------




#------------------------------------------------------ALGORITHM----------------------------------------------
def update_assignment(A, best_assignment):

	print()
	print("Assignments to be updated: ")
	print()
	
	for i in A :

		if i.time_interval == best_assignment.time_interval and i.valid :
			print('(', i.time_interval, ' a ', i.event, ')', end = ' ')
			i.score = update_score(i,best_assignment)

	print()
	print()

  

def remove_assignment(A,best_assignment): 
	
	best_assignment.valid=False  #removing best assignment from assignment list

	#removing any clashing assignments
	#print("\nLooking for clashes with "+str(best_assignment.event)+" at "+str(best_assignment.location)+" during "+str(best_assignment.time_interval))
	for assignment in A:
		#print(assignment.event,"\t",assignment.location,"\t",assignment.time_interval)
		if ((assignment.location==best_assignment.location and assignment.time_interval==best_assignment.time_interval) or (assignment.event==best_assignment.event)):
			assignment.valid=False




def generate_assigment(events,time_intervals):


	c=list(product(events,time_intervals))

	for i in c :

		a = Assignment(i[1],i[0], location= location[i[0]])
		A.append(a)


def greedy_alg(k=3):


	generate_assigment(list(range(len(E))),list(range(len(T))))

	assign_score()

	status_log()
	
	for i in range(k):


		best_assignment=select_assignment()

		print("Selection:", E[best_assignment.event],' ', T[best_assignment.time_interval], ' ', best_assignment.score)
		S.append(best_assignment)

		remove_assignment(A,best_assignment)

		update_assignment(A,best_assignment)

		status_log()





def select_assignment():

	max_assignment = Assignment()

	for i in A :

		if (i.score > max_assignment.score) and i.valid :
			max_assignment = i


	return max_assignment


def assign_score() :

	for i in A :
		i.score = score(i.event, i.time_interval, S+[i])



#------------------------------------------------------------------------------------------------------------

def status_log() :

	print()
	print()

	print("Event  Time Interval  Score  Location  Validity")

	for i in A :

		if len(str(i.score)) >= 5 :

			print(E[i.event], '   ', T[i.time_interval], '           ', '{:.5}'.format(str(i.score)), '', '{:7}'.format(i.location), ' ', i.valid)

		else :
			print(E[i.event], '   ', T[i.time_interval], '           ', '{:5}'.format(str(i.score)), '', '{:7}'.format(i.location), ' ', i.valid)


	print()
	print()


#-----------------------------------------------EXECUTION---------------------------------------------------

def main() :


	greedy_alg()



main()












