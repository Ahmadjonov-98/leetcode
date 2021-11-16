def isPrime(digit:int)-> bool:
        for i in range(2,digit):
            if digit%i ==0:
                return False
        return True    
def countPrimes(self,n: int) -> int:
    arr = []
    for x in range(2,n+1):
        if isPrime(x):
            arr.append(x) 
    return len(arr) #if arr else 0  

print(countPrimes(10))


