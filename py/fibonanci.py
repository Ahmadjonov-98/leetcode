def fib(n):
    arr = [0,1]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        while True:
            if len(arr)==n+1:
                return arr[n]
            else:
                arr.append(arr[-1]+arr[-2])
print(fib(42))