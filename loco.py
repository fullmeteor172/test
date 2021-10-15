#This is a python port of main.cpp

def DivTwo(a,b):
    return a/b

def ModTwo(a,b):
    return a%b

def MultTwo(a,b):
    return a*b

def AddTwo(a,b):
    return a+b

def SubTwo(a,b):
    return a-b

<<<<<<< HEAD
def PrintLol():
    print("\n---LOL---\n")
def Cry():
    print("\n-----Cry----\n")
=======
def PrintEnd():
    print("\n---End---\n")

>>>>>>> faa8d931f2ddec497b04b481e9a502b7cc2e16a7

def GetAndPrintName():
    userName = input("\nEnter your name: ")
    devs_vitap = ["VIJAY" , "SID" , "MARIA" , "DHRUV", "RYU", "AMAAN"]
    
    # Guys add your names if you want to in the list devs_vitap
    if userName.upper() in devs_vitap:
        print("\nHey boss")
    else :    
        print("\n\nIt's good to meet you " + userName)


def PrintHeader():
    print("---GIT TESTING DUMMY APP v 0.04 PY EDITION---")

def GetTwoNumbers():
    num1 = int(input("\nEnter one number: "))
    num2 = int(input("\nEnter another number: "))
    return num1, num2

def SixNineCheck(a,b):
    if a == 69 or b == 69:
        return True
    else:
        return False    
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
    
    print("What opperation to perform Addition/Subtraction/Multiplication/Division/Modulo")
    print("Addition = A Subtraction = S Multiplication = M Division = D Modulo = Mod")
    value = str(input("\n Enter opperation: "))
    
    #Printing operations on the two numbers
<<<<<<< HEAD
    if (value == "A" or  value =="a"):
        print("The sum is: " + str(AddTwo(num1, num2)))
    elif (value == "S" or  value == "s"):
        print("The difference is: " + str(SubTwo(num1, num2)))
    elif (value == "M" or  value == "s"):  
        print("The product is: " + str(MultTwo(num1, num2)))
    elif (value == "D" or  value == "d"):
         print("The div is: " + str(ModTwo(num1, num2)))
    elif (value == "Mod" or  value == "mod"):
        print("The mod is: " + str(ModTwo(num1, num2)))
    else:
        Cry()
=======
    print("The sum is: " + str(AddTwo(num1, num2)))
    print("The difference is: " + str(SubTwo(num1, num2)))
    print("The product is: " + str(MultTwo(num1, num2)))
    print("The mod is: " + str(ModTwo(num1, num2)))
    print("The Factorials are: ", GetFact(num1), " and ", GetFact(num2))

>>>>>>> faa8d931f2ddec497b04b481e9a502b7cc2e16a7
    #Footer
    PrintEnd();


if __name__ == "__main__":
    main()
