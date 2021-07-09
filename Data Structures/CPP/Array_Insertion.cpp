// Array Insertion in unsorted

#include <bits/stdc++.h>

using namespace std;

int sortElement(int arr[], int n, int key, int capacity)
{
    if (n >= capacity)
    {
        return n;
    }

    arr[n] = key;
    return (n + 1);
}

int main()
{
    int arr[20] = {1, 3, 5, 7, 23, 87, 7};

    int capacity = sizeof(arr) / sizeof(arr[0]);

    int n = 20;

    int key = 29;

    for (int i = 0; i < n; i++)
    {
        cout << i << " : " << arr[i] << endl;
    }
    cout << "\nAfter insertion" << endl;
    n = sortElement(arr, n, key, capacity);

    for (int i = 0; i < n; i++)
    {
        cout << i << " : " << arr[i] << endl;
    }

}
