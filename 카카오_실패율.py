def solution(N, stages):
    answer = []
    counts = [0] * (N+1) ##스테이지별 횟수 N+1(스테이지완료)포함 0할당
   
    length = len(stages)
    sum = 0
    
    for i in stages:
        counts[i-1] += 1 ##멈춰있는스테이지 누적
    
    for i in range(N):
        count = counts[i]
        fail = 0 if count==0 else count/(length-sum)
        answer.append((i+1, fail))
        sum += count
        
    ## key 값으로 정렬 
    answer = [x[0] for x in sorted(answer, key=lambda x:x[1], reverse=True)]
    
    return answer