# factorial
def factorial(n):
    if n>0:
        result=n*factorial(n-1) #6*5=35   , 5*4=20    , 4*3=12    , 3*2=6  , 2*1=2   , 1*1=1  , 1
        print(result)
    else:
        result=1
    

    return result

n=int(input("Enter the value of n"))
factorial(n)

