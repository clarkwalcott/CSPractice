# letters.py
# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
# Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
# Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 
# Problem Credits: Coderbyte.com

def LetterChanges(str): 
    newString = [chr(ord(x)+1) if x.isalpha() else x for x in list(str)]
    newString2 = [x.upper() if x in {'a', 'e', 'i', 'o', 'u'} else x for x in newString]
    # code goes here 
    return "".join(newString2)
    
# keep this function call here  
print LetterChanges(raw_input())