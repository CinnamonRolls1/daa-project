# Horizontal Assignment Algorithm
#### Many of the variables and functions have been imported from INC
## Variables

`self.k`  
no of events to be assigned

`self.U`  
lists of users 

`self.E`   
list of events

`self.T`  
list of time intervals

`self.location`  
Location

`self.sigma`  
social\_active\_probabilities ???

`self.mu_E`   
event\_attendance\_probability ???

`self.mu_C`   
competing\_event\_attendance\_probability ???


`self.A` 
list of all possible assignments

`self.S` 
schedule set

`self.L_i`  
list of assignemnt lit in each time interval

`self.M`                   
has the top score assignment of each time interval


## Functions
`def getAssign(e,time):`

`def generate_assignment():`  
  initializes `self.A` with all possible assignments and their respective scores
  initilazes `self.M` and `self.L_i` 
  
`def popTopAssgn():`  
Pops top assignment from list `M`.
  
`def select_update_assgn():`
modifies the lists `S` and `M` according to the Algorithm.

`def not_belongs_to_S(param):`
It returns `True` if param doesnt belongs to List `S`.
  
`def hor_algorithm():`  
  its the binding fucntion which runs the overall algoirithm. It resets `self.M` and calls  `generate assignments` and calls `select_update assignments`. The algorithm loop terminate when |`self.S`| gets filled with `self.k` no of candidate events.
