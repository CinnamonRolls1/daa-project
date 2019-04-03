# Greedy Algorithm
## Variables
Users  
`U = ['u1','u2']`   

Schedule  
`S = []`  

Assignment set            
`A = []`        

Active probability(time)  
`sigma = [[0.8, 0.5],[0.5, 0.7]]`      

Event interest                
`mu_E = [[0.9, 0.3, 0, 0.6],[0.2, 0.6, 0.1, 0.6]]`   

Competing event interest  
`mu_C = [[0.8, 0.3],[0.4, 0.7]]`                     


## Functions
`def score(event, time_interval, S) :`   
Returns net_score
       


`def prob_e_t_u(event, time_interval, u, S):`   
Returns p
       
       
`def update_assignment(A, best_assignment):`   
Calls update_score to update assignment 


`def update_score(assignment,best_assignment):`   
Returns assignment.score
        
    
`def remove_assignment(A,best_assignment):`     
removes best assignment from assignment list for next iteration


`def combinations(a,b):`   
creates combination set of two given sets
