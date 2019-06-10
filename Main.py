from test import *
from searcher import *

with open('output.csv', 'w') as f:
    f.write('Title, Main Story, Main + Extras, Completionist, Developer, Publisher, Platform(s), Genre(s)\n')

with open('games.txt') as f:
    for line in f:
        line = line.strip()
        url = searcher(line)
        data = data_extractor(url)

        print_game(data)
        add_to_csv('output.csv', data)
