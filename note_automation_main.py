# overview:
    # in part one we are generating a list of all the points (lines that begin with 0)...
    #... and sorting the points with a heirarchy were subpoints are listed
    #... with a 4 space indent from their parent point

    # in part two we are concerned with the tags
    # for part two we need to isolate all the words and run an algorithm to sort info by tags
    # hopefully we can get nested tags working in a reasonable amount of time.


#enter a testScript and tag dictionaries

testScript = """
01 a list is a <def> sequence:  <.def.> 
02 <def> I call comma seperated items in a list items, and if items have items, the smallest building blocks of a list are called elements.
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

0101 keep coding...end

"""
# tag dictionaries
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

# Q: How do you count lines of a multi-line string?
# Answering the question: use string.splitlines() to separate the string into a list of lines...
# ... then you use len() function on list of lines


def selectPoints(lineListIn):
    # take in a list of lines that are strings
    # return a list of all the lines / strings that begin with '0'
    linesWithStartingZeros = []
    for i in lineListIn:
        if len(i) > 0:
            if i[0] == '0':
                linesWithStartingZeros.append(i)
                # return a list with entries of all lines that start with a numeric code (points)
    return linesWithStartingZeros # return a list of strings that start with 0 (called points)


# def isSubPoint(lineIn):
#     wordsIn = lineIn.split()
#     print(lineIn)
#     print("number of digits of point-code =")
#     print(len(wordsIn[0]))

# we made a new function, let's test is on list of points (mainPointsList)

# decision for sub-points, all I need to do is count the dots..
# ...it makes it feel kinda like bullet-points


def dotCounter(wordIn):
    #used inside of writeDemo
    dotCount = 0
    for letter in wordIn:
        if letter == '.':
            dotCount += 1
    return dotCount


def writeDemo(listOfPointStrings):
    #the goal of this is to write points to the left and sub-points indented the appropriate amount
    #take in a list of (string) points as input
    for i in listOfPointStrings:
        currentLine = i
        currentWords = currentLine.split() # a list of words from the current line
        currentPointCode = currentWords[0] # the code is the first item in the current words list
        currentDotCount = dotCounter(currentPointCode)
        if currentDotCount == 0:
            print(i)
        elif currentDotCount > 0:
            print('    ' * currentDotCount + i)

# ----------------------------------part one: running code----------------------------------------#=

# here we are verifying we can split a multi-line string into a list of lines
testSplit = testScript.splitlines()
# for i in testSplit:
#     print(i)

# call the select points (returns a list of every line that starts with 0)
# ... function and pass in the note-txt-like-string (aka testString) ...
# ... this returns a list with all the lines that are points as entries
pointsList = selectPoints(testSplit)
# call the writeDemo function on the pointsList
writeDemo(pointsList)

# -------------------------part two dealing with adding hyper markups

# now start writing something to process testScript...word by word
print('=====================Begin part two==============')

def stringToLineList(stringIn):
    #functionizing the splitlines() method
    lineListFromString = stringIn.splitlines()
    return lineListFromString


def lineListToWordList(lineListIn):
    # returns a list of words that was converted from an input list of lines,
    # ... using space as delimiter
    wordListOut = []
    for i in lineListIn:
        if len(i) > 0:
            currentLine = i
            currentLineWordList = currentLine.split()
            # print('currentLineWordList = ')
            # print(currentLineWordList)
            for word in currentLineWordList:
                wordListOut.append(word)
    return wordListOut


testScriptLineList = stringToLineList(testScript)

# demo to print out each individual line from the original multi-line  test string
for i in testScriptLineList:
    print(i)

# call the lineListToWordListFunction to obtain a list of all words
testScriptWordList = lineListToWordList(testScriptLineList)

print(testScriptWordList)

# now we have one list with all the words

# to start the code go through until you find an open tag
print('output from sorter tool')


def tagSorter(wordListIn):
    for word in wordListIn:
        if word in openTags.values():
            print(word)

