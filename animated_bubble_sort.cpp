#include <iostream>
#include<math.h>
#include <bits/stdc++.h>
#include<windows.h>
#include <cstdlib>
#include <unistd.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
void check_bubble(int arr[], int n,int moghaiese1, int moghaiese2){
	HANDLE h=GetStdHandle(STD_OUTPUT_HANDLE);
    int arr1[10];
	int maxEle = *max_element(arr, arr + n);
	for (int i=maxEle;i>=1;i--){
		if(i<10)
		cout<<" "<<i<<"|";
		else
		cout<<i<<"|";
		for(int j=0;j<=n-1;j++){
			if(arr[j]>=i){
				if(j==moghaiese2||j==moghaiese1){
					SetConsoleTextAttribute(h,11);
					cout<<"X   ";}
				else
					{SetConsoleTextAttribute(h,4);
					cout<<"X   ";}}
			else
				cout<<"    ";
		}
		cout<<"\n";
	}
	for (int i = 0; i < n + 3; i++)
   cout << "---";
   cout << "\n";
    
	
}
void ifchange_bubble(int arr[], int n,int moghaiese1, int moghaiese2,int changeposs){
	HANDLE h=GetStdHandle(STD_OUTPUT_HANDLE);
    int arr1[10];
	int maxEle = *max_element(arr, arr + n);
	for (int i=maxEle;i>=1;i--){
		if(i<10)
		cout<<" "<<i<<"|";
		else
		cout<<i<<"|";
		for(int j=0;j<=n-1;j++){
			if(arr[j]>=i){
				if(changeposs==true) {
					if(j==moghaiese2||j==moghaiese1){	
						SetConsoleTextAttribute(h,10);
						cout<<"X   ";}
					else
						{SetConsoleTextAttribute(h,4);
						cout<<"X   ";}}
				else{
					if(j==moghaiese2||j==moghaiese1){	
						SetConsoleTextAttribute(h,11);
						cout<<"X   ";}
					else
						{SetConsoleTextAttribute(h,4);
						cout<<"X   ";}
				}}
			else
				cout<<"    ";
		}
		cout<<"\n";
	}
	for (int i = 0; i < n + 3; i++)
   cout << "---";
   cout << "\n";
    
	
}
void gotchanged_bubble(int arr[], int n,int moghaiese1, int moghaiese2,int changeposs){
	HANDLE h=GetStdHandle(STD_OUTPUT_HANDLE);
    int arr1[10];
	int maxEle = *max_element(arr, arr + n);
	for (int i=maxEle;i>=1;i--){
		if(i<10)
		cout<<" "<<i<<"|";
		else
		cout<<i<<"|";
		for(int j=0;j<=n-1;j++){
			if(arr[j]>=i){
				
				if(j==moghaiese2||j==moghaiese1){	
					SetConsoleTextAttribute(h,10);
					cout<<"X   ";}
				else
					{SetConsoleTextAttribute(h,4);
					cout<<"X   ";}
				}
			else
				cout<<"    ";
		}
		cout<<"\n";
	}
	for (int i = 0; i < n + 3; i++)
   cout << "---";
   cout << "\n";
    
	
}
void bubble_sort(int arr[] , int n)
{
	int T,i,j;
	bool changepossibility=false;
		for(i=0;i<n;i++){
			for(j=0;j<n-i-1;j++){
				check_bubble(arr,n,j,j+1);
				usleep(1000000);
				system("cls");
				if(arr[j]>arr[j+1])
					{
					changepossibility=true;
					ifchange_bubble(arr,n,j,j+1,changepossibility);
					usleep(1000000);
					system("cls");
					T=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]= T;
					gotchanged_bubble(arr,n,j,j+1,changepossibility);
					usleep(1000000);
					system("cls");
					}
					}}
}



int main(int argc, char** argv) {
	int arr[10] = { 10, 9, 12, 4, 5, 2,
   8, 5, 3, 1 };
   int n = sizeof(arr) / sizeof(arr[0]);
   bubble_sort(arr,n);
   
	return 0;
}
