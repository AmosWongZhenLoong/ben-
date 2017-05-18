smallPaths = [[0,1,2,4,0],[1,3,6,4,1],[2,5,2],[3,7,6,5,3]]
finalPath = []

# first item goes straight into finalPath
# delete it afterwards
for i in range(len(smallPaths[0])):
    finalPath.append(smallPaths[0][i])
del smallPaths[0]

# loop until nothing left to loop
while len(smallPaths) != 0:
    # get first item
    # find its location in finalPath
    # split left portion and right portion (at the position of the item you found)
    leftSplit = []
    rightSplit = []
    frontItem = smallPaths[0][0]
    for j in range(len(finalPath)):
        if frontItem == finalPath[j]:
            leftSplit = finalPath[:j+1]
            rightSplit = finalPath[j+1:]
            break
    print (leftSplit)
    print (rightSplit)

    del smallPaths[0][0]

    # append left portion
    # append remaining stuff from first item of smallPaths
    # append right portion
    finalPath = []
    for i in range(len(leftSplit)):
        finalPath.append(leftSplit[i])
    for i in range(len(smallPaths[0])):
        finalPath.append(smallPaths[0][i])
    for i in range(len(rightSplit)):
        finalPath.append(rightSplit[i])

    # remember to delete so the rule of always taking the first item will ngam every loop
    # and also the rule for stopping the loop when it is empty
    del smallPaths[0]
    
print(finalPath)
