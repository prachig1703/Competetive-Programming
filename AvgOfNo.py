A = int(input("Enter an integer A: "))

if A % 5 == 0 and A % 11 == 0:
    print(f"{A} is divisible by both 5 and 11.")
else:
    print(f"{A} is not divisible by both 5 and 11.")