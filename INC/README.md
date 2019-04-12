# Incremental Updating Algorithm
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

`self.bound`   
phi value for which values only above it are considered for updation and selection

`self.M`                   
has the top score assignment of each time interval


## Functions
`def generate_assignment():`  
  initializes `self.A` with all possible assignments and their respective scores
  initilazes `self.M` and `self.L_i` 
  
`def score(event, time_interval, S):`  
  
`def prob_e_t_u(event, time_interval, u, S):`
  
`def update_score(assignment,best_assignment):`
  
`def update__L_i():` 
Removes Top assignment from list `L_i[ ]`. And makes update status False for all the processes in the list `L_i[ ]` with same `time_interval`.
  
`def update_M():`
  
`def get_bound()`:   
Returns assignment from `self.M` with the highest `score` value.
  
`def update_assignments():`
  updates validity of assignments in `L_i[]` and also updates the score of the assignments in `L_i[]`, `self.M` and score of `bound`. Also updates the validity for each time-interval in the `L_i[]` list
  
`def get_top_assignment():`   
Returns assignment from `self.A` with the highest `score` value and `valid` set to True. 
  
`def INC_algo():`  
  its the binding fucntion which runs the overall algoirithm
