database = [[0, 'AAA', 'N'], [1, 'AAB', 'N'], [2, 'ABA', 'N'], [3, 'ABB', 'N'], [4, 'BAA', 'N'], [5, 'BAB', 'N'], [6, 'BBA', 'N'], [7, 'BBB', 'N']]

adjacencyCart = [[1],[2,3],[4,5],[6,7],[0,1],[2,3],[4,5],[6]]

#BFS
regularCart = []
queue = []
currentThing = database[0][1]
endFound = False

queue.append(database[0][0])

firstRound = True
while endFound == False:

    queueServe = queue.pop(0)
    regularCart.append(queueServe)
    #database[queueServe][2] = 'Y'

##    if firstRound == False:
##        if queueServe == 0:
##            endFound = True
##            print ("found the end point")
##            break

    for i in range(len(adjacencyCart[queueServe])):
        for j in range(len(adjacencyCart[queueServe])):
            if database[adjacencyCart[queueServe][j]][2] == "N":
                queue.append(database[adjacencyCart[queueServe][j]][0])
                database[adjacencyCart[queueServe][j]][2] = "Y"
    firstRound = False
    print (queue)
    print (regularCart)
    if len(queue) == 0:
        break
