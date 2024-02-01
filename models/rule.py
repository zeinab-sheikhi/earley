class Rule:
    # field lhs: Symbol
    # field rhs: list of Symbol
    # (no methods)

    def __init__(self, lhs, rhs):
        # lhs: Symbol
        # rhs: list of Symbol

        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return str(self.lhs) + " --> [" + ",".join([str(s) for s in self.rhs]) + "]"
