n=5

def countdown(n):
    if n == 1:
        print(1)
        return
    print(n)
    countdown(n-1)

countdown(n)