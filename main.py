from lxml import html
from lxml import etree
from formatting import *



import requests

def getListFromFile(filePath):
    f = open(filePath, "r")
    list = []
    for line in f:
        list.append(line)
    f.close()
    return list
def listToListOfLinks(list, lang):
    linkList = []
    for word in list:
        word = word.replace('\n','').replace('\r','')
        link = "https://en.wiktionary.org/wiki/" + word + "/#" + lang
        linkList.append(link)
        #print(link)
    return linkList

def makeCSV(words, definition):
    #file = open("saveFile2", "w")
    x = len(words)
    for y in range(0,x):
        try:
            thing = words[y] + " : "
        except IndexError:
            thing = "ERROR :"
        try:
            defThing = definition[y] + "  ***"
        except IndexError:
            defThing = " ERROR ***"
        print(thing + defThing)
        #print(words[y] + " : " + definition[y])
        #file.write(words[y] + " : " + definition[y])
        #file.write(words[y].replace('\n','').replace('\r','') + " : " + definition[y].replace('\n','').replace('\r','') + "\n")
    #file.close()
    return 0


#
def getFullEntry(link):

    page = requests.get(link)
    tree = html.fromstring(page.content)
    word = tree.xpath('//p[strong/@lang = "la"]')
    definitions = tree.xpath('//p[strong/@lang="la"]/following-sibling::ol[1]')
    try:
        wordEntry = word[0].text_content()
    except IndexError:
        print("ERROR ERROR ERROR WORD error")
        print(link)
        wordEntry = "This word has been problematic, here's the link;" + link


    try:
        defEntry = definitions[0].text_content()
    except IndexError:
        print("ERROR ERROR ERROR DEF error")
        print(link)
        defEntry = "This definition ran into a problem, here's the link; " + link

    return cardFormat(wordEntry, defEntry)


def main():
    lang = "Latin"
    file = "section09.txt"
    cardList = []


    try:
        f = open(file, "r")
    except FileNotFoundError:
        print("Sorry, file not found!")
    for line in f:
        url = urlFormat(line, lang)
        card = getFullEntry(url)
        print(card)
        cardList.append(card)



    return 0

main()





