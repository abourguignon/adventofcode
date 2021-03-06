from data import input


up = down = 0
first_basement_visit = False

for i, char in enumerate(input):
    if char is '(':
        up += 1
    elif char is ')':
        down += 1
    else:
        raise Exception('What\'s that char doing there ?  "%s", really ?' % char)

    if up-down < 0 and not first_basement_visit:
        first_basement_visit = True
        print 'Santa is paying his first visit to the basement (at character position %d) !' % (i+1)  # 1-based positions


assert len(input) == up+down, 'Lenghts don\'t match !'

print 'Santa went up %d floor(s) and down %d floor(s) during his journey; he\'s now at floor %d' % (up, down, up-down)
