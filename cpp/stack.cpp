#include <iostream>

using namespace std;

typedef class node {
public:
  int val;
  class node *next;
  node()
  {
	val = 0;
	next = NULL;
  }
} node;

unsigned int count = 0;

bool empty(node *head)
{
  return (count == 0 ? true : false);
}

int push(node *h, int val)
{
  node *curr = h;

  if (count == 0) {
	cout << "Creating new stack\n";
	curr->val = val;
	curr->next = NULL;
	++count;
	return 0;
  }

  while (curr->next != NULL) {
	curr = curr->next;
  }
  node *ptr = new node;
  curr->next = ptr;
  ptr->val = val;

  ++count;

  return 0;
}

int pop(node *h)
{
  node *curr = h, *prev;

  if (count == 0) {
	cout << "Stack empty, cannot pop.\n";
	return 1;
  }

  if (curr->next == NULL) {
	curr->val = -1;
	--count;
	return 0;
  }

  while (curr->next->next != NULL) {
	curr = curr->next;
  }

  delete curr->next;
  curr->next = NULL;
  --count;

  return 0;
}

int disp(node *h)
{
  node *curr = h;
  if (count == 0) {
	return 1;
  }
  cout << "Stack ";
	while(curr != NULL) {
	  cout << "\t->\t" << curr->val;
	  curr = curr->next;
	}
	cout << "\n";
	return 0;
}

int main()
{
  node *head = new node;
  head->val = -1;
  int input;
  while (true) {
  cout << "1. Push\t2. Pop\t3. Exit\n";
  cin >> input;
	switch (input) {
	case 1:
	  int num;
	  cout << "Push value: ";
			  cin >> num;
	  push(head, num);
	  disp(head);
	  break;
	case 2:
	  pop(head);
	  disp(head);
	  break;
	case 3:
	  return 0;
	default:
	  disp(head);
	}
  }
  return 0;
}
