import re
def findword(fulltext):
    if type(fulltext) != str:
        raise "Type Error"
    result = re.findall(r'\b\w*at\b', fulltext)
    filtered = filter(threecharacters, result)
    return filtered

def threecharacters(word):
    if len(word) >  3:
        return True
    else:
        return False

file = open("Alice.txt", "r")
textfile = file.read()
result = findword(textfile)
print result
