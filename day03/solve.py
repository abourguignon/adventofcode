from collections import Counter

from data import input


input_per_santa = {
    'Santa': input[0::2],
    'Robo-Santa': input[1::2],
}

positions = []
for santa, plan in input_per_santa.items():
    position = (0,0)  # Initial position
    positions_per_santa = []
    positions_per_santa.append(position)
    for move in plan:
        if move == '^':
            position = (position[0], position[1]+1)
        elif move == '>':
            position = (position[0]+1, position[1])
        elif move == 'v':
            position = (position[0], position[1]-1)
        elif move == '<':
            position = (position[0]-1, position[1])
        positions_per_santa.append(position)

    print 'Number of houses that received at least one present from %s: %d' % (santa, len(Counter(positions_per_santa)))

    positions.extend(positions_per_santa)

print 'Number of houses that received at least one present from the Santa team: %d' % len(Counter(positions))
