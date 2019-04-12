##Assignment Object
`self.time_interval` = index of time_interval in `self.T`
`self.event` =  index of event in `self.E` 
`self.score` = float value that stores expected attendance
`self.location` = index of venue from `self.location`
`self.valid` = Stores  *True* if it is valid assignment else *False*
`self.update` = *True* if it is updated *False* if  it is yet to be update

##Class HOR_I

###Variables

`self.k` = no of events tat have to be scheduled

`self.U` = list([u1,u2,...]) of users 

`self.E` =  list([e1,e2,e3....]) of candidate events

`self.T` = list([t1,t2,...]) of time intervals available

`self.location` = list of venues availabe



`self.sigma` = social_active_probabilities of each user for each time interval users are represented as rows and time intervals as columns

`self.mu_E` = event\_attendance\_probability of each user attenndance for every event

`self.mu_C` = competing\_event\_attendance\_probability of each competing event for evey user


`self.A` : deprecated for HOR-I algorithm as well as HOR

`self.S` : set of scheduled events 

`self.L_i` = list of   lists where each list stores the assignments under that particular time interval  and each index maps to the index of the relevant time interval in `self.T`

`self.M` :   stores max(L<sub>t</sub>, key = (`Assignment().score ) &  `Assignment().valid` = *True* &  `Assignment.update` = *True* 


`self.bound` = stores value of `Assignment()` 

###Methods

hor_i() :
runs until |`self.S`| >= `self.k`
perfoms the overall algorithm








