def printTable(tableData):
    # Step 1: Find the maximum width of each column
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        # Find the longest string in this column
        colWidths[i] = max(len(item) for item in tableData[i])

    # Step 2: Print row by row
    numRows = len(tableData[0])
    for row in range(numRows):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print()  # Newline at the end of each row


# Example input
tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

printTable(tableData)
