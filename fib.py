def fib():
    fibs = [1, 2]
    x = 0
    for i in range(1,9):
        fibo = fibs[x] + fibs[x+1]
        x += 1
        fibs.append(fibo)
    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
