from functools import lru_cache
import time

@lru_cache
def fib(n):
    if n <= 1:
        return n 
    return fib(n-1) + fib(n -2)

def main():
    start = time.time()
    for i in range(400):
        print(i, fib(i))
    print("done")
    fin = time.time()
    print("total time : ", fin - start)

if __name__ == "__main__":
    main()
