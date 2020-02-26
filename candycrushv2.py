# Implements the remove groups method from a candy crush like game
# Implemented with a stack (push on pairs of numbers and counts)
# e.g. Stack: (1,1), (2,1), (3,1..2..3) remove this pair and add 1 to the 2 pair before it
# \param candyList a list where each element is a number representing a type of candy
# \return the remaining list after groups of 3 or more have been removed
# e.g. [1,2,3,3,3,2,2,2,1]
def removeCandy(candyList):
    if len(candyList) < 1: return []
    stack = [[candyList[0],1]]
    last = len(stack) - 1
    for candy in range(1, len(candyList)):
        if candyList[candy] == stack[last]:
            candyList[stack][1] += 1
        elif stack[last][1] >= 3:
            for i in range(stack[last][1]):
                candyList.remove(candyList[candy-stack[last][1]])
        else:
            stack.append([candyList[candy], 1])
    return candyList

print(removeCandy([1,2,3,3,3,2,2,2,1]))