for i in range(2, 100):
    j = 2

    while j <= (i / 2):

        if i % j == 0:
            break
        j += 1

    if j > i / j:
        print(i, "Is a Prime number")
