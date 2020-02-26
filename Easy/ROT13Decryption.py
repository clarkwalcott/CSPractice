# encodes the input "message" in ROT13
# https://en.wikipedia.org/wiki/ROT13
# Problem Credit: codewars.com

def rot13(message):
    newMessage = []
    for c in list(message):
        if c.isalpha():
            if c.islower():
                newMessage.append(chr(((ord(c)-84) % 26) + 97))
            else:
                newMessage.append(chr(((ord(c)-78) % 26) + 65))
        else:
            newMessage.append(c)
    return "".join(newMessage)