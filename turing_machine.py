   

from io import FileIO


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


    def __str__(self):
        return str(self.__number)
        

    def addTransition(self, transition : Transition):
        self.__transitions.append(transition)

    def getTransitions(self):
        return self.__transitions

    def setTransitions(self, transitions : list[Transition]):
        self.__transitions = transitions

    def hasTransition(self, symbol : bytes):
        for transition in self.__transitions:
            if transition.getReadSymbol() == symbol:
                return transition
        return False

    def printTransitions(self):
        if len(self.__transitions) == 0:
            print("")
            return
        for transition in self.getTransitions():
            print(transition)

  

class Transition():
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

    def getMovement(self):
        return self.__movement

    def getDestination(self):
        return self.__destinationState

    def getReadSymbol(self):
        return self.__readSymbol

    def getWriteSymbol(self):
        return self.__writeSymbol

    def __str__(self):
        string = ""

        string += "Destination state: "+str(self.__destinationState)+" "
        string += "Read symbol: "+self.__readSymbol+" "
        string += "Write symbol: "+self.__writeSymbol+" "
        string += "Movement: "+self.__movement

        return string

      
class Tape():

    __lambda = "B"

    def __init__(self, tape = ""):
        self.__tape = dict((enumerate(tape)))
        self.__posAtual = 0

    def __str__(self):
        string = ""
        
        for value in self.__tape.values():
            string += value

        return string

    def read(self):     
        if self.__posAtual in self.__tape:
            return self.__tape[self.__posAtual]

        else:
            return Tape.__lambda    

    def write(self, **kwargs):
        index = self.__posAtual;
        symbol = Tape.__lambda

        for name, value in kwargs.items():
            if name == "index":
                index = value 
            if name == "symbol":
                symbol = value 

        self.__tape[index] = symbol

    def right(self):
        self.__posAtual = self.__posAtual + 1


    def left(self):
        self.__posAtual = self.__posAtual - 1 


     


class TuringMachine():

    def __init__(self, acceptanceState: int, states : list[State]):
        self.__currState = 0
        self.__acceptance = acceptanceState
        self.__states = states
        self.__tape = None

    def verificaEntrada(self, entrada: str, stream : FileIO):
        """
        Função responsável por controlar a lógica da máquina em si
        Modificar aqui caso queira alterar a saída
        """
        result = self.__processaEntrada(entrada)

        if result:
            stream.write("aceita\n")
            return
        stream.write("rejeita\n")
        return

    def __processaEntrada(self, entrada : str):
        # Inicia a fita
        self.__tape = Tape(entrada)
        # volta para estado inicial
        self.__currState = 0 

        # While no return is given
        result = self.__transiciona(self.__tape.read())
        while result != True and result != False:
            result = self.__transiciona(self.__tape.read())

        return result
        

    def __transiciona(self, symbol : bytes):
        # existe uma transição para esse símbolo ?
        result = self.__states[self.__currState].hasTransition(symbol)
        
        # nao existe transicao
        if result == False:
            # É estado de aceitação ?
            if self.__currState == self.__acceptance:
                return True
            else:
                # Erro !
                return False

        # Existe transição, executa !
        # Escreve na fita !
        self.__tape.write(symbol = result.getWriteSymbol())

        # Move
        if result.getMovement() == 'R':
            self.__tape.right()
        elif result.getMovement() == 'L':
            self.__tape.left()
        elif result.getMovement() == 'S':
            return False

        # Muda de estado para o destino
        self.__currState = self.__states.index(result.getDestination())


