def solution(nubmers):

    ##comb 함수의 각 요소(2차원배열)의 합계를 arr에 넣기
    arr = [sum(x) for x in comb(nubmers, 2)]

    ##최종적으로 arr에 중복제거 및 정렬한값을 리턴
    return sorted(list(set(arr)))


def comb(population,num):
	ans = []
    ## 정의된 값인지 확인한다.
	if num > len(population): return ans
	## Base Case
	if num == 1:
		for i in population:
			ans.append([i])
    ## General Case
	elif num>1:
		for i in range(len(population)-num+1): ## i가 시작하는 값 - len(population) - (n-1)이고 이 때 n은 lst로부터 추출할 개수와 같다.
			for temp in comb(population[i+1:],num-1):
				ans.append([population[i]]+temp)

	return ans


anss = []
ansss = [[1,2],[3,4]]
anss.append(ansss[0] + [7])
print(anss)

print(solution([1,2,3]))