def is_P(S):
    if len(S) < 3:
        return False

    largest_side = max(S)
    S.remove(largest_side)
    total = 0

    for side in S:
        total += side

    if total > largest_side:
        return True
    else:
        return False

class Cached(object):
    def __init__(self):
        self.cache = {1: 1, 2: 2, 3: 3}

    def s(self, n):
        if n in self.cache:
            return self.cache[n]

        elif n > 3:
            y = self.s(n-1) + self.s(n-3)

            self.cache[n] = y
            return y

        else:
            raise ValueError

cache = Cached()

def get_U(n):
    U = set()
    for x in xrange(1,n+1):
        U.add(cache.s(x))

    return U

def get_f(u):
    # number of subsets of U for which is_P(U) is True
    pass

U = get_U(25)
