def charAt(s, i):
    if len(s) - 1 < i:
        return " "
    else:
        return s[i]

def radixsort(unsortedlist, size):


def main():
    expr = input("Enter expression: ")
    pythons = eval(expr)
    mine = eval_infix(expr)
    print(mine, pythons)


if __name__ == '__main__':
    main()
