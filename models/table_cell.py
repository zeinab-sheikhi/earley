class TableCell:
    # field cell: list of Item
    # method addItemToCell: add Item to table cell

    def __init__(self):
        self.cell = []

    # Adds an item at the end of the t (+ prints some log), argument reason indicates the name of operations:"init","pred","scan","comp"
    def add_item_to_cell(self, item, reason=None):
        if reason is not None:
            reasonStr = reason + ": "
        else:
            reasonStr = ""

        if item not in self.cell:
            self.cell.append(item)
            print(reasonStr + str(item))
