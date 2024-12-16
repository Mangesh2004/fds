#include <iostream>
#include <cstring>
using namespace std;
#define MAX 50

class Stack
{
private:
    char a[MAX];
    int top;

public:
    Stack()
    {
        top = -1;
    }

    void push(char x)
    {
        if (top >= MAX - 1)
        {
            cout << "Stack overslow" << endl;
            return;
        }
        a[++top] = x;
        cout << x << "is pushed into stack" << endl;
    }

    char pop(){
        return a[top--];
    }

    void reverse() const
    {
        for (int i = top; i >= 0; i--)
        {
            cout << a[i];
        }
    }

    void convert(char str[])
    {
        int k = 0;
        for (int j = 0; str[j] != '\0'; j++)
        {
            if (isalnum(str[j]))
            {
                str[k] = tolower(str[j]);
                k++;
            }
        }
        str[k] = '\0';
        cout << "comverted string is" << str << endl;
    };
    bool isPalindrome(char str[])
    {
       for(int i=0;str[i]!='\0';i++){
            push(str[i]);
       }

       for(int i=0;str[i]!='\0';i++){
        if(pop()!=str[i]){
            return false;
        }
       }
       return true;
    }
};

int main()
{
    Stack s;
    char str[MAX];
    cin.getline(str, MAX);

    s.convert(str);
    if(s.isPalindrome(str)){
        cout<<"string is a plaiondrome"<<endl;
    }else{
        cout<<"String is not a pliondfrome";
    }
    return 0;
}
