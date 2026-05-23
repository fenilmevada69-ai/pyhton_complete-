#include<iostream>
using namespace std;



typedef struct Student {    
    string name;
    int age;
    bool flag;
};


class Teacher {
    public:
        string name;
        int age;
        bool isPass;
        Teacher(string name, int age, bool isPass) {
            this->name = name;
            this->age = age;
            this->isPass = isPass;
        }

        void display() {
            cout << "Name: " << this->name << endl;
            cout << "Age: " << this->age << endl;
        }

        void setAge(int age) {
            this->age = age;
        }
};

int main() {

    return 0;
}