def input_number():
    num = input("Enter a number:")
    if num.isnumeric():
        print(type(int(num)))
        return int(num)
    print("Please enter a number.")
    return input_number()

def collatz(num):
    if num %2 == 0:
        num = num //2
    else:
        num = 3*num+1
    print(num)
    if num!= 1 :
        collatz(num)

num = input_number()
print(type(num))
collatz(num)