#------------------------------------IMPORT LIBRARIES--------------------------------------------
from assignment_object import Assignment
from assignment_object import List_timeInt
from itertools import product
from operator import attrgetter
from hor import HOR
#-------------------------------------------------------------------------------------------------

#--------------------------------GUIDELINES-------------------
#line references from Algorithm 1. INC (k, T, E, C, U)
#comment lines have been used to seprate section for each function
#please include functions definitions of functions that have been called in a function in its respective sub-section
#------------------------------------------------------------

class HOR_I(HOR) :

	def __init__(self,k = 0, U = [], E = [], T = [], location = [] ,social_active_probabilities = [],event_attendance_probability = [] ,competing_event_attendance_probability = []):
		
		super().__init__(k , U , E , T , location  ,social_active_probabilities ,event_attendance_probability ,competing_event_attendance_probability )

	
#-------------------------------------ALGORITHM---------------------------
	def hor_i__algo() :

		while(len(self.S) < self.k) :

			if self.S == [] :
				self.generate_assignment() # line 4-7 need not be done inherited from class HOR

			else :

				for i in range(len(self.T)) :
					self.inc_assgnmnt_update(i) 


			self.select_update_assgn()


#--------------------------------------------------------------------------------------------------------------


#---------------------------INCREMENTAL ASSIGNMENTS UPDATING-----------------------------------------

	def inc_assgnmnt_update(self, time_interval) : #line 10-20 .time interval is an index in self.T
		#calls getBetterAssignment which is inherited. please do not redefine.
		#completely remove t_a_e from self.L_i for line 19 
		#M[i] = phi as in not just the score value but  the assignment . phi is always an assignment object
		pass
#----------------------------------------------------------------------------------------------------------------


	def select_update_assgn(self): # line 21-30. reuse code of self.inc_assgnmnt_update() in place of 29
		# please refer to the definittion of this function in hor.py since they are similar however not the exact same.
		#self.popTopAssgn() can be reused from hor.py 
		pass
	



