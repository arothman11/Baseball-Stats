import re
import sys, os


baseball_regex = re.compile(r"(\w* \w*) batted (\d+) times with (\d+) hits and \d+ runs")

if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

with open(filename) as f:
    for line in f:
        match = re.match(baseball_regex, line)