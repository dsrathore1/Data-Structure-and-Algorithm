#include <bits/stdc++.h>
using namespace std;
void iSort(int myarr[], int nElements)
{
    int x, key, y;
    for (x = 1; x < nElements; x++)
    {
        key = myarr[x];
        y = x - 1;
        while (y >= 0 && myarr[y] > key)
        {
            myarr[y + 1] = myarr[y];
            y = y - 1;
        }
        myarr[y + 1] = key;
    }
}
void printArray(int myarr[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        cout << myarr[i] << " ";
    cout << endl;
}
int main()
{
    int myarr[] = {163, 152, 252, 356};
    int n = sizeof(myarr) / sizeof(myarr[0]);
    iSort(myarr, n);
    printArray(myarr, n);
    return 0;
}