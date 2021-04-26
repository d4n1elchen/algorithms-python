from tabulate import tabulate

def print_table(table): 
    print(tabulate(table, showindex="always", headers=list(range(0, len(table[0]))), tablefmt="pipe"))
