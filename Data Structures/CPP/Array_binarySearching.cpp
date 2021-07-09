#include <iostream>

using namespace std;

int binarySearch(int arr[], int n, int key)
{
    int s = 0;
    int e = n;

    while (s <= e)
    {
        int mid = (s + e) / 2;

        if (arr[mid] == key)
        {
            return mid;
        }
        else if (arr[mid] < key)
        {
            return mid + 1;
        }
        else if (arr[mid] > key)
        {
            return mid - 1;
        }
    }
    return -1;
}

int main()
{
    cout << "Enter the array size : ";

    int n;

    cin >> n;

    int arr[n];

    for (int i = 0; i <= n; i++)
    {
        cin >> arr[i];
    }
    cout << "\n";
    cout << "Your enterd value is : ";

    for (int i = 0; i <= n; i++)
    {
        cout << arr[i] << " ";
    }

    int key;
    cin >> key;

    cout << binarySearch(arr, n, key);

    return 0;
}