#include <iostream>

using namespace std;

int linearSearching(int arr[], int n, int key)
{
    for (int i = 0; i <= n; i++)
    {
        if (arr[i] == key)
        {
            cout << "Your searched value's index at : " ;
            return i;
        }
    }
    if (arr[n] != key)
    {
        cout << "Your entered value is not into the array and the index value is : ";
    }
    return -1;
}

int main()
{
    cout << "Enter the array : ";
    int n;
    cin >> n;
    int arr[n];

    for (int i = 0; i <= n; i++)
    {
        cin >> arr[i];
    }

    cout << "\n";
    cout << "Your enterd value is : ";

    for (int j = 0; j <= n; j++)
    {
        cout << arr[j] << " ";
    }

    cout << "\n";
    cout << "Enter your searching value : ";

    int key;
    cin >> key;

    cout << "\n";

    cout << linearSearching(arr, n, key) << endl;

    return 0;
}
