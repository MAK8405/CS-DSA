def countDown(i):
    # base case
    if i <= 0:
        return 0
    # recursive case
    else:
        print(i)
        return countDown(i - 1)


countDown(5)
