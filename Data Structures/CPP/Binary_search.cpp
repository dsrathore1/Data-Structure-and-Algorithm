#include <iostream>

using namespace std;

int main()
{
    int arr[5] = {1, 2, 3, 4, 5};
    int first = 0;
    int key = 4;
    int mid;
    int last;

    do
    {
        mid = (first + last) / 2;

        if (arr[mid] == key)
        {
            cout << mid;
            break;
        }
        else if (arr[mid] < key)
        {
            return mid + 1;
            break;
        }
        else if (arr[mid] > key)
        {
            return mid - 1;
            break;
        }
    } while (first <= last);
}