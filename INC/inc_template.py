from assignment_object import Assignment
from assignment_object import INC_traits
from itertools import product
from operator import attrgetter


#line references from Algorithm 1. INC (k, T, E, C, U)

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

		self.L_t = []
		self.bound = 0
		self.M = []

	#-------------------GENERATE ASSIGNMENT LIST-------------------------------
	
	def generate_assignment() : # line 1-5
		pass

	#-------------------------------------------------------------------------


	#-------------------SCORE CALCULATION------------------
	
	def score(event, time_interval, S) :
		pass

	def prob_e_t_u(event, time_interval, u, S) :
		pass

	def update_score(assignment,best_assignment) :
		pass

	#-------------------------------------------------------



	#-------------------------UPDATE LIST INTERVAL-----------------------------------

	def update__L_t() : # line 9-10 
		pass
	#--------------------------------------------------------------------------------



	#-------------------------UPDATE TOP VALID UPDATED ASSIGN LIST -------------------

	def update_M() : # line 11-15
		pass
	#----------------------------------------------------------------------------------

	#-------------------------FIND BOUND(Φ)-------------------

	def get_bound() : # line 16
		pass

	#--------------------------------------------------------


	#------------------------UPDATE ASSIGNMENTS-----------------------------

	def update_assignments() : # line 17 - 26
		pass
	#-----------------------------------------------------------------------

	

	#-------------------------SELECT TOP VALID UPDATED ASSIGNMENT-------------

	def get_top_assignment() : # line 7 '(similar to select_assignment()' from greedy.py)
		pass

	#--------------------------------------------------------------------------
	

	#----------------------INC ALGORITHM------------------------------
	def INC_algo() : # line 6-26
		pass

	#----------------------------------------------------------------
