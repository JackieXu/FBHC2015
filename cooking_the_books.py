from __future__ import print_function
import sys


def is_valid(num):
    return num[0] != '0'


def solve(case):
    if case == '0':
        return '0 0'
    
    min_num = case
    max_num = case
    char_count = len(case)
    
    for i in range(char_count):
        for j in range(char_count):
            char_list = list(case)
            char_list[i], char_list[j] = char_list[j], char_list[i]
            char_str = ''.join(char_list)
            if char_str < min_num and is_valid(char_str):
                min_num = char_str
            if char_str > max_num and is_valid(char_str):
                max_num = char_str
    return min_num + " " + max_num


def main():
    with open(__file__.replace("py", "in"), "r") as input_file:
        output_file = open(__file__.replace("py", "out"), "w")
        case_count = next(input_file)
        case_counter = 1
        for case in input_file:
            print("Case #{0}: {1}".format(
                case_counter, solve(case.strip())), file=output_file)
            case_counter += 1
    return 0

if __name__ == "__main__":
    status = main()
    sys.exit(status)
