def fibinocci(N):
    if(N==0):
        return 0
    elif(N==1):
        return 1
    else:
        return fibinocci(N-1)+fibinocci(N-2)
N = int(input("Enter: "))
print(fibinocci(N))
