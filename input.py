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

import turing_machine as tm

def input(**kwargs):

    docName = "entrada.txt"

    for arg, value in kwargs:
        if arg == "file":
            docName = value


    stream = open(docName, 'r')

    # First we read the number of states:
    nStates = int(stream.readline().strip())

    states : list[tm.State] = []

    for i in range(0, nStates):
        states.append(tm.State(i))


    # Now we read the second line which contains the number of symbols + the symbols themselves
    line2 = stream.readline().strip()
    line2 = line2.split(' ')
    nSymbols = int(line2[0])
    symbols = []
    for i in range(1, nSymbols+1):
        symbols.append(line2[i])
    print("Symbols = "+str(symbols))
    print("nStates = "+str(nStates))

    # Similarly for the 3rd line
    line3 = stream.readline().strip()
    line3 = line3.split(' ')
    nNotTermSymbols = int(line3[0])
    notTermsymbols = []
    for i in range(1, nNotTermSymbols+1):
        notTermsymbols.append(line3[i])
    print("Symbols = "+str(notTermsymbols))
    print("nNotTerm = "+str(nNotTermSymbols))

    acceptState = int(stream.readline().strip())

    nTransitions = int(stream.readline().strip())

    transitions = []

    for i in range(nTransitions):
        line = stream.readline().strip()
        line = line.split(' ')
        originState = int(line[0])
        symbolRead = line[1]
        destinationState = int(line[2])
        symbolWrite = line[3]
        movement = line[4]
        states[originState].addTransition(tm.Transition(states[destinationState], symbolRead, symbolWrite, movement))

    for state in states:
        state.printTransitions()

    nInputs = int(stream.readline().strip())

    inputs : list[str] = []

    for i in range(nInputs):
        string = stream.readline().strip().replace("-", "B")
        inputs.append(string)

    for input in inputs:
        print(input)

   
    # retorna todos os dados colhidos
    return nStates, states, nSymbols, symbols, nNotTermSymbols, notTermsymbols, acceptState, inputs

