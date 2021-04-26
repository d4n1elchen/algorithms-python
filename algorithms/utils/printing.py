from tabulate import tabulate

def print_table(table, showindex = None, headers = None):
    print(tabulate(table, 
                    showindex="always" if not showindex else showindex, 
                    headers=list(range(0, len(table[0]))) if not headers else headers, 
                    tablefmt="pipe"))
