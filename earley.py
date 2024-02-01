from models.table_cell import TableCell
from models.item import Item


# Creation and initialisation of the table T for the word w and the grammar gr
def init(g, word):
    T = {}
    rules = g.rules
    for j in range(1, len(word) + 2): 
        T[j] = TableCell()
    for rule in rules:
        if rule.lhs == g.axiom:
            item = Item(i=1, lhs=g.axiom, bd=[], ad=rule.rhs)
            T[1].add_item_to_cell(item, reason="init")
    return T


# Insert in the table any new items resulting from the pred operation for the iterm it
def pred(g, it, T, j):
    beta1 = it.ad[0]
    for rule in g.rules:
        if rule.lhs == beta1:
            new_item = Item(i=j, lhs=beta1, bd=[], ad=rule.rhs)
            T[j].add_item_to_cell(new_item, reason="pred")


# Insert in the table any new items resulting from the scan operation for the iterm it
def scan(item, T, j, u):
    beta1 = item.ad[0]
    if beta1.name == u:
        new_bd = item.bd + [beta1]
        new_ad = item.ad[1:]
        new_item = Item(i=item.i, lhs=item.lhs, bd=new_bd, ad=new_ad)
        T[j + 1].add_item_to_cell(new_item, reason="scan")
    

# Insert in the table any possible new items resulting from the comp operation for the iterm it
def comp(item, T, j):
    i = item.i
    m = 0
    while m < len(T[i].cell):
        current_it = T[i].cell[m]   
        if current_it.ad != []:     
            beta1 = current_it.ad[0]
            if item.lhs == beta1:
                new_bd = current_it.bd + [beta1]
                new_ad = current_it.ad[1:]
                new_item = Item(i=current_it.i, lhs=current_it.lhs, bd=new_bd, ad=new_ad)
                T[j].add_item_to_cell(new_item, reason="comp")
        m = m + 1


# Return True if the analysis is successful, otherwise False 
def table_complete(g, w, T):
    items = T[len(w) + 1].cell
    for item in items:
        if item.lhs == g.axiom and item.ad == []:
            return True
    return False


# Parse the word w for the grammar g return the parsing table at the end of the algorithm
def parse_earley(g, w):
    
    # Initialisation
    T = init(g, w)
    
    # Main Loop
    for j in range(1, len(w) + 2):
        k = 0
        while k < len(T[j].cell):    
            current_item = T[j].cell[k]
            if current_item.ad == []:
                comp(item=current_item, T=T, j=j)
            elif g.is_non_terminal(current_item.ad[0]):
                pred(g=g, it=current_item, T=T, j=j)
            elif j < len(w) + 1:
                scan(item=current_item, T=T, j=j, u=w[j - 1])          
            k = k + 1
    
    print(f"\nThe word is: {w}\n")
    # Top-down analysis
    if table_complete(g, w, T):
        print("********** Success **********\n")
    else:
        print("********** Failure **********\n")

    return T


def printChart(T, w):
    for j in range(1, len(w) + 2):
        items = T[j].cell
        for item in items:
            print(item)
