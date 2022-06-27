import xml.etree.ElementTree as ET
#import pyaudio
from nltk.tokenize import sent_tokenize, word_tokenize
#import morfeusz2
import io
#from stempel import StempelStemmer

stopwords = []
commands = []
home = None
root = None
#stemmer = StempelStemmer.polimorf()

def getPathToObj(obj):
    #doesnt work
    if obj == None or obj == root:
        return ""
    return getPathToObj(obj.find("..")) +"/"+ obj.tag

def loadStopWords():
    out = []
    f = io.open("resources/polish_stopwords", "r", encoding="utf-8")
    for line in f:
        for word in line.split():
            out.append(word)
    return out


def loadExampleCommands():
    out = []
    f = io.open("resources/example_commands", "r", encoding="utf-8")
    for line in f:
        out.append(line)
    return out


def getFilteredWords(words):
    global stopwords
    out = []
    for w in words:
        for st in stopwords:
            if w == st:
                # print("in stopwords",w)
                break
        else:
            # print(w,"not in stops",w not in stopwords,stopwords)
            out.append(w)
    return out


def load():
    return ET.parse('home.xml')


def printChildren(r, recursion_step=0, recurse=True):
    for c in r:
        print("  " * recursion_step, c.tag, c.attrib)
        if recurse:
            printChildren(c, recursion_step + 1)


def isON(a):
    _o = a.get("set", None)
    if (_o == None):
        print("Component ", a, " does not have set option.")
        return -1
    if (_o == "on"):
        return True
    if (_o == "off"):
        return False
    print("Component ", a, " is set incorrectly as:", _o)
    return -1


def switch_device(a):
    if a.get("set", None) == None:
        return False

    if isON(a):
        a.attrib["set"] = "off"
    else:
        a.attrib["set"] = "on"
    home.write("home.xml")
    return True


polecenia = [
    ["switch", "przelacz", "przełącz", "przełacz"],
    ["włącz", "włacz", "wlacz","załącz","zaświeć","zaświecić","zapal"],
    ["wyłącz", "wylacz", "wyłacz","zgaś","zgas"]
]

struktura = [
    [0,"parter","parterze","zerowym","zero"],
    [1,"pierwsze", "pierwszym"],
    [2,"drugie", "drugim"],
    [3,"trzecie", "trzecim"],
    ["garaz", "garażu", "garazu"]
]

pokoje = [
    ["kuchnia", "kuchni"],
    ["korytarz", "korytarzu"],
    ["biuro", "biurze"],
    ["sypialnia", "sypialni"],
    ["pokoj", "pokój", "pokoju"],
    ["garderoba", "garderobie"],
    ["lazienka", "łazience", "lazience", "łazience"],
]
"""
struktura = [
    ["dom", "domu"],
    ["pietro", "pietrze", "piętrze"],
    ["parter", "parterze"],
]"""
urzadzenia = [
    ["czajnik"],
    ["lampa", "lampe", "lampę","światło","światła"],
    ["telewizor", "telewizje"],
    ["komputer"],
    ["drzwi"]
]

keywords = [struktura, pokoje, urzadzenia]


def asystent(pytanie):
    words = word_tokenize(pytanie, "polish")
    for i in range(len(words)):
        words[i] = words[i].lower()
    filteredwords = getFilteredWords(words)
    words = filteredwords
    print("tokenized", words)
    action = -1

    for l_action in range(len(polecenia)):
        for alias in polecenia[l_action]:
            if alias in words:
                action = l_action
                words.remove(alias)
                break
        if action != -1:
            break

    if action == -1:
        return False
    print("choosen mode", polecenia[action])

    node_struktura = None
    #node_liczby = None
    node_pokoj = None
    node_urzadzenie = None

    matched = [node_struktura, node_pokoj, node_urzadzenie]

    # stemming works funky ... :(
    # for w in words:
    #   print(stemmer.stem(w))

    def analiseWord(word):
        if None in matched:
            for cat_id, category in enumerate(keywords):
                if matched[cat_id] is None:
                    for cat_keywords in category:
                        for alias_ in cat_keywords:
                            if alias_ == w.lower():
                                matched[cat_id] = cat_keywords[0]
                                return True

    for w in words:
        analiseWord(w)

    print(matched)
    def find():
        _path = ""
        if matched[0] == None:
            _path +="*"
        else:
            if type(matched[0]) == type(1):
                _path += "pietro[@poziom=\'" + str(matched[0])+"\']"
            else:
                _path += "garaz"

        for i in [1,2]:
            _path += "/"

            if matched[i] == None:
                _path+="*"
            else:
                _path+=matched[i]
        return _path

    path = find()
    found = root.findall(path)

    print("found:",found)

    def execute():
        for f in found:
            if action == 0:
                switch_device(f)
            elif action == 1:
                if not isON(f):
                    switch_device(f)

            elif action == 2:
                if isON(f):
                    switch_device(f)

    if  len(found) == 0:
        print("something went wrong, I didnt find anything at location ",path, "\n try again please")
        return False
    else:
        print("do you confirm command? ")
        print(action," on...")
        print(path)
        print(found)
        #for f in found:
            #print(getPathToObj(f))
        while True:
            answ = input("Is that correct? [Y]/[N]")
            if answ.lower() == 'y':
                execute()
                return True
            elif answ.lower() == 'n':
                return False
            else:
                print("wrong answer...")

def init():
    global stopwords
    global commands
    global home
    global root

    print("Start")
    home = load()
    root = home.getroot()
    stopwords = loadStopWords()
    #print(stopwords)
    commands = loadExampleCommands()

init()