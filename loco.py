#This is a python port of main.cpp

def ModTwo(a,b):
    return a%b

def MultTwo(a,b):
    return a*b

def AddTwo(a,b):
    return a+b

def SubTwo(a,b):
    return a-b

def oe(a,b):
    if a%2==0:
        print("Your number is even :",a)
    else:
        print("Your number is odd :",a)
    if b%2==0:
        print("Your number is even :",b)
    else:
        print("Your number is odd :",b)
    return a and b

def prime(n):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                break
        else:
            print("Your number is a prime number :",n)

def PrintEnd():
    print("\n---End---\n")


def GetAndPrintName():
    userName = input("\nEnter your name: ")
    devs_vitap = ["VIJAY" , "SID" , "MARIA" , "DHRUV", "RYU", "AMAAN", "OBITO"]
    
    # Guys add your names if you want to in the list devs_vitap
    if userName.upper() in devs_vitap:
        print("\nHey boss")
    else :    
        print("\n\nIt's good to meet you " + userName)


def PrintHeader():
    print("\n\n---GIT TESTING DUMMY APP v 0.04 PY EDITION---")

def GetTwoNumbers():
    num1 = int(input("\nEnter one number : "))
    num2 = int(input("Enter another number : "))
    return num1, num2

def SixNineCheck(a,b):
    if a == 69 or b == 69:
        return True
    else:
        return False
    
def GetFact(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact    

def main():
    
    PrintHeader()
    
    GetAndPrintName()
    num1, num2 = GetTwoNumbers()

    #69 checker
    if SixNineCheck(num1, num2):
        print("\n\nOhhh! 69 is a nice choice ( ͡~ ͜ʖ ͡°)")
    
    #Printing operations on the two numbers
    print("")
    p=oe(num1,num2)
    q=prime(num1)
    r=prime(num2)
    print("The sum is : " + str(AddTwo(num1, num2)))
    print("The difference is : " + str(SubTwo(num1, num2)))
    print("The product is : " + str(MultTwo(num1, num2)))
    print("The mod is : " + str(ModTwo(num1, num2)))
    print("The Factorials are : ", GetFact(num1), " and ", GetFact(num2))

    #Footer
    PrintEnd();


if __name__ == "__main__":
    main()
