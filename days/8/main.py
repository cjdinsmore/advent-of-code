def get_metadata(input_stream):
    """ part one """
    if len(input_stream) == 0:
        return 0, []
    num_children, num_metadata = input_stream[:2]
    total_meta_sum = 0
    remaining_stream = input_stream[2:]
    for _ in range(num_children):
        children_meta_sum, remaining_stream = get_metadata(remaining_stream)
        total_meta_sum += children_meta_sum
    total_meta_sum += sum(remaining_stream[:num_metadata])
    return total_meta_sum, remaining_stream[num_metadata:]


def get_value(input_stream):
    """ part two """
    if len(input_stream) == 0:
        return 0, []
    num_children, num_metadata = input_stream[:2]
    remaining_stream = input_stream[2:]
    children_values = []
    if num_children:
        for _ in range(num_children):
            children_value, remaining_stream = get_value(remaining_stream)
            children_values.append(children_value)
    else:
        return sum(remaining_stream[:num_metadata]), remaining_stream[num_metadata:]
    metadata = remaining_stream[:num_metadata]
    value = 0
    for index in metadata:
        try:
            value += children_values[index-1]
        except IndexError:
            continue
    return value, remaining_stream[num_metadata:]


def main(input_filename):
    with open(input_filename) as input_file:
        input_stream = input_file.read().strip()
        input_stream = [int(i) for i in input_stream.split()]
        print(get_metadata(input_stream))
        print(get_value(input_stream))


main('input.txt')
