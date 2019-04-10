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
	def getAssign(self,e,time):
		for i in self.A:
			if i.event == e and i.time_interval == time:
				return i


	def generate_assignment(self): # line 4-8
		ev=list(self.E)
		se=list()
		for i in self.S:
			se.append(i.event)


		events = list(range(len(set(ev).intersection(se)))) #Finding uncommon elements using a method I found at https://stackoverflow.com/questions/11348347/find-non-common-elements-in-lists
		time_intervals = list(range(len(self.T)))
		c = list(product(events,time_intervals))
		for i in c:
			x=self.getAssign(i[0],i[1])
			if x.valid == True:
				x.score = self.score(x.event, x.time_interval, self.S)
				self.L_i[i[1]].l.append(events)
				if self.M[i[1]] == None:
					self.M[i[1]] = x
				self.M[i[1]] = getBetterAssignment(self.M[i[1]].score,x.score)

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
				tp=None
				for i in self.L_i[ass.time_interval]:
					if((tp == None or tp.score < i.score) and not_belongs_to_S(param)): #new function needed for param
						tp=i
				
				M.append(tp). #line 14	
					    
	def not_belongs_to_S(param):  #returns true if param doesnt belong to S
		for i in S:
			if(i == param):
				return False
		return True

	def popTopAssgn(self) : #line 10
		top=None
		for i in M:
			if(top == None or top.score < i.score):
				top=i
		M.remove(top)
		return top
			

	def update_M(self,best_assignment) : #line 14
		pass

	#-------------------------------------------------------------------------------------------------

	#---------------------------ALGORITHM-------------------------------------------------------------

	def hor_algorithm(self) :



		for i in range(len(self.S)) :

			self.M = [Assignment() for i in self.T]

			self.L_i = [[] for i in self.T]0

			self.generate_assignment()

			self.select_update_assgn()

