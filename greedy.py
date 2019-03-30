from assignment_object import Assignment
from itertools import product
def remove_assignment(A,best_assignment):
	#removing best assignment from assignment list
	A.remove(best_assignment)

	#removing any clashing assignments
	for assignment in A:
		if (assignment.location==best_assignment.location and assignment.time_interval==best_assignment.time_interval) or assignment.name==best_assignment.name:
			A.remove(assignment)

def update_assignment(A,best_assignment):
	pass

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
	
	
	
