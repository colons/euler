import re


size = 20


def is_route(route):
    bin_string = bin(route)[2:]
    while len(bin_string) < size*2:
        bin_string = '0' + bin_string

    return len(re.findall('1', bin_string)) == size


route = 0
possible_route_count = (2**size)**2
routes = []

while route < possible_route_count:
    if route % 1000 == 0:
        print '{doing}/{of}'.format(doing=route, of=possible_route_count)

    if is_route(route):
        routes.append(route)

    route += 1

print len(routes)
