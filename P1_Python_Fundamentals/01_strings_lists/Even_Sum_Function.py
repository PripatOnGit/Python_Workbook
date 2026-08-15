
#Return the sum of all even numbers from 1 to n (inclusive).

def calculate_even_sum(num):
    sum = 0
    if num!=0:
        for n in range(num+1):
            if n%2==0:
                sum+=n
    return sum

if __name__=="__main__":
    num = int(input("Enter Number: "))
    print(calculate_even_sum(num))