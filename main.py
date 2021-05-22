import math
import copy


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))


def bruteForce(P, n):
    min_value = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if distance(P[i], P[j]) < min_value:
                min_value = distance(P[i], P[j])

    return min_value


def stripClosest(strip, size, d):
    min_value = d

    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < min_value:
            min_value = distance(strip[i], strip[j])
            j += 1

    return min_value


def closestUtil(P, Q, n):
    if n <= 3:
        return bruteForce(P, n)

    mid = n // 2
    midPoint = P[mid]

    dl = closestUtil(P[:mid], Q, mid)
    dr = closestUtil(P[mid:], Q, n - mid)

    d = min(dl, dr)

    strip = []
    for i in range(n):
        if abs(Q[i].x - midPoint.x) < d:
            strip.append(Q[i])

    return min(d, stripClosest(strip, len(strip), d))


def closest(P, n):
    P.sort(key=lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key=lambda point: point.y)

    return closestUtil(P, Q, n)
P = [Point(4, 6), Point(24, 60),
     Point(50, 60), Point(15, 5),
     Point(22, 11), Point(6, 8)]

n = len(P)
print("The smallest distance is",closest(P, n))