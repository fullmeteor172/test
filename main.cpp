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

void lol(){
    cout<<endl<<"LOL";
}

void SplashScreen(){
    cout<<"RUNNING THE ULTRA NEW NEW PROGRAM\tPRE_ALPHA_BUILD V 0.0.1"<<endl<<endl;
}

void name(){
    char name[20];
    cout<<endl<<"Enter your name: ";
    cin>>name;
    cout<<endl<<"It's good to meet you "<<name;
}

int main(){
SplashScreen();
cout<<"Hello World!";
name();
int max;
max = 100; //set the upper bound to generate the random number
srand(time(0));
cout << "The random number is: "<<rand()%max;
int num[2];
cout<<endl<<"Enter one number: ";
cin>>num[0];
cout<<endl<<"Enter second number: ";
cin>>num[1];
cout<<endl<<"The sum of these numbers is: "<<AddTwo(num[0],num[1]);
cout<<endl<<"The diff of these two numbers is: "<<SubTwo(num[0], num[1]);
cout<<endl<<"The product of these two numbers is: "<<MultTwo(num[0],num[1]);
cout<<endl<<"The remainder of the division of these two numbers is: "<<ModuloTwo(num[0], num[1]);
cout<<endl;
lol();
return 0;
}

   
