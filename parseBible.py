#parse bible
def writeToFile(text):
    f = open('parsedBible.txt','w+')
    f.write(text)
    f.close()
def removeFormatting(text):    
    t = text.replace("\\n","")
    t = t.replace("\\","")
    return t
parsedBible = []
with open('bible.txt', 'r') as openfileobject:
    for line in openfileobject:
        global parsedBible
        x = line.split("\t")
        parsedBible.append(x[1])
writeToFile(removeFormatting(str(parsedBible)))

    
        
