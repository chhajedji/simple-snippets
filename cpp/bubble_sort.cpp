#include <iostream>

using namespace std;

void bubbleSort(int arr[], int len)
{
  for (int j = len-1; j >= 0; --j)
  for (int i = 0; i <= j; ++i) {
    if (arr[i] > arr[i+1]) {
      swap(arr[i], arr[i+1]);
    }
  }
}

int main(void)
{
  int len;
  cout << "Length: ";
  cin >> len;
  int arr[len];
  cout << "Unsorted Array: ";
  for (int i = 0; i < len; i++) {
    cin >> arr[i];
  }
  bubbleSort(arr, len);
  cout << "Sorted Array:";
  for (int i = 0; i < len; i++) {
    cout << " " << arr[i];
  }
  cout << endl;
  return 0;
}
