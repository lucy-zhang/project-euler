MAX_VALUE = 10 ** 6
MAX_ROW = 100

def get_next_row(row, is_even_row, is_complete):
    next_row = []
    if is_even_row and is_complete:
        to_add = zip([0] + row, row + row[-1:])
    else:
        to_add = zip([0] + row, row)
    for i, j in to_add:
        entry = i + j
        if entry <= MAX_VALUE:
            next_row.append(entry)
        else:
            return next_row, False
    return next_row, is_complete

def values_greater_than_max():
    num_values = 0
    curr_row = [1]
    row_complete = True
    for row_num in xrange(1, MAX_ROW + 2):
        vals_in_row = 2 * len(curr_row) - (1 if (row_num % 2 == 1) and row_complete else 0)
        num_values += (row_num) - vals_in_row
        curr_row, row_complete = get_next_row(curr_row, row_num % 2 == 0, row_complete)

    return num_values

def main():
    print values_greater_than_max()

if __name__ == '__main__':
    main()
