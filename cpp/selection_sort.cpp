#include <iostream>

using namespace std;

void selectionSort(int arr[], int len)
{
  for (int j = 0; j < len; j++) {
  int lowest_index = j;
    for (int i = j+1; i < len; i++) {
      if (arr[i] < arr[lowest_index]) {
        lowest_index = i;
      }
    }
    swap(arr[lowest_index], arr[j]);
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
  selectionSort(arr, len);
  cout << "Sorted Array:";
  for (int i = 0; i < len; i++) {
    cout << " " << arr[i];
  }
  cout << endl;
  return 0;
}
