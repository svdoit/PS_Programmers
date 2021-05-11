import math

def solution(n):
    sqrt = int(math.sqrt(n))
    return pow(sqrt+1, 2) if pow(sqrt,2) == n else -1
