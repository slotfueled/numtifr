#include<iostream>
using namespace std;
int N = 10;

int larges(int a[], int st){
	int la = a[st];
	for(int i = st+1;i<N;i++){
		if(la<a[i]){
			la = a[i];
			st = i;
		}
	}
	return st;
}

int main(){
	int arr[] = {1,200,33,4,-3,88,7,8,9,4};
	int j = larges(arr,0);
	int t=0;
	int n;
	cout<<"Enter the number of sorted element: ";
	cin>>n;
	for(int i = 0; i<n; i++){
		j = larges(arr,i);
		t = arr[i];
		arr[i]=arr[j];
		arr[j]=t;
		cout<<arr[i]<<" "<<endl;
	}
	return 0;
}
