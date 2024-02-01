from models.symbol import Symbol


class Grammar:
    # field symbols: list of Symbol
    # field axiom: Symbol
    # field rules: list of Rule
    # field non_terminals: set of Symbol
    # field name: String
    # method createNewSymbol: String -> Symbol
    # method isNonTerminal: Symbol -> Boolean

    def __init__(self, symbols, axiom, rules, name):
        # symbols: list of Symbol
        # axiom: Symbol
        # rules: list of Rule
        # name: String

        self.symbols = symbols
        self.axiom = axiom
        self.rules = rules
        self.name = name

        self.non_terminals = set()
        for rule in rules:
            self.non_terminals.add(rule.lhs)

    # Returns a new symbol (with a new name build from the argument)
    def createNewSymbol(self, symbolName):
        # symbolName: String

        name = symbolName

        ok = False
        while not ok:
            ok = True
            for s in self.symbols:
                if s.name == name:
                    ok = False
                    continue

            if ok is False:
                name = name + "'"

        return Symbol(name)

    def is_non_terminal(self, symbol):
        # symbol: Symbol
        return symbol in self.non_terminals

    def __str__(self):
        return "{" + \
               "symbols = [" + ",".join([str(s) for s in self.symbols]) + "] " + \
               "axiom = " + str(self.axiom) + " " + \
               "rules = [" + ", ".join(str(r) for r in self.rules) + "]" + \
               "}"
