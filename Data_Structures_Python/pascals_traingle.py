def pascal(row, column):
    if row == column or column ==0:
        return 1
    else:
        return pascal(row-1, column) + pascal(row-1, column-1)

		
for row in range(10):
    print('{: ^45}'.format(' '.join(str(pascal(row, col)) for col in range(row+1))))