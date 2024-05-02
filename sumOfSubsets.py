import time 

def findSubset(target, arr, sol, curr, submit=[]):
    s = sumFunc( arr, sol)
    if s == target:
        submit.append(sol)
        return submit
    for i in range(curr, len(sol)):
        solCopy = sol.copy()
        solCopy[i] = 1
        tmpSum = sumFunc(arr, solCopy)
        submit = findSubset(target, arr, solCopy, curr + 1, submit)
        if tmpSum < target:
            submit = findSubset(target, arr, solCopy, curr + 1, submit)
    return submit

def sumFunc(arr, sol):
    val = 0
    for i in range(len(sol)):
        if sol[i] == 1:
            val += arr[i]
    return val


target = 6
arr = [2,5,3,1,10,4] #[2,3,5] #
t1 = time.time()
sol = [0 for _ in range(len(arr))]
t2 = time.time()
print('Time Taken = ', t2-t1)
answer = findSubset(target, arr, sol, 0)
answer = [tuple(lst) for lst in answer]
answer = set(answer)
for i in answer:
    print(i, end = '=> ') 
    print('+'.join([str(arr[j]) for j in range(len(i)) if i[j]!=0]))