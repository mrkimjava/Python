def solution(s):
    return s[int(len(s)/2 - 1) : int(len(s)/2 + 1)] if len(s) % 2 == 0 else s[int(len(s)/2)]



a = solution('abcdefgh')
print('테스트')


