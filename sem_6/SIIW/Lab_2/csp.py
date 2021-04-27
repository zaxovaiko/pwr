import copy
import time
import json


class Constraint:
    def __init__(self, vars, isValid):
        self.vars = vars
        self.isValid = isValid


    def __str__(self):
        return str(self.vars)


class CSP:
    def __init__(self, vars, doms, cons, heur=None):
        self.vars = vars
        self.doms = doms
        self.cons = cons
        self.heur = heur
        self.key = list(self.doms.keys())
        self.counter = 0
        self.sols = []


    def __str__(self):
        return ' '.join([str(x) for x in self.doms.values()])


    # Check if entire solution is correct
    def is_complete(self, csp) -> bool:
        for con in self.cons:
            if not con.isValid(self.doms): return False
        return True


    # Check constraints only for current variable
    def check_constraints(self, var) -> bool:
        isValid = True
        for con in list(filter(lambda x: var in x.vars, self.cons)):
            if not all(self.doms[v] for v in con.vars): continue
            if not con.isValid(self.doms): isValid = False
        return isValid


    def ac3_helper(self, x, y):
        revised = False
        cons = [con for con in self.constraints if con[0] == x and con[1] == y]

        for x_value in self.doms[x]:
            satisfies = False
            for y_value in self.doms[y]:
                for con in cons:
                    constraint_func = self.constraints[con]
                    if constraint_func(self.doms): satisfies = True
            if not satisfies:
                self.doms[x].remove(x_value)
                revised = True

        return revised


    def solve_ac3(self):
        '''
        Check time performance for AC3 algorithm.
        Prepare data arcs and constraints
        '''
        self.arcs = list(map(lambda x: tuple(x.vars), self.cons))
        self.constraints = { tuple(con.vars): con.isValid for con in self.cons }

        self.counter = 0
        t0 = time.time()
        self.ac3()
        print('Time execution: ', time.time() - t0)
        print('Counter: ', self.counter)


    def ac3(self):
        '''
        AC3 algorithm.
        For each constraint checks domains of all variables and remove incosistent.
        '''
        q = self.arcs[:]
        while q:
            self.counter += 1
            (x, y) = q.pop(0)
            if self.ac3_helper(x, y):
                neighbors = [nei for nei in self.arcs if nei[1] == x]
                q += neighbors
        self.sols = [copy.deepcopy(self.doms)]


    def forward_checking(self, v=0):
        '''
        Back Tracking algorithm with forward checking.
        Before moving on checks constraints for current and future variable and it's domains.
        link: https://ktiml.mff.cuni.cz/~bartak/constraints/propagation.html
        '''
        self.counter += 1

        if v == len(self.doms.keys()) - 1:
            if self.is_complete(self):
                self.sols.append(copy.deepcopy(self.doms))
                return True
            return False
        
        for dom in self.vars:
            self.doms[self.key[v]] = [dom]
            
            # for con in list(filter(lambda x: self.key[v] in x.vars and self.key[v + 1] in x.vars, self.cons)):
            #     for i in self.doms[self.key[v + 1]]:
            #         if not con.isValid(self.doms):
            #             self.doms[self.key[v + 1]].remove(i)

            if dom in self.doms[self.key[v + 1]]:
                self.doms[self.key[v + 1]].remove(dom)

            if v < len(self.doms.keys()) - 1 and len(self.doms[self.key[v + 1]]) == 0:
                self.doms[self.key[v + 1]] = list(self.vars)
                # ... if the domain of a future variable becomes empty, it is known immediately that the current partial solution is inconsistent
                return False

            if not self.check_constraints(self.key[v]): 
                self.doms[self.key[v]] = list(self.vars)
                continue

            self.forward_checking(v + 1)

            self.doms[self.key[v]] = list(self.vars)
            self.doms[self.key[v + 1]] = list(self.vars)


    def solve_forward_checking(self) -> None:
        '''
        Check time performance for forward checking algorithm.
        '''
        self.counter = 0
        self.sols = []
        t0 = time.time()
        self.forward_checking()
        print('Time execution: ', time.time() - t0)
        print('Counter: ', self.counter)


    def solve_backtracking(self) -> None:
        '''
        Check time performance for backtracking algorithm.
        '''
        self.counter = 0
        self.sols = []
        t0 = time.time()
        self.rbt()
        print('Time execution: ', time.time() - t0)
        print('Counter: ', self.counter)


    def rbt(self, v=0) -> bool:
        '''
        Backtracking algorithm.
        Before moving on checks constraints for current variable and it's domains.
        Get solutions from the end (cuz of recursion)
        '''
        self.counter += 1

        if v == len(self.doms.keys()):
            if self.is_complete(self):
                self.sols.append(copy.deepcopy(self.doms))
                return True
            return False

        domains = self.heur(self.key[v], self.doms, self.vars) if self.heur else self.vars
        
        for dom in domains:
            self.doms[self.key[v]] = [dom]

            if not self.check_constraints(self.key[v]): continue

            self.rbt(v + 1)
            self.doms[self.key[v]] = list(self.vars)