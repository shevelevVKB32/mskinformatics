from collections import deque
n = int(input())
deq = deque()
deqt = deque()
res = []
k1 = 0
k2 = 0
for i in range(n):
    t1 = input().split()
    if  "-" in t1:
        res.append(deq.popleft())
        k1 -= 1
    elif  '+' in t1:
        deqt.append(t1[-1])
        k2 += 1
    else :
        deqt.appendleft(t1[-1])
        k2 += 1
    if k1 < k2:
        deq.append(deqt.popleft())
        k2 -= 1
        k1 += 1
print(*res, sep='\n')
