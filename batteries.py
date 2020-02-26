import queue

# Problem: You are working a children's toy drive and are tasked with obtaining enough 
# batteries to power the pile of toys in front of you. Batteries in your town are sold
# in packs of 6, 9, and 20. Write an algorithm that will allow you to determine all possible
# combinations of battery packs that will give you exactly N batteries.

class Tree(object):
    def __init__(self):
        self.children = []
        self.data = None


# \param N the total batteries
def getPacks(packTypes, N):
    packTypes.sort(reverse=True)
    root = buildTree(packTypes, N)
    printTree(root)

# Consider changing Tree class to Node class. Include parent, depth, etc.
def buildTree(packTypes, N):
    root = Tree()
    root.data = (0,0)
    for _ in range(int(N/packTypes[0])+1):
            tree = Tree()
            tree.data = (packTypes[0], _)
            root.children.append(tree)
    for child in root.children:
        rem = N - (child.data[0]*child.data[1])
        for _ in range(int(rem/packTypes[1])+1):
            tree = Tree()
            tree.data = (packTypes[1], _)
            child.children.append(tree)
    for child in root.children:
        for ch in child.children:
            rem = N - (child.data[0]*child.data[1]) - (ch.data[0]*ch.data[1])
            for _ in range(int(rem/packTypes[2])+1):
                tree = Tree()
                tree.data = (packTypes[2], _)
                ch.children.append(tree)
    return root

def printTree(root):
    for child in root.children:
        print(child.data)
        for ch in child.children:
            print(ch.data)
            for c in ch.children:
                print(c.data, end="")
            print()
        print()

def main():
    getPacks([6,9,20], 60)

if __name__ == '__main__':
    main()