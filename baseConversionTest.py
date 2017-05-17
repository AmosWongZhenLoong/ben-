
def baseConversion(number, base):
    """
    converts the integer (base10) into another base (baseX) which is defined by
    the user
    arg number: the base10 integer to be converted
    arg base: the base that the integer should be converted to
    return: the resulting number in its new base form **AS A STRING**
    complexity: O(log base (number)) where base is the log's base
    """
    result = ''
    if number < base:
        return number
    while True:
        remainder = number % base
        number = (number // base)
        result = str(remainder) + result
        if number < base:
            break

    return (str(number) + result)


def testModule(n, base):
    for i in range(n):
        print (str(i).ljust(10) + str(baseConversion(i,base)))
    print ('\n')



testModule(20, 2)
testModule(20, 3)
