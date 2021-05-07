from itertools import combinations

def check(a, b, c):
    total = a + b + c
    
    for i in range(2, total):
        if total % i == 0: return False
    return True

def solution(nums):
    answer = 0
    
    num_sum = list(combinations(nums, 3))
    
    for n in num_sum:
        if check(n[0], n[1], n[2]) : answer  += 1    
    
    return answer
