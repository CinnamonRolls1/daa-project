
U = ['u1','u2']   //Users
S = []            //Schedule
A = []            //Assignment set


sigma = [[0.8, 0.5],[0.5, 0.7]]                     //Active probability(time)
mu_E = [[0.9, 0.3, 0, 0.6],[0.2, 0.6, 0.1, 0.6]]    //Event interest
mu_C = [[0.8, 0.3],[0.4, 0.7]]                      //Competing event interest



def score(event, time_interval, S) :   
       returns net_score
       


def prob_e_t_u(event, time_interval, u, S) :   //Gives attendance probability
       returns p
       
       
def update_assignment(A, best_assignment):   //Calls update_score to update assignment 


def update_score(assignment,best_assignment): 
        returns assignment.score
        
    
def remove_assignment(A,best_assignment):     //removes best assignment from assignment list for next iteration



def combinations(a,b):

--------------------------------------------------------------------------------------------------------------------

def main:
for j in range(2) :
	for i in range(4) :

		a = Assignment(time_interval =j, event = i,)
		a.score = score(i,j,S+[a])
		A.append(a)
		#print()
		#print()

for i in A :
	print("event: ",i.event, "time_interval: ",i.time_interval, "score: ", i.score)

a = A[7]
S.append(a)

remove_assignment(A,a)


update_assignment(A,a)

print()
print()

for i in A :
print("event: ",i.event, "time_interval: ",i.time_interval, "score: ", i.score)
