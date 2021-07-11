"""
    This module parses python input into the format specified by the given
    documentation. I.E:

    1st line = int X where x is the number of states on the turing machine
   
    2nd line = int Y + String x where Y is the number of terminal symbols
    and x is the sequence of the symbols themselves separated by spaces, 
    we assume that 10 is the maximum number of terminal symbols allowed

    3rd line = int X + String s where x is the number of non terminal symbols
    and s is the sequence of non terminal symbols separated by spaces 

    4th line = int X where x is a cardinal number from 0 to 9 representing the 
    acceptation state of the machine

    5th line = int X where x is the number of transitions for the machine 
    (max 50)

    6th line forward: the X transitions numerated on the previous line, each line
    corresponds to one transition whose elements are separated by spaces. The boundaries 
    of the tape are given by the blank symbol (B). Lambda is "-"

    6+Xth line : int X where x is the number of entry strings

    7+Xth line : String s where s are the the entry strings, each 
    string must contain a maximum of 20 symbols
"""

def input():
    pass