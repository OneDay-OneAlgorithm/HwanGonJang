# 배열 * 와 for문 차이
n = 10
a = [[] for _ in range(n + 1)]
b = [[] * (n + 1)]
c = [[n] * (n + 1)]

print(a)
print(b)
print(c)