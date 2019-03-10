# Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an 
# acceptable sequence by either returning the string true or false. The str parameter will be composed of
# + and = symbols with several letters between them (ie. ++d+===+c++==a) and for the string to be true each 
# letter must be surrounded by a + symbol. So the string to the left would be false. 
# The string will not be empty and will have at least one letter. 
# Problem Credit: Coderbyte.com

def SimpleSymbols(str): 
    symbols = list(str)
    for x in range(len(symbols)):
        if (symbols[x] is not "+") and (symbols[x].isalpha()):
            if(x==0) or (x==len(symbols)-1): return "false"
            if(symbols[x-1] is not "+") or (symbols[x+1] is not "+"): return "false"
    return "true"

print SimpleSymbols(raw_input())