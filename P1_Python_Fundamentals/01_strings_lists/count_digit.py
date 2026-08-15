def count_digit(num):
    count = 0
    if num == 0:
        count= 1 
    while(num > 0):
        count += 1
        num = num//10
    return count
       

if __name__ == "__main__":
    num = abs(int(input("Enter number: ")))
    ans = count_digit(num)
    print(f"count of digit in {num}:{ans}")