import re

current_guard = None
guards = {}


def handle_awake_event(current_minute):
    global current_guard, guards
    processed_minute = guards[current_guard]['minute_fell_asleep']
    while processed_minute != current_minute:
        if not guards[current_guard]['minutes_dozing'].get(processed_minute):
            guards[current_guard]['minutes_dozing'][processed_minute] = 0
        guards[current_guard]['minutes_dozing'][processed_minute] += 1
        guards[current_guard]['total_minutes_asleep'] += 1
        processed_minute += 1
        if processed_minute == 60:
            processed_minute = 0


def process_event(input_line: str):
    global current_guard, guards
    match = re.match(r'\[\d+-\d+-\d+\s\d+:(\d+)\]\s(.*)', input_line)
    minute, event = match.groups()
    minute = int(minute)
    guard_match = re.match(r'Guard\s(#\d+)', event)
    if guard_match:
        (guard_number,) = guard_match.groups()
        current_guard = guard_number
        if not guards.get(guard_number):
            guards[guard_number] = {
                'minute_fell_asleep': None,
                'total_minutes_asleep': 0,
                'minutes_dozing': {}
            }
    elif 'asleep' in event:
        guards[current_guard]['minute_fell_asleep'] = minute
        if not guards[current_guard]['minutes_dozing'].get(minute):
            guards[current_guard]['minutes_dozing'][minute] = 0
    elif 'wakes up' in event:
        handle_awake_event(minute)


def main(input_filename):
    global guards
    with open(input_filename) as input_file:
        lines = input_file.readlines()
        lines.sort()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            process_event(line)
    most_asleep_guard = None
    most_asleep_minutes = -1
    for guard in guards:
        if guards[guard]['total_minutes_asleep'] > most_asleep_minutes:
            most_asleep_minutes = guards[guard]['total_minutes_asleep']
            most_asleep_guard = guard
    minute_most_asleep = -1
    minute_sleep_occurrences = -1
    for minute in guards[most_asleep_guard]['minutes_dozing']:
        if guards[most_asleep_guard]['minutes_dozing'][minute] > minute_sleep_occurrences:
            minute_most_asleep = minute
            minute_sleep_occurrences = guards[most_asleep_guard]['minutes_dozing'][minute]
    return most_asleep_guard, minute_most_asleep



def part_two():
    global guards
    most_asleep_guard, minute_most_dozed, occurrences = None, -1, -1
    for guard in guards:
        for minute in guards[guard]['minutes_dozing']:
            if guards[guard]['minutes_dozing'][minute] > occurrences:
                most_asleep_guard = guard
                minute_most_dozed = minute
                occurrences = guards[guard]['minutes_dozing'][minute]
    return most_asleep_guard, minute_most_dozed


if __name__ == '__main__':
    print(main('input.txt'))
    print(part_two())
