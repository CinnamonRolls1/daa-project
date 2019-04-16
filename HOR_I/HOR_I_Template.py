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
	def hor_i__algo(self) :

		while(len(self.S) < self.k) :

			if self.S == [] :
				self.generate_assignment() # line 4-7 need not be done inherited from class HOR

			else :

				for i in range(len(self.T)) :
					self.inc_assgnmnt_update(i) 


			self.select_update_assgn()
		return self.S


#--------------------------------------------------------------------------------------------------------------


#---------------------------INCREMENTAL ASSIGNMENTS UPDATING-----------------------------------------

	def inc_assgnmnt_update(self, time_interval, top_assignment) : #line 10-20 .time interval is an index in self.T
		#calls getBetterAssignment which is inherited. please do not redefine.
		#completely remove t_a_e from self.L_i for line 19 
		#M[i] = phi as in not just the score value but  the assignment . phi is always an assignment object
		
		self.bound.score=0     #Initializing bound as 0
		j=0
		while j < len(self.L_i[time_interval].l):  #For all assignments residing in L_i[i]
			if self.L_i[time_interval].l[j].valid==True:
				if self.L_i[time_interval].l[j].score >= self.bound.score:
					self.update_score(self.L_i[time_interval].l[j],top_assignment)
					self.L_i[time_interval].l[j].update == True
					self.bound = self.getBetterAssignment(self.bound,self.L_i[time_interval].l[j])
				else:
					self.L_i[time_interval].l[j].update == False
			else:
				self.L_i[time_interval].l.pop(j)
			j=j+1
		self.M[time_interval]=self.bound
		
#----------------------------------------------------------------------------------------------------------------


	def select_update_assgn(self): # line 21-30. reuse code of self.inc_assgnmnt_update() in place of 29
		for i in range(len(self.M)):

			self.status_log(self.S)

			if(len(self.S) >= self.k):
				break

			ass=self.popTopAssgn()

			eve=[i.event for i in self.S]
			eve=list(filter(lambda z : z!=None,eve))

			if len(eve)!=0 and ass.event in eve:
				has=True
			else:
				has=False

			if(has is False):

				self.S.append(ass)

			else:
				tp=None
				for i in self.L_i[ass.time_interval]:
					if((tp == None or tp.score < i.score) and i.update == True and self.not_belongs_to_S(i)): #new function needed for param
						tp=i
				self.M[tp.time_interval]=tp

				if(tp== None and self.valid(ass)):
					self.inc_assgnmnt_update(tp.time_interval)

	
obj=HOR_I()
s=obj.hor_i__algo()
def result(ob):	
	for i in ob.S:
		#print("DAFS")
		print("event","\t\t","time_interval","\t\t","location")
		print(i.event,"\t\t",i.time_interval,"\t\t",i.location)


