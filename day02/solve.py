from collections import namedtuple

from data import input


Dimensions = namedtuple('Dimensions', 'l w h')
total_wrapping_paper_surface = 0
total_ribbon_length = 0

for i, dimensions_str in enumerate(input.splitlines()):
    d = Dimensions(*[int(x) for x in dimensions_str.split('x')])

    # Wrapping paper
    sides = d.l*d.w, d.w*d.h, d.h*d.l
    wrapping_paper_surface = sum([2*side for side in sides]) + min (sides)
    total_wrapping_paper_surface += wrapping_paper_surface

    # print 'Dimensions to wrapping paper square feet: %s -> %s sq ft' % (dimensions_str, wrapping_paper_surface)

    # Ribbon
    a, b = sorted(d)[:2]
    total_ribbon_length += 2*a + 2*b + reduce(lambda x, y: x*y, d)

print 'Total wrapping paper surface (square feet): %s' % total_wrapping_paper_surface
print 'Total ribbon length (feet): %s' % total_ribbon_length
