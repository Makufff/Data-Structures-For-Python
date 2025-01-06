def ex_02(n):
    if n == 8 :
        print("Go Back!")
    else :
        print(str(n) + " Hello!")
        ex_02(n+2)
        print(str(n) + " Bye!")
ex_02(0)


