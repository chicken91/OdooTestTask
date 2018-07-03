import itertools
import random, time
from collections import Counter


def validate_string(validate_map, validate_value):
    return True if validate_map[validate_value] is not None else False


def update_validate_map(validate_map, validate_value, max_count):
    validate_map[validate_value] += 1
    if validate_map[validate_value] == max_count:
        del validate_map[validate_value]


def create_char():
    while True:
        char_value = random.choice(list(one_char_validate_map.keys()))

        string_length = len(string)
        if string_length > 1:
            two_char_validate_value = string[-1:] + char_value
            if validate_string(two_char_validate_map, two_char_validate_value):
                if string_length > 2:
                    three_char_validate_value = string[-2:] + char_value
                    if validate_string(three_char_validate_map, three_char_validate_value):
                        update_validate_map(one_char_validate_map, char_value, 40000)
                        update_validate_map(two_char_validate_map, two_char_validate_value, 2000)
                        update_validate_map(three_char_validate_map, three_char_validate_value, 100)
                        return char_value
                else:
                    update_validate_map(one_char_validate_map, char_value, 40000)
                    update_validate_map(two_char_validate_map, two_char_validate_value, 2000)
                    return char_value
        else:
            update_validate_map(one_char_validate_map, char_value, 40000)
            return char_value


def init_validate_maps():
    for i in range(97, 123):
        one_char_validate_map[chr(i)] = 0
        for j in range(97, 123):
            two_char_validate_map[chr(i) + chr(j)] = 0
            for k in range(97, 123):
                three_char_validate_map[chr(i) + chr(j) + chr(k)] = 0


one_char_validate_map = Counter()
two_char_validate_map = Counter()
three_char_validate_map = Counter()
string = ""
start_time = time.time()

init_validate_maps()
for i in range(1000000):
    char = create_char()
    print(char, end='')
    string += char

print(end='\n')
print("Passed time: " + str(time.time() - start_time))
