for i in range(5, 0, -1):
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print("_", end="")
    print()
