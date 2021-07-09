// Linear Search

#include <iostream>

using namespace std;

int main()
{
    int arr[4] = {1, 2, 3, 4};
    int check;

    cout << "Enter the element you want to search : ";
    cin >> check;

    for (int i = 0; i < 4; i++)
    {
        if (check == arr[i])
        {
            cout << "It is on index no. : " << i << " and the element is : " << check;
            break;
        }
    }
    return 0;
}