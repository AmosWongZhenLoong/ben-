smallPaths = [[0,1,2,4,0],[1,3,6,4,1],[2,5,2],[3,7,6,5,3]]
finalPath = []

for i in range(len(smallPaths[0])):
    finalPath.append(smallPaths[0][i])
del smallPaths[0]

while len(smallPaths) != 0:
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
    finalPath = []
    for i in range(len(leftSplit)):
        finalPath.append(leftSplit[i])
    for i in range(len(smallPaths[0])):
        finalPath.append(smallPaths[0][i])
    for i in range(len(rightSplit)):
        finalPath.append(rightSplit[i])
        
    del smallPaths[0]
    
print(finalPath)
