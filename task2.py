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

#############################################################################
'''
0. loop n - 1 times
1. start with 0 and 1 -> [0,1]
2. duplicate and flip -> [0,1] [1,0]
3. append a zero for list one -> [00,10]
4. append a one for list two -> [11,01]
5. append list two to list one -> [00,10,11,01]
6. repeat from step 2
'''
n = 0
while n < 2 or n > 10:
    n = int(input("how many elements (2 - 10): "))
    if n < 2 or n > 10:
        if n % 2 == 0:
            print ("PLEASE FOLLOW THE RULES")
            print ('\n')
        else:
            print ("RULES ARE SET FOR A REASON")
            print ('\n')
        time.sleep(1)

        
carty = ['1','0']   # list one
carter = []         # list two

for x in range(n - 1):
    carter = []
    # duplicate and flip
    for i in range(len(carty)-1, -1, -1):
        carter.append(carty[i])

    # append 0 for list one
    for i in range(len(carty)):
        thing = carty[i]
        thing = thing + '0'
        carty[i] = thing

    # append 1 for list two
    for i in range(len(carter)):
        thang = carter[i]
        thang = thang + '1'
        carter[i] = thang

    # join list 2 to list 1
    for i in range(len(carter)):
        carty.append(carter[i])



letters = obtainLetters(n)


'''
the positions of 1 corresponds to which letter to take
eg:
number 101 corresponds to {A,C}
'''
final = []
for i in range(len(carty)):
    item = carty[i]
    subset = ''
    for j in range(len(item)):
        if item[j] == '1':
            subset = subset + letters[j]
    final.append(subset)


# writefile
for i in range(len(final)):
    line = 'subset'.ljust(7) + str(i+1).rjust(2) + ': {' + final[i] + '}'
    writefile("outputTask2.txt", line)


print('done')





