
class Assignment :

	def __init__(self, time_interval = None, event = None, score = 0, location = None, valid = True, update = True):
		
		self.time_interval = time_interval
		self.event = event
		self.score = score
		self.location = location
		self.valid = valid
		self.update = update

class List_timeInt :

	def __init__(self, time_interval = None, l = [], update = True):
		
		self.time_interval = time_interval
		self.l = l[:]
		self.update = update

		
    
