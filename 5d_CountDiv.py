"""Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6

    count = 0
    for i in range(A, B):
        if i % K == 0:
            count += 1

    return count"""


def solution(A, B, K):
    # write your code in Python 3.6

    if A == B:
        if A % K == 0:
            return 1
        else:
            return 0

    if A == 0:
        minRem = 0
    elif A < K:
        minRem = K - A
    else:
        minRem = (A % K)
    maxRem = (B % K)

    # print(minRem,maxRem)

    rem = (((B - maxRem) - (A + minRem)) // K) + 1

    return (rem)



