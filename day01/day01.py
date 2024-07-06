#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    prog="day01",
    conflict_handler="resolve",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument(
    "-i", "--input", default="./puzzle_test.txt", dest="input_file", help="Input puzzle"
)
args = parser.parse_args()

result = 0
with open(args.input_file, "r") as f:
    for line in f:
        digits = list(filter(lambda x: x.isdigit(), line))
        if len(digits) > 0:
            result += int(digits[0] + digits[-1])

print(result)
