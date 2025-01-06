def ex_03(x):
    if x < 5 :
        return 3*x
    else :
        return 2 * ex_03(x - 5) + 7
    print("finish")
    return 1


