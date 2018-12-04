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
    return frequency, first_twice


if __name__ == '__main__':
    import os
    this_dir = os.path.abspath(os.path.dirname(__file__))
    input_dir = os.path.join(this_dir, 'inputs')
    print(main(os.path.join(input_dir, 'one.txt')))
