#include <iostream>

using namespace std;

class base_class {

public:
  virtual void display()
	{
		cout << "Virtual Base Class function.\n";
	}

  void print()
	{
	  cout << "Base_class print function.\n";
	}
};

class derived_class : public base_class {

public:
  void display()
  {
	cout << "Derived class display function.\n";
  }

  void print()
  {
	cout << "Derived class print function.\n";
  }
};

int main()
{
  derived_class child;

  child.base_class::display();
  child.display();
  child.print();
}
