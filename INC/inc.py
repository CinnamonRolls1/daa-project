#------------------------------------IMPORT LIBRARIES--------------------------------------------
import sys
sys.path.insert(0, '../imports')
from imports import Assignment, printer

from imports import List_timeInt
sys.path.insert(0,'../INC')
from itertools import product
from operator import attrgetter


#-------------------------------------------------------------------------------------------------

#--------------------------------GUIDELINES-------------------
#line references from Algorithm 1. INC (k, T, E, C, U)
#comment lines have been used to seprate section for each function
#please include functions definitions of functions that have been called in a function in its respective sub-section
#------------------------------------------------------------

class INC:

	def __init__(self,k = 0, U = [], E = [], T = [], location = [] ,social_active_probabilities = [],event_attendance_probability = [] ,competing_event_attendance_probability = [],verbose=True):
		
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
		self.bound = Assignment()
		self.verbose=verbose

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


	def getBetterAssignment(self, current_assignment, t_a_e) :

		if t_a_e.score > current_assignment.score :
	
			current_assignment = t_a_e

		return current_assignment


	def assign_score(self) :

		for i in self.A :
			i.score = self.score(i.event, i.time_interval, self.S+[i])
			self.M[i.time_interval] = self.getBetterAssignment(self.M[i.time_interval],i)

		
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

		for i in self.S :
			old_score += self.score(i.event, assignment.time_interval, self.S)

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
		for i in range(len(self.M)):
			if (self.M[i].time_interval==top_assignment.time_interval):
				self.M[i].score=float("-inf")
				self.M[i].valid=False
			elif (self.M[i].event==top_assignment.event):
				#self.status_log(self.L_i[i].l)
				self.M[i]=self.get_top_assignment(self.L_i[i].l)



	#----------------------------------------------------------------------------------

	#-------------------------FIND BOUND(Φ)-------------------
	def get_bound(self) : # line 16

		flag = False

		for i in self.M :
			if i.update and i.valid :
				flag = True

		top_scorer = Assignment(score = "unavailable")
		if flag :
			top_scorer=max(self.M, key=attrgetter('score'))

		return top_scorer

	#--------------------------------------------------------


	#------------------------UPDATE ASSIGNMENTS-----------------------------

	def update_assignments(self,top_assignment):

		update_assignment_list = []
		for i in range(len(self.T)):

			if self.bound.score == "unavailable" :
				max = Assignment()
				for j in range(len(self.A)) :
					if self.A[j].valid and self.A[j].score > max.score :
						max = self.A[j]

				self.update_score(max,top_assignment)
				max.update = True
				update_assignment_list.append(max)
				self.bound = max

				break


			if self.L_i[i].update==False and self.M[i].score<=self.bound.score:
				#printer(i)

				j = 0
				while j < len(self.L_i[i].l) :

					#
					if self.L_i[i].l[j].valid==False:
						self.L_i[i].l.pop(j)


					elif self.L_i[i].l[j].update==False and self.L_i[i].l[j].score >=self.bound.score:
						self.update_score(self.L_i[i].l[j],top_assignment)
						self.L_i[i].l[j].update=True
						update_assignment_list.append(self.L_i[i].l[j])
						self.M[i] = self.getBetterAssignment(self.M[i],self.L_i[i].l[j])

						self.bound = self.getBetterAssignment(self.bound,self.L_i[i].l[j])

					j += 1

					
				temp=0
				for j in self.L_i[i].l:
					if j.update==False:
						temp=1
						break
				if temp==0:
					self.L_i[i].update=True
				


		for i in range(len(self.M)):
			#max = Assignment()
			printer(("M[i] = ", self.printer_assignment(self.M[i])),verbose=self.verbose)


			for j in range(len(self.L_i[i].l)):

				printer(("L_i.l= ",self.printer_assignment(self.L_i[i].l[j]) ),verbose=self.verbose)

				if self.L_i[i].l[j].valid == True and self.L_i[i].l[j].update == True :

					self.M[i] = self.getBetterAssignment(self.M[i],self.L_i[i].l[j])

					
		self.printer_updated_assignments(update_assignment_list)

	#-----------------------------------------------------------------------

	

	#-------------------------SELECT TOP VALID UPDATED ASSIGNMENT-------------

	def get_top_assignment(self,array=None): # line 7 '(similar to select_assignment()' from greedy.py)
		max_assignment = Assignment()
		max_assignment.score = float('-inf')

		if array == None:
			array=self.A
		
		for i in array:
			if (i.score > max_assignment.score) and (i.valid==True) and (i.update == True):
				max_assignment = i



		return max_assignment

	def update_validity(self,top_assignment) :

		for assignment in self.A:
			if ((assignment.location==top_assignment.location and assignment.time_interval==top_assignment.time_interval) or (assignment.event==top_assignment.event)):
				assignment.valid=False

	#--------------------------------------------------------------------------
	

	#----------------------INC ALGORITHM------------------------------
	def INC_algo(self) : # line 6-26


		self.status_log(self.A)
	
		for i in range(self.k) :	
			top_assignment = self.get_top_assignment(self.M)

			printer(("top_assignment: ",self.E[top_assignment.event], self.T[top_assignment.time_interval]),verbose=self.verbose)

			self.update_validity(top_assignment)
			#self.status_log(self.A)

			#self.L_i[top_assignment.time_interval].l.remove(top_assignment)

			self.S.append(top_assignment)

			self.update__L_i(top_assignment)
			

			self.update_M(top_assignment)
			
			self.bound = self.get_bound()

			printer(("                       status_log 1                         "),verbose=self.verbose)
			self.status_log(self.A)
			

			

			self.update_assignments(top_assignment)
			
			printer(("                       status_log 2                         "),verbose=self.verbose)
			self.status_log(self.A)

			#self.printer_updated_assignments()


	#----------------------------------------------------------------

	#--------------------------------------------------------DISPLAY----------------------------------------------
	def status_log(self,assignment_list) :

		printer("\n",verbose=self.verbose)
		printer("\n",verbose=self.verbose)
		printer("-------------------------------------------------------------",verbose=self.verbose)

		printer("Event  Time Interval  Score  Location  Validity",verbose=self.verbose)

		for i in assignment_list :

			if len(str(i.score)) >= 5 :

				printer((self.E[i.event], '   ', self.T[i.time_interval], '           ', '{:.5}'.format(str(i.score)), '', '{:7}'.format(i.location), ' ', i.valid),verbose=self.verbose)

			else :
				printer((self.E[i.event], '   ', self.T[i.time_interval], '           ', '{:5}'.format(str(i.score)), '', '{:7}'.format(i.location), ' ', i.valid),verbose=self.verbose)


		printer(("Bound: ",self.printer_assignment(self.bound), " ", self.bound.score),verbose=self.verbose)

		printer(("M: ", list(map(self.printer_assignment,self.M)),"\n"),verbose=self.verbose)
		printer(("L_1: ",list(map(self.printer_assignment,self.L_i[0].l))," update: ",self.L_i[0].update),verbose=self.verbose)
		printer(("L_2: ", list(map(self.printer_assignment,self.L_i[1].l))," update: ",self.L_i[1].update,"\n"),verbose=self.verbose)


		printer(("--------------------------------------------------------------"),verbose=self.verbose)
		printer("\n",verbose=self.verbose)
		printer("\n",verbose=self.verbose)

	def printer_assignment(self,assignment):

		if assignment.event == '' :
			return str(assignment.time_interval + "_a_" + assignment.event)
			
		return str(self.T[assignment.time_interval] + "_a_" + self.E[assignment.event])


	def printer_updated_assignments(self,UA_list):

		printer("Updated Assignments:  ",end = ' ',verbose=self.verbose)

		for j in UA_list :
			if j.update :
				printer(self.printer_assignment(j),end = "  ",verbose=self.verbose)

		printer("\n\n",verbose=self.verbose)
		

	#----------------------------------------------------------------------------------------------------------------

