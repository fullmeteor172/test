#include<iostream>

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
    
    //Printing operations of those numbers
    cout << "\nThe sum is: " << AddTwo(num[0], num[1]);
    cout << "\nThe difference is: " << SubTwo(num[0], num[1]);
    cout << "\nThe product is: " << MultTwo(num[0], num[1]);
    cout << "\nThe mod is: " << ModuloTwo(num[0], num[1]);

    PrintLol();
    return 0;
}