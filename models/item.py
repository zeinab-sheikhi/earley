class Item:
    # field lhs: Symbol
    # field bd: list of Symbol
    # field ad: list of Symbol
    # field i: Integer

    def __init__(self, i, lhs, bd, ad):  # [i,lhs --> bd•ad]
        self.lhs = lhs
        self.bd = bd
        self.ad = ad
        self.i = i

    def __str__(self):
        return "[%d,%s --> %s • %s]" % \
            (self.i, str(self.lhs), ",".join([str(s) for s in self.bd]), ",".join([str(s) for s in self.ad]))

    def __eq__(self, other):
        return self.i == other.i and \
            self.lhs == other.lhs and self.bd == other.bd and self.ad == other.ad
