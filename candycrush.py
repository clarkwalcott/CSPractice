# Implements the remove groups method from a candy crush like game
# \param candyList a list where each element is a number representing a type of candy
# \return the remaining list after groups of 3 or more have been removed
# e.g. [1,2,3,3,3,2,2,2,1]
def removeCandy(candyList):
    currentCandy = 0; candyCount = 1; startIndex = 0
    for c in range(len(candyList)):
        if candyList[c] != currentCandy:
            currentCandy = candyList[c]
            startIndex = c
        else:
            candyCount += 1
        if candyCount >= 3:
            if candyList[c+1] == currentCandy:
                continue
            for i in range(candyCount):
                candyList.pop(startIndex)
            return removeCandy(candyList)
    return candyList

print(removeCandy([1,2,3,3,3,2,2,2,1]))

# Implement with a stack (push on pairs of numbers and counts)

# Stack: (1,1), (2,1), (3,1..2..3) remove this pair and add 1 to the 2 pair before it