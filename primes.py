from typing import List

# Returns list of primes between 2 and n. Uses the Seive of Eratosthenes
def primes(myList: List[bool])-> List[int]:
    n = int(len(myList))
    p = 2   # p is initialized to the first prime number
    while(p**2 < n):
        if(myList[p] == True):
            for i in range(2*p, n, p):
                myList[i] = False
        p += 1
    return [i for i, val in enumerate(myList) if val]

def generateList(n):
    return [True if x > 1 else False for x in range(n+1)]

def main():
    myList = generateList(100)
    primeList = primes(myList)
    print(primeList)

if __name__ == "__main__":
    main()