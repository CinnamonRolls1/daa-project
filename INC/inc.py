#------------------------------------IMPORT LIBRARIES--------------------------------------------
from assignment_object import Assignment
from assignment_object import List_timeInt
from itertools import product
from operator import attrgetter
#-------------------------------------------------------------------------------------------------

#--------------------------------GUIDLINES-------------------
#line references from Algorithm 1. INC (k, T, E, C, U)
#comment lines have been used to seprate section for each function
#please include functions definitions of functions that have been called in a function in its respective sub-section
#------------------------------------------------------------

class SES :

	def __init__(self,k = 0, U = [], E = [], T = [], location = [] ,social_active_probabilities = [],event_attendance_probability = [] ,competing_event_attendance_probability = []):
		
		self.k = k
		self.U = U
		self.E = E
		self.T = T
		self.location = location

		self.sigma = social_active_probabilities
		self.mu_E = event_attendance_probability
		self.mu_C = competing_event_attendance_probability


		self.A = []
		self.S = []

		self.L_i = [List_timeInt(i) for i in self.T]
		self.M = [Assignment() for i in self.T]
		self.bound = 0

	#-------------------GENERATE ASSIGNMENT LIST-------------------------------
	
	def generate_assignment(self) : # line 1-5 - generates all possible assignments and initializes the M list

		events = list(range(len(self.E)))
		time_intervals = list(range(len(self.T)))


		c=list(product(events,time_intervals))



		for i in c :

			t_a_e = Assignment(i[1],i[0], location= self.location[i[0]])
			self.A.append(t_a_e)

			self.L_i[t_a_e.time_interval].l.append(t_a_e)



		self.assign_score()


	def insert_M(self, t_a_e) :

		#print("inside insert_M")

		if t_a_e.score > self.M[t_a_e.time_interval].score :
			#print("inserted", t_a_e.score)
			self.M[t_a_e.time_interval] = t_a_e


	def assign_score(self) :

		for i  in self.A :
			i.score = self.score(i.event, i.time_interval, self.S+[i])
			self.insert_M(i)

		
	#-------------------------------------------------------------------------


	#-------------------SCORE CALCULATION------------------
	
	def score(self, event, time_interval, S) :
		net_score = 0

		for u in range(len(self.U)) :

			p = self.prob_e_t_u(event, time_interval, u, S)

			net_score += p

		return net_score

	def prob_e_t_u(self, event, time_interval, u, S) :

		#print("for user ",U[u])

		mu_u_e = self.mu_E[u][event]

		#print("mu_u_e: ", mu_u_e)

		sigma_u_t = self.sigma[u][time_interval]

		#print("sigma_u_t: ",sigma_u_t)

		mu_u_c = 0
		for c in range(len(self.mu_C[u])) :

			if c == time_interval :
				mu_u_c += self.mu_C[u][c]

		#print("mu_u_c: ",mu_u_c)

		mu_u_p = 0
		for p in S :

			if p.time_interval == time_interval :
				mu_u_p += self.mu_E[u][p.event]

		#print("mu_u_p: ",mu_u_p)

		p = sigma_u_t * (mu_u_e / (mu_u_c + mu_u_p))

		#print("p: ",p)

		#print()

		return p

	def update_score(self,assignment,best_assignment) :

		new_score = 0 
		old_score = 0

		new_S = self.S + [assignment]

		for i in new_S :
			new_score += self.score(i.event, assignment.time_interval, new_S)

		for i in S :
			old_score += self.score(i.event, assignment.time_interval, S)

		#assignment.score = score(assignment.event,assignment.time_interval, S+[assignment]) - score(assignment.event, assignment.time_interval, S)
		assignment.score = new_score - old_score
		return assignment.score

	#-------------------------------------------------------



	#-------------------------UPDATE LIST INTERVAL-----------------------------------

	def update__L_i(self, top_assignment) : # line 9-10 
		pass
	#--------------------------------------------------------------------------------



	#-------------------------UPDATE TOP VALID UPDATED ASSIGN LIST -------------------

	def update_M(self, top_assignment) : # line 11-15
		pass
	#----------------------------------------------------------------------------------

	#-------------------------FIND BOUND(Φ)-------------------
	def get_bound() : # line 16
		top_scorer=max(self.M, key=attrgetter('score')).score
		return top_scorer

	#--------------------------------------------------------


	#------------------------UPDATE ASSIGNMENTS-----------------------------

	def update_assignments(self) : # line 17 - 26
		pass
	#-----------------------------------------------------------------------

	

	#-------------------------SELECT TOP VALID UPDATED ASSIGNMENT-------------

	def get_top_assignment() : # line 7 '(similar to select_assignment()' from greedy.py)
		max_assignment = Assignment()

		for i in self.A:
			if (i.score > max_assignment.score) and i.valid==True:
				max_assignment = i

		return max_assignment

	#--------------------------------------------------------------------------
	

	#----------------------INC ALGORITHM------------------------------
	def INC_algo(self) : # line 6-26
	
		for i in range(self.k) :	
			top_assignment = self.get_top_assignment()

			print("top_assignment: ",top_assignment)
			self.status_log(self.A)

			self.S.append(top_assignment)

			self.update__L_i(top_assignment)

			self.update_M(top_assignment)

			self.bound = self.get_bound()

			self.update_assignments()

	#----------------------------------------------------------------

	def status_log(self,assignment_list) :

		print()
		print()

		print("Event  Time Interval  Score  Location  Validity")

		for i in assignment_list :

			if len(str(i.score)) >= 5 :

				print(self.E[i.event], '   ', self.T[i.time_interval], '           ', '{:.5}'.format(str(i.score)), '', '{:7}'.format(i.location), ' ', i.valid)

			else :
				print(self.E[i.event], '   ', self.T[i.time_interval], '           ', '{:5}'.format(str(i.score)), '', '{:7}'.format(i.location), ' ', i.valid)


		print()
		print()



