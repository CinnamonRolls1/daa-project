#------------------------------------IMPORT LIBRARIES--------------------------------------------
import sys

sys.path.insert(0, '../imports')
from assignment_object import Assignment

sys.path.insert(0, '../imports')
from assignment_object import List_timeInt

from itertools import product
from operator import attrgetter
sys.path.insert(0, '../imports')
from class_ses import SES
sys.path.insert(0,'../Greedy')
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

		super().generate_assignment()

    							#list for all available events
		se= set(list(map(lambda x: x.event, self.S)))           #List for all events in the schedule set

		e = set(list(range(len(self.E))))

		diff_e = e.difference(se)


		events = list(diff_e) #Finding uncommon elements using a method I found at https://stackoverflow.com/questions/11348347/find-non-common-elements-in-lists



		time_intervals = list(range(len(self.T)))  #list of time intervals
		c = list(product(events,time_intervals))   #All possible combinations of events and time intervals


		for i in c:
			x=self.getAssign(i[0],i[1])   #returns assignment with the given event and time interval
			self.print_assignment(x)
			if x.valid == True:
				x.score = self.score(x.event, x.time_interval, self.S+[x])
				#print("out of range error val: ",i[1])
				self.L_i[i[1]].append(x)
				if self.M[i[1]].event == "":
					self.M[i[1]] = x
				self.M[i[1]] = self.getBetterAssignment(self.M[i[1]],x)

		

	#--------------------------------------------------------------------------------------


	def popTopAssgn(self) : #line 10
		top=None
		index=None
		for i in range(len(self.M)):
			if(self.M[i].event  == ""):
				continue
			elif((top == None) or (top.score < self.M[i].score)):
				top=self.M[i]
				index=i
		self.M[index] = Assignment()

		return top

	#----------------------------SELECT and UPDATE ASSIGNMENT from M----------------------------------

	def select_update_assgn(self) : #line 9-14
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

			if(has == False):

				self.S.append(ass)
			else:
				tp=None
				for i in self.L_i[ass.time_interval]:
					if((tp == None or tp.score < i.score) and self.not_belongs_to_S(i)): #new function needed for param
						tp=i

				
				self.M[tp.time_interval]=tp #line 14	
					    
	def not_belongs_to_S(self,param):  #returns true if param doesnt belong to S
		for i in range(len(self.S)):
			if(self.S[i].event == param.event):
				return False
		return True
			


	#-------------------------------------------------------------------------------------------------

	#---------------------------ALGORITHM-------------------------------------------------------------

	def hor_algorithm(self) :

		while(len(self.S)<self.k):

			self.status_log()

			self.generate_assignment()

			self.select_update_assgn()
			




