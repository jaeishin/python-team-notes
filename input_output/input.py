#input 방법 정리

import sys
inp = sys.stdin.readline

#단일 정수 입력
#int로 형변환 포함되어서 rstrip이 필요 없음?!

n = int(inp())

#여러 정수 공백기준으로 입력
n, m, k = map(int, inp().split())

#공백 기준으로 입력받은 원소 리스트화
data = list(map(int, inp().split()))

#2차원 배열입력
# 1 2 3
# 4 5 6
$ 7 8 9
graph = [list(map(int, inp().split())) for _ in range(n)]

or 

for _ in range(n):
  graph.append(list(map(int, inp().split())))

#2차원 배열로 만들고 싶은데 공백없이 문자가 들어오는 경우
#list comprehension사용
# 123
# 456 
# 789
graph = [list(int(x) for x in inp().strip()) for _ in range(n)]


