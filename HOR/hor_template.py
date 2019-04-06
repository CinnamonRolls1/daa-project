#------------------------------------IMPORT LIBRARIES--------------------------------------------
from assignment_object import Assignment
from assignment_object import List_timeInt
from itertools import product
from operator import attrgetter
from class_ses import SES
#-------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class HOR(SES) :

	def __init__(self,k = 0, U = [], E = [], T = [], location = [] ,social_active_probabilities = [],event_attendance_probability = [] ,competing_event_attendance_probability = []):
		
		super().__init__(k , U , E , T , location  ,social_active_probabilities ,event_attendance_probability ,competing_event_attendance_probability )

		self.L_i = [[] for i in self.T]


	#-------------------------------GENERATE ASSIGNEMENT LIST------------------------------
	def generate_assignment(self) : # line 4-8
		pass

	def getBetterAssgn(self,M_t, t_a_e) : #line 8
		pass

	#--------------------------------------------------------------------------------------

	#----------------------------SELECT and UPDATE ASSIGNMENT from M----------------------------------

	def select_update_assgn(self) : #line 9-14
		while( len(M) != 0):
			ass=popTopAssgn()
			has=False
			for i in S:
				if(ass.event == i.event):
					has=True
					break
			if(has == False):
				S.append(ass)
			else:
				update_M(). # The parameter to this function need to be calculated separately
					    # the top assignment is from list L_t_p and e_i doesnot belong to S 
				

	def popTopAssgn(self) : #line 10
		pass

	def update_M(self,best_assignment) : #line 14
		pass

	#-------------------------------------------------------------------------------------------------

	#---------------------------ALGORITHM-------------------------------------------------------------

	def hor_algorithm(self) :

		for i in range(len(self.S)) :

			self.generate_assignment()

			self.select_update_assgn()

