#------------------------------------IMPORT LIBRARIES--------------------------------------------
from assignment_object import Assignment
from assignment_object import List_timeInt
from itertools import product
from operator import attrgetter
#-------------------------------------------------------------------------------------------------

#--------------------------------GUIDELINES-------------------
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

		if t_a_e.score > self.M[t_a_e.time_interval].score :
	
			self.M[t_a_e.time_interval] = t_a_e


	def assign_score(self) :

		for i in self.A :
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

		mu_u_e = self.mu_E[u][event]

		sigma_u_t = self.sigma[u][time_interval]

		mu_u_c = 0
		for c in range(len(self.mu_C[u])) :

			if c == time_interval :
				mu_u_c += self.mu_C[u][c]

		mu_u_p = 0
		for p in S :

			if p.time_interval == time_interval :
				mu_u_p += self.mu_E[u][p.event]

		p = sigma_u_t * (mu_u_e / (mu_u_c + mu_u_p))

		return p

	def update_score(self,assignment,best_assignment) :

		new_score = 0 
		old_score = 0

		new_S = self.S + [assignment]

		for i in new_S :
			new_score += self.score(i.event, assignment.time_interval, new_S)

		for i in S :
			old_score += self.score(i.event, assignment.time_interval, S)

		assignment.score = new_score - old_score
		return assignment.score

	#-------------------------------------------------------



	#-------------------------UPDATE LIST INTERVAL-----------------------------------

	def update__L_i(self, top_assignment) : # line 9-10 
		self.L_i[top_assignment.time_interval].l.remove(top_assignment)
		top_assignment.U=False
		self.L_i[top_assignment.time_interval].update=False

		for event in self.L_i[top_assignment.time_interval].l:
			event.update=False

		#removal of associations	
		#for assignment in self.A:
		#	if ((assignment.location==top_assignment.location and assignment.time_interval==top_assignment.time_interval) or (assignment.event==top_assignment.event)):
		#		assignment.valid=False
		
	#--------------------------------------------------------------------------------



	#-------------------------UPDATE TOP VALID UPDATED ASSIGN LIST -------------------

	def update_M(self, top_assignment) : # line 11-15
		for i in self.M:
			if (i.time_interval==top_assignment.time_interval):
				i.score=float("-inf")
				i.valid=False
			elif (i.event==top_assignment.event):
				i=self.get_top_assignment(self.L_i[i.time_interval].l)



	#----------------------------------------------------------------------------------

	#-------------------------FIND BOUND(Φ)-------------------
	def get_bound(self) : # line 16
		top_scorer=max(self.M, key=attrgetter('score')).score
		return top_scorer

	#--------------------------------------------------------


	#------------------------UPDATE ASSIGNMENTS-----------------------------

	def update_assignments(self,top_assignment):
		for i in range(len(self.T)):
			if self.L_i[i].update==False and self.M[i].score<=self.bound:
				for j in self.L_i[i].l:
					if j.valid==False:
						L_i[i].l.remove(j)
					elif j.update==False and j.score >=self.bound:
						self.update_score(j,top_assignment)
						j.update=True
						self.M[i].score=self.getBetterAssignment(self.M[i].score,j.score)
						self.bound=self.getBetterAssignment(self.bound,j.score)
				temp=0
				for j in self.L_i[i]:
					if j.update==False:
						temp=1
				if temp==0:
					L_i[i].update=True
	#-----------------------------------------------------------------------

	

	#-------------------------SELECT TOP VALID UPDATED ASSIGNMENT-------------

	def get_top_assignment(self,array=None): # line 7 '(similar to select_assignment()' from greedy.py)
		max_assignment = Assignment()

		if array == None:
			array=self.A
		
		for i in array:
			if (i.score > max_assignment.score) and i.valid==True:
				max_assignment = i


		return max_assignment

	#--------------------------------------------------------------------------
	

	#----------------------INC ALGORITHM------------------------------
	def INC_algo(self) : # line 6-26
	
		for i in range(self.k) :	
			top_assignment = self.get_top_assignment()

			print("top_assignment: ",self.E[top_assignment.event], self.T[top_assignment.time_interval])

			#self.L_i[top_assignment.time_interval].l.remove(top_assignment)

			self.S.append(top_assignment)

			self.update__L_i(top_assignment)
			
			self.status_log(self.A)

			self.update_M(top_assignment)

			self.bound = self.get_bound()

			self.update_assignments(top_assignment)

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



