target = 1001

def ring(level, last_corner):
    return range(last_corner, last_corner + 8*level + 1, level*2)[1:]

lines = (target + 1) / 2

corners = [1]
total = 1

for l in xrange(1, lines):
    corners = ring(l, corners[-1])
    for corner in corners:
        total += corner

print total
