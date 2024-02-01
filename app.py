from models.symbol import Symbol
from models.grammar import Grammar
from models.rule import Rule

from earley import parse_earley

# Definition of the symbols
symS = Symbol("S")
symA = Symbol("A")
symTerminalA = Symbol("a")
symTerminalB = Symbol("b")

# Definition of a grammar
g1 = Grammar(
    # All symbols
    [symS, symA, symTerminalA, symTerminalB],
    # Axiom
    symS,
    # List of rules
    [
        Rule(symS, [symA, symS]),    # S --> AS
        Rule(symS, [symTerminalB]),  # S --> b
        Rule(symA, [symTerminalA]),  # A --> a
    ],
    # name
    "g1"
)

# Definition of a grammar
g2 = Grammar(
    [symS, symA, symTerminalA, symTerminalB],
    symS,
    [
        Rule(symS, [symA, symS]),    # S --> AS
        Rule(symS, [symTerminalB]),  # S --> b
        Rule(symA, [symA]),          # A --> A
        Rule(symA, [symTerminalA]),  # A --> a
    ],
    "g2"
)


# Definition of a grammar
g3 = Grammar(
    [symS, symA, symTerminalA, symTerminalB],
    symS,
    [
        Rule(symS, [symA, symS]),                   # S --> AS
        Rule(symS, [symA]),                         # S --> A
        Rule(symA, [symS]),                         # A --> S
        Rule(symS, [symTerminalB]),                 # S --> b
        Rule(symS, [symTerminalB, symTerminalB]),   # S --> bb
        Rule(symA, []),                             # A --> [epsilon]
        Rule(symA, [symTerminalA]),                 # A --> a
    ],
    "g3"
)

symNP = Symbol("NP")
symVP = Symbol("VP")
symDET = Symbol("DET")
symN = Symbol("N")
symPN = Symbol("PN")
symV = Symbol("V")
symthe = Symbol("the")
syma = Symbol("a")
symtruck = Symbol("truck")
symexperiment = Symbol("experiment")
symSabine = Symbol("Sabine")
symFred = Symbol("Fred")
symJamy = Symbol("Jamy")
symsaw = Symbol("saw")
symprepared = Symbol("prepared")

g4 = Grammar(
    [symS, symNP, symVP, symDET, symN, symPN, symV, symthe, syma, symtruck, symexperiment, symSabine, symFred, symJamy, symsaw, symprepared],
    symS,
    [
        Rule(symS, [symNP, symVP]),
        Rule(symNP, [symDET, symN]),
        Rule(symNP, [symPN]),
        Rule(symVP, [symV]),
        Rule(symVP, [symV, symNP]),
        Rule(symDET, [symthe]),
        Rule(symDET, [syma]),
        Rule(symN, [symtruck]),
        Rule(symN, [symexperiment]),
        Rule(symPN, [symSabine]),
        Rule(symPN, [symFred]),
        Rule(symPN, [symJamy]),
        Rule(symV, [symsaw]),
        Rule(symV, [symprepared]),
    ],
    "course note grammar"
)

symS = Symbol("S")
symNP = Symbol("NP")
symVP = Symbol("VP")
symAux = Symbol('AUX')
symDET = Symbol("DET")
symNoun = Symbol('Noun')
symV = Symbol("V")
symBook = Symbol('book')
symThat = Symbol('that')
symFlight = Symbol('flight')
symdoes = Symbol('does')


g5 = Grammar(
    [symS, symNP, symVP, symV, symBook, symThat, symFlight, symNoun, symdoes, symDET, symAux], 
    symS, 
    [
        Rule(symS, [symNP, symVP]),
        Rule(symS, [symAux, symNP, symVP]),
        Rule(symS, [symVP]),
        Rule(symNP, [symDET, symNoun]),
        Rule(symVP, [symV]),
        Rule(symVP, [symV, symNP]),
        Rule(symV, [symBook]),
        Rule(symDET, [symThat]),
        Rule(symAux, [symdoes]),
        Rule(symNoun, [symFlight]),
    ],
    "class example"
)

# --------------
w = ["Sabine", "saw", "a", "truck"]
words = ["aab", "b", "aaaaab", "abab"]
example_words = ["book", "that", "flight"]

print("GRAMMAR 1:")
print(g1)
for word in words:
    parse_earley(g1, word)
print("\n")

print("GRAMMAR 2:")
print(g2)
print()
for word in words:
    parse_earley(g2, word)
print("\n") 

print("GRAMMAR 3:")
print(g3)
print()
for word in words:
    parse_earley(g3, word)
print("\n") 

print("GRAMMAR 4:")
print(g4)
print()
parse_earley(g4, w)
print("\n") 

print("GRAMMAR 5:")
print(g5)
print()
parse_earley(g5, example_words)
print("\n") 
