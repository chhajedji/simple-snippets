#include <iostream>

using namespace std;

void myswap(int &x, int &y) {
  cout << "Addresses in myswap:\t" << &x << " " << &y << endl;
  int temp = x;
  x = y;
  y = temp;
}

void falseswap(int x, int y) {
  cout << "Addresses in falseswap:\t" << &x << " " << &y << endl;
  int temp = x;
  x = y;
  y = temp;
}

int main(void)
{
  int a = 3, b = 12;
  cout << "Before swap values: " << a << " " << b << endl;
  cout << "Addresses in main:\t" << &a << " " << &b << endl;
  myswap(a, b);
  cout << "Values after myswap: "<< a << " " << b << endl;
  falseswap(a, b);
  cout << "Values after flaseswap : "<< a << " " << b << endl;
  return 0;
}
