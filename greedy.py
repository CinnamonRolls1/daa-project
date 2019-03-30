from assignment_object import Assignment

def remove_assignment(A,best_assignment):
	#removing best assignment from assignment list
	A.remove(best_assignment)

	#removing any clashing assignments
	for assignment in A:
		if (assignment.location==best_assignment.location and assignment.time_interval==best_assignment.time_interval) or assignment.name==best_assignment.name:
			A.remove(assignment)

def update_assignment(A,best_assignment):
	pass