def getTokens(text):
    return [word.lower().translate(None,string.punctuation) for word in word_tokenize(text)]

def containsName(tokens):
    for i in tokens:
        if i in firstNames or i in surnames:
            return True
    return False

def isDictionaryWord(word):
    if not wordnet.synsets(word):
        return False
    return True

def removeNames(names):
    return [name for name in names if not isDictionaryWord(name)]

def loadNames():
    firstNames = [line.strip('\n').strip(' ').lower() for line in open('firstNames.txt') if line != "\n"] #from census data
    #surnames contains duplicates, remove
    surnames = [line.strip('\n').strip(' ').lower() for line in open('surnamesdb.txt') if line != "\n"]
    return set(firstNames),set(surnames),len(firstNames),len(surnames)

firstNames,surnames,count,countS = loadNames()

def hasNegativeSent(text):
    #take in raw text, not tokens
    return nb_classifier.classify(word_features(text))

def hasOffensiveLang():
    return

def word_features(words):
    return dict([(word,True) for word in words])

def checkText(text):
    #Returns true if should post else false to remove
    tokens = getTokens(text)
    sent = classifier.classify(word_features(tokens))
    named = containsName(tokens)
    if named and sent == 'negative':
        return False
    return True