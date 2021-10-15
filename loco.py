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

def PrintLol():
    print("\n---LOL---\n")
def Cry():
    print("\n-----Cry----\n")

def GetAndPrintName():
    userName = input("\nEnter your name: ")
    print("\n\nIt's good to meet you " + userName)

def PrintHeader():
    print("---GIT TESTING DUMMY APP v 0.03 PY EDITION---")

def GetTwoNumbers():
    num1 = int(input("\nEnter one number: "))
    num2 = int(input("\nEnter another number: "))
    return num1, num2

def SixNineCheck(a,b):
    if a == 69 or b == 69:
        return True
    else:
        return False    

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
    #Footer
    PrintLol();


if __name__ == "__main__":
    main()