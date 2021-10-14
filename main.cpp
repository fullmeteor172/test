#include<iostream>

int MultTwo(int a, int b){
    return a*b;
}

int AddTwo(int a, int b){
    return a+b;
}

int SubTwo(int a, int b){
    return a-b;
}

void SplashScreen(){
    std::cout<<"RUNNING THE ULTRA NEW NEW PROGRAM\tPRE_ALPHA_BUILD V 0.0.1"<<std::endl<<std::endl;
}

void name(){
    char name[20];
    std::cout<<std::endl<<"Enter your name: ";
    std::cin>>name;
    std::cout<<std::endl<<"It's good to meet you "<<name;
}

int main(){
SplashScreen();
std::cout<<"Hello World!";
name();
int num[2];
std::cout<<std::endl<<"Enter one number: ";
std::cin>>num[0];
std::cout<<std::endl<<"Enter second number: ";
std::cin>>num[1];
std::cout<<std::endl<<"The sum of these numbers is: "<<AddTwo(num[0],num[1]);
std::cout<<std::endl<<"The diff of these two numbers is: "<<SubTwo(num[0], num[1]);
std::cout<<std::endl<<"The product of these two numbers is: "<<MultTwo(num[0],num[1]);
return 0;
}
using namespace std;
main() {
   int max;
   max = 100; //set the upper bound to generate the random number
   srand(time(0));
   cout << "The random number is: "<<rand()%max;
}
