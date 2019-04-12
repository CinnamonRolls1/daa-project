# Horizontal Assignment Algorithm
#### Many of the variables and functions have been imported from INC
## Variables

`self.k`  
Number of events to be assigned

`self.U`  
Lists of users 

`self.E`   
List of events

`self.T`  
List of time intervals

`self.location`  
Location

`self.sigma`  
Social active probabilities

`self.mu_E`   
Event attendance probability 

`self.mu_C`   
Competing event attendance probability 


`self.A` 
List of all possible assignments

`self.S` 
Schedule set

`self.L_i`  
List of assignemnt lit in each time interval

`self.M`                   
Has the top score assignment of each time interval


## Functions
`def getAssign(e,time):`  
  Returns an existing assignment within `self.A` correlating to an event and time-interval that are given as arguments 

`def generate_assignment():`    
  Initializes `self.A` with all possible assignments and their respective scores
  Initilazes `self.M` and `self.L_i` 
  
`def popTopAssgn():`    
Pops top assignment from list `M`.
  
`def select_update_assgn():`  
modifies the lists `S` and `M` according to the Algorithm.

`def not_belongs_to_S(param):`  
It returns `True` if param doesnt belongs to List `S`.
  
`def hor_algorithm():`    
  It's the binding function which runs the overall algoirithm. It resets `self.M` and calls  `generate assignments` and calls `select_update assignments`. The algorithm loop terminate when `self.S` gets filled with `self.k` no of candidate events.
