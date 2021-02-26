import re
import sys, os
import operator

players = dict()

class player:
    def __init__(self, name):
        self.name = name
        self.bats = 0
        self.hits = 0
        self.avg = 0
   
    def output(self):
        return f"{self.name}: {self.avg}"

baseball_regex = re.compile(r"(\w* \w*) batted (\d+) times with (\d+) hits and \d+ runs")

if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

with open(filename) as f:
    for line in f:
        match = re.match(baseball_regex, line)
        if match is not None:
            name = match.group(1)
            bat = match.group(2)
            hit = match.group(3)
            
            if name not in players.keys():
                players[name] = player(name)
            
            players[name].bats += int(bat)
            players[name].hits += int(hit)
    
for name in players:
    players[name].avg = players[name].hits/players[name].bats
    #https://docs.python.org/3/tutorial/floatingpoint.html
    players[name].avg = format(players[name].avg, '.3f')

#https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python
sorted_players = sorted(players.values(), key=operator.attrgetter('avg'), reverse=True)

for player in sorted_players:
    print (player.output())