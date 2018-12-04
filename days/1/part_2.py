def main(input_filename):
    frequency = 0
    frequency_dict = {}
    first_twice = None
    while first_twice is None:
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                number = int(line.strip())
                frequency += number
                if first_twice is None and frequency_dict.get(frequency):
                    first_twice = frequency
                elif not frequency_dict.get(frequency):
                    frequency_dict[frequency] = True
    return first_twice


if __name__ == '__main__':
    print(main('input.txt'))
