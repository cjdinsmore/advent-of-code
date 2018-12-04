def parse_line(line: str):
    split = line.split()
    col_row = split[2]
    col_start = int(col_row.split(',')[0])
    row_start = int(col_row.split(',')[1].replace(':', ''))
    width, height = split[3].split('x')
    return col_start, row_start, int(width), int(height)


def make_claim(matrix, col_start, row_start, width, height):
    for row in range(row_start, row_start + height):
        for col in range(col_start, col_start + width):
            matrix[row][col] += 1
