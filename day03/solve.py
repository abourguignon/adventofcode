from collections import Counter

from data import input


position = (0,0)  # Initial position
positions = []
positions.append(position)
for move in input:
    if move == '^':
        position = (position[0], position[1]+1)
    elif move == '>':
        position = (position[0]+1, position[1])
    elif move == 'v':
        position = (position[0], position[1]-1)
    elif move == '<':
        position = (position[0]-1, position[1])
    positions.append(position)

c = Counter(positions)

print 'Number of houses that received at least one present from Santa: %d' % len(c)
