def countPrimes(self,n: int) -> int:
    arr = [i for i in range(2,n) ]
    for p in arr:
        for d in range(2, int(n/p)+1):
            if p*d in arr:
                arr.remove(p*d)
    return len(arr)