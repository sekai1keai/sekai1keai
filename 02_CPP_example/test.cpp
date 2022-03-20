#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char name[10];
    cin.getline(name, 10);

    name[0] = cin.get();
    cout << name;
    
    return 0;
}