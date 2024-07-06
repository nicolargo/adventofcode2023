#!/usr/bin/env python3

import argparse
import logging
import sys

logger = logging.getLogger(__name__)

TRANSFORMS = [
    {"letters": "one", "digits": "1", "position": "-1"},
    {"letters": "two", "digits": "2", "position": "-1"},
    {"letters": "three", "digits": "3", "position": "-1"},
    {"letters": "four", "digits": "4", "position": "-1"},
    {"letters": "five", "digits": "5", "position": "-1"},
    {"letters": "six", "digits": "6", "position": "-1"},
    {"letters": "seven", "digits": "7", "position": "-1"},
    {"letters": "eight", "digits": "8", "position": "-1"},
    {"letters": "nine", "digits": "9", "position": "-1"},
]

parser = argparse.ArgumentParser(
    prog="day02",
    conflict_handler="resolve",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument(
    "-d",
    "--debug",
    action="store_true",
    default=False,
    dest="debug",
    help="enable debug mode",
)
parser.add_argument(
    "-i", "--input", default="./puzzle_test.txt", dest="input_file", help="Input puzzle"
)
args = parser.parse_args()
if args.debug:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
    )

result = 0
with open(args.input_file, "r") as f:
    for line in f:
        # Remove \n
        line = line.rstrip()
        print(line)

        logger.debug("*" * 80)
        logger.debug(line)

        transforms_copy = TRANSFORMS.copy()
        # Find letters position in the string
        for i in transforms_copy:
            i["position"] = line.find(i["letters"])
        # Remove not found
        transforms_copy = [x for x in transforms_copy if x["position"] != -1]
        # Sort
        transforms_copy.sort(key=lambda x: x["position"])
        # Only take into account first one and last one
        logger.debug(transforms_copy)
        if len(transforms_copy) > 0:
            transforms_copy = [transforms_copy[0], transforms_copy[-1]]

        # Replace letters by digits
        logger.debug(transforms_copy)
        for i in transforms_copy:
            line = line.replace(i["letters"], i["digits"])
        logger.debug(line)

        # Use same algo than day01
        digits = list(filter(lambda x: x.isdigit(), line))
        if len(digits) > 0:
            logger.debug(int(digits[0] + digits[-1]))
            print(int(digits[0] + digits[-1]))
            result += int(digits[0] + digits[-1])
        else:
            logger.error("Can not add digits {} for line {}".format(digits, line))
            sys.exit(1)

print(result)
