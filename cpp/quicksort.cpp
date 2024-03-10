#include <iostream>

using namespace std;

int partition(int *arr, int low, int high)
{
  // `lower_pointer` keeps track of the lowest position of numbers greater than pivot.
  int lower_pointer = low;

  // pivoting the array at `arr[high]`. If pivoting on some other
  // element, then include `arr[high]` in the comparison as well.
  for (int j = low; j < high; j++) {
    if (arr[j] < arr[high]) {
      swap(arr[lower_pointer], arr[j]);
      lower_pointer++;
    }
  }
  swap(arr[lower_pointer], arr[high]);
  return lower_pointer;
}

void quickSort(int *arr, int low, int high)
{
  if (low < high) {
    int part = partition(arr, low, high);

    quickSort(arr, low, part-1);
    quickSort(arr, part+1, high);
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
  quickSort(arr, 0, len-1);
  cout << "Sorted Array:";
  for (int i = 0; i < len; i++) {
    cout << " " << arr[i];
  }
  cout << endl;
  return 0;
}
