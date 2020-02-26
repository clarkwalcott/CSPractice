import queue

# CURRENTLY ONLY RETURNS THE FIRST SOLUTION FOUND

# Problem: You are working a children's toy drive and are tasked with obtaining enough 
# batteries to power the pile of toys in front of you. Batteries in your town are sold
# in packs of 6, 9, and 20. Write an algorithm that will allow you to determine all possible
# combinations of battery packs that will give you exactly N batteries.

class CSP():
    def __init__(self, variables, constraints):
        self.variables = variables
        self.constraints = constraints
        self.domains = {}
        for var in variables:
            self.domains[var] = [i for i in range((constraints//var)+1)]

# \param N the total batteries
def getPacks(packTypes, N):
    packTypes.sort(reverse=True)
    root = CSP(packTypes, N)
    print(root.domains)
    result = backtracking_search(root)
    #print(result)

# Runs backtracking search over the csp
# \param csp the csp object containing the problem
# \param assignment the current assignment of variables in the csp
# \return the assigment after checking for consistency, otherwise None
def backtracking_search(csp, assignment = {}):
    if len(assignment) == len(csp.variables):
        return assignment
    unassigned = [var for var in csp.variables if var not in assignment]
    for domain in csp.domains[unassigned[0]]:
        assign_copy = assignment.copy()
        assign_copy[unassigned[0]] = domain
        c = is_consistent(unassigned[0], assign_copy, csp)
        if c == -1:
            continue
        elif c == 1:
            result = backtracking_search(csp, assign_copy)
            if result != None:
                return result
    return None

# \param variable the variable to check against the given assignment
# \param assignment the assignment to check against
# \param csp the given problem
def is_consistent(variable, assignment, csp):  
    if(len(assignment) < 3):
        return 1
    sum = 0
    for i, var in enumerate(assignment):
        sum += assignment[var]*csp.variables[i]
    if sum > csp.constraints or sum < csp.constraints:
        return -1
    return 1

def main():
    getPacks([6,9,20], 60)

if __name__ == '__main__':
    main()