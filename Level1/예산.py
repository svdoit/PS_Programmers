def solution(d, budget):
    answer = 0
    
    d = sorted(d)
    
    for i in d:
        if budget-i < 0:
            break
        else:
            budget -= i
            answer += 1
    
    return answer
