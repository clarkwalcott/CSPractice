# Purpose: Display a list of numbers 1 to n. If a number is divisible by 3, output "Fizz". If a number is divisible by 5, 
# output "Buzz". Finally, if a number is divisible by both 3 and 5, output "FizzBuzz".

def fizzbuzz(n):
    numList = list()
    myDict = {3:"Fizz", 5:"Buzz"}
    for i in range(1,n+1):
        numString = ""
        for key in myDict.keys():
            if i % key == 0:
                numString += myDict.get(key)
        numList.append(i) if numString == "" else numList.append(numString)
    print(numList)

fizzbuzz(100)
