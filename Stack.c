#include<stdio.h>
int temp = 0;

void push(int ele) {
    if (temp == 4) {
        
    }
    arr[temp] = ele;
    temp++;
}

int main() {
    int arr[5];
    push(10);
    push(20);
    push(30);
    push(40);
    pop();
    
    return 0;
}