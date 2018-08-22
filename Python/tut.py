
def do_twice(f,val):
    f(val)
    f(val)



def print_msg(str):
    print(str)



def printBeam():
    print('+ - - - - ',end='')


def printSpace():
    print(' ',end='')

def printSlash():
    print('/         ',end='')

def doTwice(f):
    f()
    f()

def doFour(f):
    doTwice(f)
    doTwice(f)

def printBeams():
    doTwice(printBeam)
    print('+')

def printPost():
    doTwice(printSlash)
    print('/')

def printRow():
    printBeams()
    doFour(printPost)

def printGrid():
    doTwice(printRow)
    printBeams()

printGrid()



str=input("Enter string")
do_twice(print_msg,str )

print("+",end='')


