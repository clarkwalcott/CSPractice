# Have the function LetterCapitalize(str) take the str parameter being passed 
# 	and capitalize the first letter of each word. 
# Words will be separated by only one space. 
# Problem Credit: Coderbyte.com

def LetterCapitalize(str): 
    return " ".join([x.capitalize() for x in str.split(" ")])
    
# keep this function call here  
print LetterCapitalize(raw_input())