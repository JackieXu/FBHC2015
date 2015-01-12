from __future__ import print_function
from itertools import chain, combinations
from operator import add
import sys


def solve(max_nutrients, foods):
    food_combinations = chain.from_iterable(map(lambda x: combinations(foods, x), range(len(foods) + 1)))
    for combination in food_combinations:
        current_nutrients = [0, 0, 0]
        for food in combination:
            current_nutrients = map(add, current_nutrients, food)
            if current_nutrients[0] > max_nutrients[0] or current_nutrients[1] > max_nutrients[1] or current_nutrients[2] > max_nutrients[2]:
                break
        if current_nutrients[0] == max_nutrients[0] and current_nutrients[1] == max_nutrients[1] and current_nutrients[2] == max_nutrients[2]:
            return "yes"        
    return "no"


def main():
    with open(__file__.replace("py", "in"), "r") as input_file:
        output_file = open(__file__.replace("py", "out"), "w")
        case_count = int(next(input_file))
        case_counter = 1
        for case in range(case_count):
            max_nutrients = [int(n) for n in next(input_file).split(" ")]
            food_count = int(next(input_file))
            foods = [[int(n) for n in next(input_file).split(" ")] for _ in range(food_count)]
            print("Case #{0}: {1}".format(case_counter, solve(max_nutrients, foods)), file=output_file)
            case_counter += 1
    return 0

if __name__ == "__main__":
    status = main()
    sys.exit(status)
