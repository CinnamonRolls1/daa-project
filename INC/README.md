## Variables
`self.k`  

`self.U`  

`self.E`   

`self.T`  

`self.location`  
Location

`self.sigma`  
social\_active\_probabilities ???

`self.mu_E`   
event\_attendance\_probability ???

`self.mu_C`   
competing\_event\_attendance\_probability ???


`self.A` 

`self.S` 

`self.L_i`  

`self.bound`   

`self.M`                   


## Functions
`def generate_assignment():`  
  
`def score(event, time_interval, S):`  
  
`def prob_e_t_u(event, time_interval, u, S):`
  
`def update_score(assignment,best_assignment):`
  
`def update__L_i():` 
  
`def update_M():`
  
`def get_bound()`:   
Returns assignment from `self.M` with the highest `score` value.
  
`def update_assignments():`
  
`def get_top_assignment():`   
Returns assignment from `self.A` with the highest `score` value and `valid` set to True. 
  
`def INC_algo():`  
