#!/usr/bin/python
import sys

def main():
    print("Hello, World!")

# $ python test.py arg1 arg2 arg3
if __name__== "__main__" :
    main()
    print( 'Number of arguments:' + str(len(sys.argv)) + ' arguments.' )
    print ( 'Argument List:' + str(sys.argv) )