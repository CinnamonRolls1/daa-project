
#-------------------IMPORTING LIBRARIES-------------
import sys

sys.path.insert(0, '../imports')
from imports import Assignment, printer
sys.path.insert(0,'../Greedy')
from itertools import product
from operator import attrgetter
#----------------------------------------------------

class GRE:

        #-------------------------------DATA AND GLOBAL VARIABLES---------------------------

        def __init__(self,U = [],E = [],T = [],location = [],sigma = [],mu_E = [],mu_C = [],verbose=True):
                self.U = U[:]
                self.S = []
                self.A = []
                self.E = E[:]
                self.T = T[:]
                self.location = location[:]

                self.sigma = sigma[:]
                self.mu_E = mu_E[:]
                self.mu_C = mu_C[:]
                self.verbose=verbose

        #-------------------------------------------------------------------------------------


        #------------------------------------SCORE CALCULATION-----------------------------------------------------------

        def score(self,event, time_interval, S) :

                net_score = 0

                for u in range(len(self.U)) :

                        p = self.prob_e_t_u(event, time_interval, u, S)

                        net_score += p

                return net_score



        def prob_e_t_u(self,event, time_interval, u, S) :

                #printer("for user ",self.U[u])
                #printer("Schedule Set: ",list(map(lambda x: x.event, S)),"\n")

                mu_u_e = self.mu_E[u][event]

                #printer("mu_u_e: ", mu_u_e)

                sigma_u_t = self.sigma[u][time_interval]

                #printer("sigma_u_t: ",sigma_u_t)

                mu_u_c = 0
                #printer(u)
                #printer(self.mu_C)
                for c in range(len(self.mu_C[u])) :

                        if c == time_interval :
                                #printer("inside loop")
                                mu_u_c += self.mu_C[u][c]
                                #printer("inside mu_u_c",self.mu_C[u][c])

                #printer("mu_u_c: ",mu_u_c)

                mu_u_p = 0
                for p in S :

                        if p.time_interval == time_interval :

                                mu_u_p += self.mu_E[u][p.event]
                                #printer("inside mu_u_p", self.mu_E[u][p.event])

                
                #printer("mu_u_p: ",mu_u_p)
                #printer("mu_u_c: ",mu_u_c)

                p = sigma_u_t * (mu_u_e / (mu_u_c + mu_u_p))

                #printer("p: ",p)

                #printer("\n")

                return p

        def update_score(self,assignment,best_assignment) :

                new_score = 0 
                old_score = 0

                new_S = self.S + [assignment]

                for i in new_S :
                        new_score += self.score(i.event, assignment.time_interval, new_S)

                for i in self.S :
                        old_score += self.score(i.event, assignment.time_interval, self.S)

                #assignment.score = score(assignment.event,assignment.time_interval, S+[assignment]) - score(assignment.event, assignment.time_interval, S)
                assignment.score = new_score - old_score
                return assignment.score


        #----------------------------------------------------------------------------------------




        #------------------------------------------------------ALGORITHM----------------------------------------------
        def update_assignment(self,A, best_assignment):

                printer("\n",verbose=self.verbose)
                printer("Assignments to be updated: ",verbose=self.verbose)
                printer("\n",verbose=self.verbose)
                
                for i in A :

                        if i.time_interval == best_assignment.time_interval and i.valid :
                                printer(('(', i.time_interval, ' a ', i.event, ')'), end = ' ',verbose=self.verbose)
                                i.score = self.update_score(i,best_assignment)

                printer("\n",verbose=self.verbose)
                printer("\n",verbose=self.verbose)

          

        def remove_assignment(self,A,best_assignment): 
                
                best_assignment.valid=False  #removing best assignment from assignment list

                #removing any clashing assignments
                #printer("\nLooking for clashes with "+str(best_assignment.event)+" at "+str(best_assignment.location)+" during "+str(best_assignment.time_interval))
                for assignment in A:
                        #printer(assignment.event,"\t",assignment.location,"\t",assignment.time_interval)
                        if ((assignment.location==best_assignment.location and assignment.time_interval==best_assignment.time_interval) or (assignment.event==best_assignment.event)):
                                assignment.valid=False




        def generate_assigment(self,events,time_intervals):


                c=list(product(events,time_intervals))
                #printer(c)

                for i in c :

                        a = Assignment(i[1],i[0],location= self.location[i[0]])
                        self.A.append(a)


        def greedy_alg(self,k=3):


                self.generate_assigment(list(range(len(self.E))),list(range(len(self.T))))

                self.assign_score()

                self.status_log()
                
                for i in range(k):


                        best_assignment=self.select_assignment()
                        printer(best_assignment,verbose=self.verbose)
                        printer(("Selection:", best_assignment.event,' ', best_assignment.time_interval, ' ', best_assignment.score),verbose=self.verbose)
                        printer(("Selection:", self.E[best_assignment.event],' ', self.T[best_assignment.time_interval], ' ', best_assignment.score),verbose=self.verbose)
                        self.S.append(best_assignment)

                        self.remove_assignment(self.A,best_assignment)

                        self.update_assignment(self.A,best_assignment)

                        self.status_log()





        def select_assignment(self):

                max_assignment = Assignment()
                max_assignment.score = float('-inf')

                for i in self.A :

                        if (i.score > max_assignment.score) and i.valid :
                                max_assignment = i


                return max_assignment


        def assign_score(self) :

                for i in self.A :
                        i.score = self.score(i.event, i.time_interval, self.S+[i])



        #------------------------------------------------------------------------------------------------------------

        def status_log(self,assignment_list = None) :

                if assignment_list == None :
                        assignment_list = self.A

                printer("\n",verbose=self.verbose)
                printer("\n",verbose=self.verbose)
                printer("-------------------------------------------------------------",verbose=self.verbose)

                printer("Event  Time Interval  Score  Location  Validity",verbose=self.verbose)

                for i in assignment_list :

                        if len(str(i.score)) >= 5 :

                                printer((self.E[i.event], '   ', self.T[i.time_interval], '           ', '{:.5}'.format(str(i.score)), '', '{:7}'.format(i.location), ' ', i.valid),verbose=self.verbose)

                        else :
                                printer((self.E[i.event], '   ', self.T[i.time_interval], '           ', '{:5}'.format(str(i.score)), '', '{:7}'.format(i.location), ' ', i.valid),verbose=self.verbose)


                #printer("Bound: ",self.printer_assignment(self.bound), " ", self.bound.score)

                #self.printer_M()

                #printer("M: ", list(map(self.printer_assignment,self.M)),"\n")
                #printer("L_1: ",list(map(self.printer_assignment,self.L_i[0].l))," update: ",self.L_i[0].update)
                #printer("L_2: ", list(map(self.printer_assignment,self.L_i[1].l))," update: ",self.L_i[1].update,"\n")


                printer("--------------------------------------------------------------",verbose=self.verbose)
                printer("\n",verbose=self.verbose)
                printer("\n",verbose=self.verbose)


#-----------------------------------------------EXECUTION---------------------------------------------------


if __name__ == '__main__':
        test=GRE(['u1','u2'],['e1','e2','e3','e4'],['t1','t2'],['Stage 1', 'Stage 1', 'Stage 2', 'Room A'],[[0.8, 0.5],[0.5, 0.7]],[[0.9, 0.3, 0, 0.6],[0.2, 0.6, 0.1, 0.6]],[[0.8, 0.3],[0.4, 0.7]])
        test.greedy_alg()