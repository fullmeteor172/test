#include<iostream>
#include <cmath>

using namespace std;

int ModuloTwo(int a, int b){
    return a%b;
}

int MultTwo(int a, int b){
    return a*b;
}

int AddTwo(int a, int b){
    return a+b;
}

int SubTwo(int a, int b){
    return a-b;
}

int DivTwo(int a, int b){
    return float(a/b);
}
void PrintLol(){
    cout << endl << "LOL" << endl;
}

void PrintHeader(){
    cout << "----GIT TESTING DUMMY APPLICATION V 0.02---\n\n";
}


void GetAndPrintName(){
    string name;
    cout << endl << "Enter your name: ";
    cin >> name;
    cout << endl << "It's good to meet you " << name << endl;
}

int main(){
    PrintHeader();
    GetAndPrintName();
    
    //Getting input values of two numbers
    int num[2];
    cout << endl << "Enter one number: ";
    cin >> num[0];
    cout << endl << "Enter second number: ";
    cin >> num[1];
    
    //69 Check
    if(num[0]==69 || num[1] == 69){
        cout << endl << "ohh!, 69 is a nice choice " << endl;
    }
    string value;
    cout << "What opperation to perform Addition/Subtraction/Multiplication/Division/Modulo";
    cout << "Addition = A Subtraction = S Multiplication = M Division = D Modulo = Mod";
    cout << endl << " Enter opperation: "<< endl; 
    cin >> value ;
    //Printing operations of those numbers
<<<<<<< HEAD
    if(value == "a" || "A")  {cout << "\nThe sum is: " << AddTwo(num[0], num[1]);}
    if (value == "s" || "S"){ cout << "\nThe difference is: " << SubTwo(num[0], num[1]);}
    if (value == "m" || "M"){cout << "\nThe product is: " << MultTwo(num[0], num[1]);}
    if (value == "Mod" || "mod"){cout << "\nThe mod is: " << ModuloTwo(num[0], num[1]);}
    if (value == "D" || "d"){cout << "\nThe mod is: " << DivTwo(num[0], num[1]);}
=======
    cout << "\nThe sum is: " << AddTwo(num[0], num[1]);
    cout << "\nThe difference is: " << SubTwo(num[0], num[1]);
    cout << "\nThe product is: " << MultTwo(num[0], num[1]);
    cout << "\nThe mod is: " << ModuloTwo(num[0], num[1]);
    cout << "\nThe square root of the numbers are:" << "\n1st number : " << sqrt(num[0]) << "\n2nd number : " << sqrt(num[1]) << endl; 
>>>>>>> faa8d931f2ddec497b04b481e9a502b7cc2e16a7

    PrintLol();
    return 0;
}