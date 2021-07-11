



class State():
    pass

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
    
    def __init__(self, destinationState : State, terminal : bytes, nonTerminal : list[bytes]):
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


class TuringMachine():

    def __init__(self, nEstados : int, terminal : list[int],
    nonTerminal : list[int], acceptanceState: int, transitions : list[bytes]) -> None :

        self.nEstados = nEstados
        self.terminalSymbols = terminal 
        self.nonTerminal = nonTerminal
        self.acceptance = acceptanceState



