def solution(d, budget):
    total = 0
    length = len(d)

    while len(d) > 0 :
        total += min(d)
        if total > budget : 
            return length - len(d)
        del budget(min(d))
        
    return length
    
