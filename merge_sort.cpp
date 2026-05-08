#include<iostream>
using namespace std;

void print(int a[], int s) {
    for(int i=0; i<s; i++) {
        cout << a[i] << " ";
    }cout<<endl;
}

int main() {
    int a[] = {10,30,40,60,70};
    int b[] = {5,20,37,45,90};
    int c[10];
    int k=0;
    for(int i=0, j=0; i<5 || j<5; ) {
        if(i==5 && j==4) {
            c[k] = b[j]; 
            break;
        }
        else if(j==5 && i==4) {
            c[k] = a[i]; 
            break;
        }
        if(a[i] < b[j]) {
            c[k] = a[i];
            k++;
            i++;
        } else {
            c[k] = b[j];
            j++;
            k++;
        }
    }
    print(c, 10);
}