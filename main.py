import input
import turing_machine


# Read file
nStates, states, nSymbols, symbols, nNotTermSymbols, notTermSymbols, acceptState, inputs = input.input()

# Create machine
machine = turing_machine.TuringMachine(acceptState, states)

stream = open("output.txt", mode="w+")

# Processa todas as entradas
for inputString in inputs:
    machine.verificaEntrada(inputString, stream)