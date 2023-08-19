tableData = [['apples','oranges','cherries','banana'],
              ['Alice','Bob','Carol','David'],
              ['dogs','cats','moose','goose'],
              ['sam','player','titanic']]

def printer(data):
    colWidth = [0] * len(data)
    for i in range(len(data)):
        colWidth[i] = len(data[i])
    colWidth.sort()
    for i in range(colWidth[-1]):
        for j in range(len(data)):
            try:
                print(data[j][i].ljust(10),end ="")
            except IndexError:
                print('')
        print()
printer(tableData)