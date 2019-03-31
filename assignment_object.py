class Assignment:
  
  def __init__(self, time_interval=None, event=None, score=0, location=None, valid=True) :
    self.location = location
    self.time_interval = time_interval
    self.event =  event
    self.score = score
    self.valid = valid
    
