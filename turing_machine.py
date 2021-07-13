   

class Transition():
    pass


class State():
    
    def __init__(self, *args):
        self.__transitions : list[Transition] = []
        self.__number = None
        if len(args) == 1:
            self.__number = args[0]
        elif len(args) == 2:
            self.__number = args[0]
            self.__transitions = args[1]



        

    def addTransition(self, transition : Transition):
        self.__transitions.append(transition)

    def getTransitions(self):
        return self.__transitions

    def setTransitions(self, transitions : list[Transition]):
        self.__transitions = transitions

    def printTransitions(self):
        if len(self.__transitions) == 0:
            print("")
            return
        for transition in self.getTransitions():
            print(transition)
  

class Transition(Transition):
    """
    Defines a transition

    Attributes
    ----------
    * destinationState : State
        The destination state for this transition 
    * terminal : bytes
        The terminal state for this transition
    * nonTerminal : list[bytes]
        The set of non-terminal states for this transition
    """
    
    def __init__(self, destinationState : State, readSymbol : bytes, writeSymbol : bytes, movement : bytes):
        '''
        Creates a new transition

        Parameters
        ----------
        destinationState : State
            The destination state in this transition
        terminal : bytes
            The terminal symbol in this transition
        nonTerminal : list[bytes]
            a list of non terminal symbols in this transition
        '''

        self.__destinationState = destinationState
        self.__readSymbol = readSymbol
        self.__writeSymbol = writeSymbol
        self.__movement = movement

    def __str__(self):
        string = ""

        string += "Destination state: "+self.__destinationState+" "
        string += "Read symbol: "+self.__readSymbol+" "
        string += "Write symbol: "+self.__writeSymbol+" "
        string += "Movement: "+self.__movement

        return string

      
class Tape():

    def __init__(self, tape = ""):
        self.__tape = dict((enumerate(tape)))
        self.__lambda = " "
        self.__posAtual = 0

    def __str__(self):
        string = ""
        
        for value in self.__tape.values():
            string += value

        return string

    def __read(self):     
        if self.__posAtual in self.__tape:
            return self.__tape[self.__posAtual]

        else:
            return Tape.__lambda    

    def __write(self, **kwargs):
        index = self.__posAtual;
        symbol = Tape.__lambda

        for name, value in kwargs.items():
            if name == "index":
                index = value 
            if name == "symbol":
                symbol = value 

        self.__tape[index] = symbol

    def __right(self):
        self.__posAtual = self.__posAtual - 1


    def __left(self):
        self.__posAtual = self.__posAtual + 1 


     


class TuringMachine():

    def __init__(self, nEstados : int, terminal : list[bytes],
    nonTerminal : list[bytes], acceptanceState: int, states : list[State]):

        self.__nEstados = nEstados
        self.__terminalSymbols = terminal
        self.__nonTerminal = nonTerminal
        self.__acceptance = acceptanceState
        self.__states = states
        self.__Tape = Tape() # Fita da máquina
        
    def processaEntrada(entrada : Tape):
        pass

