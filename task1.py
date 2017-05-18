import time
import math

def writefile(filename,line):
    """
    writes contents in the list to an existing file
    arg filename: the name of the file to write to
    complexity: O(1)              #PogChamp
    """
    file=open(filename,'a')         # 'a' for append mode
    file.write(line)
    file.write("\n")
    file.close()

def obtainLetters(mParam):
    """
    get the alphabets to be used
    arg mParam: mParam defines how many alphabets will be used
    var A: stores the ascii value for alphabet "A"
    returns: an array containing the first mParam alphabets
    """
    A = 65
    alphabets = []
    for i in range(mParam):
        alphabets.append(chr(A + i))
    return alphabets

def baseConversion(number, base, nParam):
    """
    converts the integer (base10) into another base (baseX) which is defined by
    the user
    arg number: the base10 integer to be converted
    arg base: the base that the integer should be converted to
    arg nParam: the length that the string should be
    return: the resulting number in its new base form **AS A STRING**
    complexity: O(log base (number) + (nParam - len(final))) where base is the log's base
    """
    result = ''
    if number < base:
        final = str(number)
        # pad zeroes in front so they are all the same length
        while len(final) < nParam:
            final = '0' + final
        return (final)
    while True:
        remainder = number % base
        number = (number // base)
        result = str(remainder) + result
        if number < base:
            break
    final = (str(number) + result)
    # pad zeroes in front so they are all the same length
    while len(final) < nParam:
        final = '0' + final
    return (final)

def nicePrint(cart):
    """
    prints the items in the array supplied
    to save two lines each time i wanna print
    arg cart: the array to be printed out
    complexity: O(n)
    """
    for i in range(len(cart)):
        print (cart[i])
    print('\n')

##############################################################################
####################### BETWEEN A ROCK AND A HARD PLACE ######################
##############################################################################


mParam = int(input("choose m (2 - 5): "))
nParam = int(input("choose n (2 - 3): "))
vertices = mParam ** nParam        # number of vertices

lettersToUse = obtainLetters(mParam)

'''
if for example theres two letters and eight vertices
the different combinations of letters can be represented by
000, 001, 010, 011, 100, 101, 110, 111
which is actually base-2 addition
'''
# generate all the base values (0 to vertices - 1)
database = []
for i in range(vertices):
    database.append(baseConversion(i, mParam, nParam))

# change them to letters
# and assign vertexes (which will also act like indices) to each of the perm
temp = []
for i in range(len(database)):
    item = database[i]
    word = ''
    for j in range(len(item)):
        word = word + lettersToUse[int(item[j])]
    temp.append(word)
    database[i] = temp
    database[i].insert(0, i)
    temp = []


# make an adjacency list
# note: directed graph
'''
what vertex is adjacent will be based on comparing the last n-1 letters of the
vertex with the first n-1 letters of other vertices
'''
adjacencyCart = []
temporary = []
for i in range(len(database)):
    endPart = database[i][1][0 - (nParam - 1):]
    for j in range(len(database)):
        if i != j:                      # dont want self edges
            startPart = database[j][1][:nParam - 1]
            if endPart == startPart:
                temporary.append(j)
    adjacencyCart.append(temporary)
    temporary = []


##########################################################################
############################# Carls Algorithm ############################
##########################################################################

'''
start: any vertex
steps: travel unvisited edges until back to start (one cycle)
check: unvisited edges?
    yea: take vertex from path that has unvisited edges, then repeat from steps
    nay: merge all the cycles that we have, then end algorithm
'''

nextLocation = 0        # current location in the graph
cycles = []             # completed cycles store here, merge at the end
currentPath = []

emptyCart = False
branchFound = False

while True:
    currentPath.append(nextLocation)
    while True:
        location = nextLocation
        nextLocation = adjacencyCart[location][0]
        currentPath.append(nextLocation)
        del adjacencyCart[location][0]
        if currentPath[0] == currentPath[-1] and len(currentPath) > 1:
            break

    # finding the next branch to continue the search
    for i in range(len(adjacencyCart)):
        if len(adjacencyCart[i]) != 0:
            nextLocation = i
            branchFound = True
            break

    cycles.append(currentPath)

    # if adjacency list is empty, stop the loop
    if branchFound == False:
        break
    
    currentPath = []
    branchFound = False
    

#############################################################################
###################### Combine all the cycles into one ######################
#############################################################################

finalPath = []

# first list goes straight into finalPath
for i in range(len(cycles[0])):
    finalPath.append(cycles[0][i])


# the rest gets inserted into respective positions
for i in range(1, len(cycles)):
    theItem = cycles[i][0]
    for j in range(len(finalPath)):
        if finalPath[j] == theItem:
            for k in range(1, len(cycles[i])):
                finalPath.insert(j+k, cycles[i][k])
            break
    

# change to letters
# first vertex takes all letters
# subsequent vertexes takes only the last letter
finalString = ''
finalString = finalString + (database[finalPath[0]][1])

for i in range(1, len(finalPath)):
    finalString = finalString + database[finalPath[i]][1][-1]

print (finalString)

# write to file
line = finalString
writefile("outputTask1.txt", line)

print('write complete')





