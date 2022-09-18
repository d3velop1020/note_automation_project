# new main version of this project
# part one: points with indentation
# part two: un-nested tag sorting
# part three: make it so it takes a properly formatted txt file and a returns a formatted txt.file
# workflow is you load in a text file called text_in

##-----------Starting with file IO---------------##
# open the file (
fIn = open('text_in.txt')
fileText = []
# intialize a file for output
fOut = open('output.txt','w')
for line in fIn:
    lineStripped = line.strip() # the lines must be stripped to get rid of the /n after every line
                                #... even a empty line will just have /n
                                #... if you don't strip it,an enter line will show up as a double enter
    print(lineStripped)
    fileText.append(lineStripped)
print('file text =')
print(fileText) # a list of strings
#use the string method .split() to remove the \n sequence from each line




##------------Begin Part One-------------------##
# use a test script until file i/o is set up
testScript = """
01 a list is a <def> sequence:  <.def.> 
02 <def> I call comma separated items in a list items, and if items have items, the smallest building blocks of a list are called elements.
<.def.>
03 <syn> the simplest way to make a new list is to enclose the items in square brackets: myList = [10,20,30]
<.syn.>
the items in a list don't have to be the same type

04 <def> a list inside a list is called: nested <.def.>

05 <syn> use myList[0] = 'hello world' to access the first item of a list <.syn.>

06 <syn> recall negative indices, where [-1] is the index of the final item <.syn.>

07 indices can be expressions myList[i+i] , where i = 1

08 <syn> range function: range(5): returns a range object: an interable sequence of indices from 0 to n-1 <.syn.> 
to traverse and read the elements is the in operator, to write or update elements use indices

09 hello
010 world
011 this point has three digits
010
01.01 point with one dot
01.01.01 point with two dots
"""

##-------------------Variables for part two-----------------------##
openTags = {'definitionOpen': '<def>',
            'exampleOpen': '<ex>',
            'questionOpen': '<qst>',
            'starOpen': '<star>',
            'syntaxOpen': '<syn>',
             }

closeTags = {
            'definitionClose': '<.def.>',
            'exampleClose': '<.ex.>',
            'questionClose': '<.qst.>',
            'starClose': '<.star.>',
            'syntaxclose': '<.syn.>',
             }


 ##------------------functions for part one throughout------------------------------##

# take a list of all lines in, filter out all lines that don't start with a point indicator
# fileText is the argument to be passed in
def selectPoints(stringList):
    pointList = []
    for i in stringList:
        if len(i) > 0 :
            if i[0] == '0':
                pointList.append(i)
    return pointList


# pass in a word and get a dotCount
def dotCounter(wordIn):
    #used inside of writeFile()
    dotCount = 0
    for letter in wordIn:
        if letter == '.':
            dotCount += 1
    return dotCount



def writePointsToFile(pointList):
# take a point list in,
# count the dots for the 1st word of the string entries
# write to a text file
    for i in pointList: # recall points are strings we want to isolate the first word
        iSplit = i.split()
        dotCount = dotCounter(iSplit[0])
        fOut.write('    ' * dotCount + i + "\n") # go with a four space indent, very pythonic




#---------------functions for part two------------------------##

# we want to be able to obtain turn a list into a single string
# we need to go to each line and each word and append it to a list

# start it not as a function

def listOfLinesToListOfWords(listOfStrings): # each line of a text is a string
    listOfWords = []
    for i in listOfStrings:
        iWords = i.split()
        for word in iWords:
            listOfWords.append(word)
    #print('List of words = ')
    #print(listOfWords)
    return listOfWords
#fileWordsString = ' '.join(fileText)


def organizeByTag(listOfWords):
    writeWord = False
    tagFormatList01 = [] #end goal is a list where each entry is a string from open tag to close tag

    for word in listOfWords:
        if word in openTags.values():
            writeWord = True
            tagFormatList01.append(word)

        elif word in closeTags.values():
            tagFormatList01.append(word)
            writeWord = False
            tagFormatList01.append('--') # newline delimiter for later

        elif writeWord == True: # this elif captures the words between the tags
            tagFormatList01.append(word)
    print('tagFormatList01 = ')
    del tagFormatList01[-1]
    #print(tagFormatList01)
    tagFormatList02 = ' '.join(tagFormatList01)

    print('tagFormatList02 = ')
    print(tagFormatList02)

    tagFormatList03 = tagFormatList02.split('--')
    print('tagFormatList03 = ')
    print(tagFormatList03)

    return tagFormatList03


def fileWriteByTag(format03TagList):
    defList = []
    synList = []
    qstList = []
    starList = []
    exList = []

    for j in format03TagList: # search strings for substrings
        if '<def>' in j:
            defList.append(j)
        elif '<syn>' in j:
            synList.append(j)
        elif '<ex>' in j:
            exList.append(j)
        elif '<star>' in j:
            starList.append(j)
        elif '<qst>' in j:
            qstList.append(j)

    # write to file by tag type:
    fOut.write('\n')
    fOut.write('======= Tagged Text =========\n')
    fOut.write('\n')
    fOut.write(' Definitions\n')
    for i in defList:
        fOut.write(str(i) + '\n')
    for i in synList:
        fOut.write(str(i) + '\n')
    for i in starList:
        fOut.write(str(i) + '\n')
    for i in qstList:
        fOut.write(str(i) + '\n')
    for i in exList:
        fOut.write(str(i) + '\n')







##--------------function calls for part one-------------------##
pointList = selectPoints(fileText)
print('point list = ')
print(pointList)

# call the point printer function
writePointsToFile(pointList)



##---------------function calls for part two-------------------##
fileTextWords = listOfLinesToListOfWords(fileText)
print('fileTextWords = ')
print(fileTextWords)

formatted03List = organizeByTag(fileTextWords)

fileWriteByTag(formatted03List)


# close the file:
fOut.close