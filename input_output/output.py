#output 방법 정리

print(sth)

string = 5
print('s: %d' %(string))


#어떤 정수를 출력할 때, 낱개 숫자가 있다면 10의 거듭제곱을 곱해서 수를 만든 뒤 출력하는 것보다 하나씩 공백없이 출력하는 것이 편리
# 기본적으로 print문은 \n을 포함하기에 end로 잘라줌
for i in range(len(data)):
  print(data[i], end='')


