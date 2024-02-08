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

node *enq(node *h, int val)
{

  if (count == 0) {
	cout << "Creating new queue\n";
	h->val = val;
	h->next = NULL;
	++count;
	return h;
  }

  node *ptr = new node;
  ptr->val = val;
  ptr->next = h;

  ++count;

  return ptr;
}

int dq(node *h)
{
  node *curr = h;

  if (count == 0) {
	cout << "Queue empty, cannot remove.\n";
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
  cout << "Queue ";
	while(curr != NULL) {
	  cout << "\t-\t" << curr->val;
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
  cout << "1. Enqueue\t2. Dequeue\t3. Exit\n";
  cin >> input;
	switch (input) {
	case 1:
	  int num;
	  cout << "Enqueue value: ";
			  cin >> num;
	  head = enq(head, num);
	  disp(head);
	  break;
	case 2:
	  dq(head);
	  disp(head);
	  break;
	case 3:
	  return 0;
	default:
	  cout << "Idiot, put one of the requested inputs.\n";
	  disp(head);
	}
  }
  return 0;
}
