def main(input_filename):
    frequency = 0
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            number = int(line.strip())
            frequency += number
    return frequency


if __name__ == '__main__':
    print(main('input.txt'))
