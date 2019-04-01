class INC_traits :
	def __init__(self, update = True):
		self.update = update	


class Assignment(INC_traits) :

	def __init__(self, time_interval = None, event = None, score = 0, location = None, valid = True, update = True):
		
		self.time_interval = time_interval
		self.event = event
		self.score = score
		self.location = location
		self.valid = valid
		INC_traits.__init__(self,update)

		
    
