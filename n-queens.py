import math
import time
def solveNQueens(n: int):
    def solve(a, submit, ans, q):
        if len(q) == n:
            submit.append(ans)
            return submit
        for i in range(n):
            ansCopy = ans.copy()
            qCopy = q.copy()
            # ath queen in position [a,i]
            qCopy.append(i)
            ansCopy[a] = '.' * i + 'Q' + '.' * (n - i - 1)
            if isValid(qCopy):
                submit = solve(a+1, submit, ansCopy, qCopy)
            
        return submit

    def isValid(q):
        l = len(q)
        if l==1:
            return True
        for i in range(l):
            for k in range(i+1, l):
                if (i==k or q[i]==q[k] or abs(i-k)==abs(q[i]-q[k])):
                    return False
        return True
    
    q = []
    submit = []
    ans = ['....' for i in range(n)]
    return solve(0, submit, ans, q)

t1 = time.time()
sol = solveNQueens(4)
t2 = time.time()
print('Time:', t2-t1)
for i in sol:
    for j in i:
        print(j)
    print('-----------------') 
   