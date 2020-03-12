"""We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    import itertools
    import math

    # A.sort()
    # print(A)

    if len(A) < 2:
        return 0

    count = 0

    for i, j in list(itertools.combinations(range(len(A)), 2)):
        # print(i,j)
        # j = i+1

        if count > 10000000:
            return -1

        # print(i,j,A[i] , A[j])

        if math.sqrt((i - j) ** 2) <= (A[i] + A[j]):
            count += 1

    return count"""


def solution(A):
    circle_endpoints = []
    for i, a in enumerate(A):
        circle_endpoints += [(i - a, True), (i + a, False)]

    #circle_endpoints.sort(key=lambda x: (x[0], not x[1]))
    circle_endpoints.sort()

    print(circle_endpoints)

    intersections, active_circles = 0, 0

    for _, is_beginning in circle_endpoints:
        if is_beginning:
            intersections += active_circles
            active_circles += 1
        else:
            active_circles -= 1
        if intersections > 10E6:
            return -1

    return intersections

solution([1, 5, 2, 1, 4, 0])