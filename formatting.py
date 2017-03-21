def urlFormat(word, lang):
    word = word.replace('\n','').replace('\r','')
    return "https://en.wiktionary.org/wiki/" + word + "#" + lang

def cardFormat(front, back):
    return front + " : " + back + "***"

