#!/usr/bin/env python3

import argparse
import logging

logger = logging.getLogger(__name__)

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
    "-i",
    "--input",
    default="./puzzle_test.txt",
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


class Game:
    def __init__(self, game_record):
        self.id = None
        self.handfuls = []
        self.stats = {
            "red": {"min": 0},
            "green": {"min": 0},
            "blue": {"min": 0},
        }
        self.read(game_record)
        self.compute_stats()

    def __repr__(self) -> str:
        ret = "Game id   : {}\n".format(self.id)
        ret += "- Handfuls: {}\n".format(self.handfuls)
        ret += "- Stats   : {}\n".format(self.stats)
        return ret

    def read(self, game_record):
        # logger.debug(game_record)
        id, results = game_record.split(":")
        self.id = int(id.strip().split(" ")[1])
        for r in results.split(";"):
            handful = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for cube in r.split(","):
                v, k = cube.strip().split(" ")
                v = v.strip()
                k = k.strip()
                handful[k] = int(v)
                self.handfuls.append(handful)

    def compute_stats(self):
        for h in self.handfuls:
            for k, v in h.items():
                self.stats[k]["min"] = max(self.stats[k]["min"], v)

    def check(self, result):
        """Return True if the proposed result is compatible with the handfuls
        result is a dict: {"red": 12, "green": 13, "blue": 14}
        """
        for k, v in result.items():
            if self.stats[k]["min"] > v:
                return False
        return True


def read_games_records(input_file):
    with open(input_file, "r") as f:
        for line in f:
            yield line.strip()


def main():
    result = 0

    games = []
    for game_record in read_games_records(args.input_file):
        new_game = Game(game_record)
        games.append(new_game)
        logger.debug(new_game)
        logger.debug(new_game.stats)
        if new_game.check({"red": 12, "green": 13, "blue": 14}):
            result += new_game.id

    print(result)


if __name__ == "__main__":
    main()
