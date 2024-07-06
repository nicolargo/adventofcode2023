#!/usr/bin/env python3

import argparse
import logging
import re
import sys

logger = logging.getLogger(__name__)

TRANSFORMS = [
    {"letters": "1", "digits": "1"},
    {"letters": "2", "digits": "2"},
    {"letters": "3", "digits": "3"},
    {"letters": "4", "digits": "4"},
    {"letters": "5", "digits": "5"},
    {"letters": "6", "digits": "6"},
    {"letters": "7", "digits": "7"},
    {"letters": "8", "digits": "8"},
    {"letters": "9", "digits": "9"},
    {"letters": "one", "digits": "1"},
    {"letters": "two", "digits": "2"},
    {"letters": "three", "digits": "3"},
    {"letters": "four", "digits": "4"},
    {"letters": "five", "digits": "5"},
    {"letters": "six", "digits": "6"},
    {"letters": "seven", "digits": "7"},
    {"letters": "eight", "digits": "8"},
    {"letters": "nine", "digits": "9"},
]

parser = argparse.ArgumentParser(
    prog="day01-part2",
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
    "-i",
    "--input",
    default="./puzzle_test-part2.txt",
    dest="input_file",
    help="Input puzzle",
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

        transforms_result = []
        # Find all "letters" positions in the string
        for i in TRANSFORMS:
            for p in [m.start() for m in re.finditer(i["letters"], line)]:
                transforms_result.append(
                    {
                        "letters": i["letters"],
                        "digits": i["digits"],
                        "position": p,
                    }
                )

        # Sort
        transforms_result.sort(key=lambda x: x["position"])
        # Only take into account first one and last one
        logger.debug(transforms_result)
        if len(transforms_result) > 0:
            transforms_result = [transforms_result[0], transforms_result[-1]]

        # Replace letters by digits
        logger.debug(transforms_result)
        for i in transforms_result:
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
