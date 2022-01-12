#include<iostream>
#include<chrono>
using namespace std;

int fib(int n){
	if(n<2){
		return n;
	}
	return fib(n-1)+fib(n-2);
}

int fibd(int n){
	int a=0,b=1,c;
	if(n==0)
		return a;
	for(int i=2;i<=n;i++){
		c=a+b;
		a=b;
		b=c;
	}
	return b;
}
int main(){
	chrono::time_point<chrono::system_clock> start, end;

	int n;
	cout<<"Enter the number of term of fibonnaci: ";
	cin>>n;

	start = chrono::system_clock::now();
	cout<<"f(n) = "<< fib(n)<<'\n';
	end = chrono::system_clock::now();

	chrono::duration<double> dur = end-start;
	cout<<"time taken for compute using recursion: "<<dur.count()<<"s\n";


	start = chrono::system_clock::now();
	cout<<"f(n) = "<< fibd(n)<<'\n';
	end = chrono::system_clock::now();

	dur = end-start;
	cout<<"time taken for compute using dynamic programming: "<<dur.count()<<"s\n";
}

