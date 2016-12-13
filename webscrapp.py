def readURL():
    from lxml import html
    import requests

    page = requests.get('https://support.intershop.com/kb/index.php/Display/255S96')
    tree = html.fromstring(page.content)
    #test = tree.xpath("//div[@class='innerCell']/*/text()")
    test = tree.xpath("//p/text()")
    text = str(test)
    #text = removeFormatting(text)
    writeToFile(text)

    
def writeToFile(text):
    f = open('IStestfile.txt','a+')
    f.write(text)
    f.close()
def removeFormatting(text):
    
    t = text.replace("\\n","")
    t = t.replace("\\","")
    return t

readURL()

'''
test = "asd \nasd"
t = test.replace("\n"," ")
print (t)


    f = open('testfile.txt','w+')
    t = f.readline()
    print (t)



    f = open('IStestfile.txt','r+')
>>> text = f.read()
>>> text = text.replace('none',"")
>>> f.write(text)
'''


