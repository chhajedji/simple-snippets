#include <iostream>

using namespace std;

int main()
{
  int x = 10;
  int *hi = &x;
  int &ref = x;

  cout << "ref: " << ref << endl;
  cout << "&ref: " << &ref << endl;
  cout << "*hi: " << *hi << endl;
  cout << "hi: " << hi << endl;

  if (&ref == hi) {
    cout << "Surprise, &ref == hi!!" << endl;
  }

  return 0;
}
