#include <iostream>

using namespace std;


/*
 * Operator Overloading.
 */

class complex {
private:
    float r, i;

public:
    complex(float r, float i) {
        this->r = r;
        this->i = i;
    }

    // This is needed in case object is created without any parameters.
    complex() {}

    void displaydata() {
        cout << "real part = " << r << endl;
        cout << "imaginary part = " << i << endl;
    }

    // Operator overloading for the addition operator '+'
    complex operator+(const complex& c) {
        return complex(r + c.r, i + c.i);
    }
};

class easy {
    private:
        float a, b;
        float val;

    public:
        easy (float a, float b)
        {
            val = a + b;
        }
        easy() {}

        void disp()
        {
            cout << endl << "Sum is: " << val << endl;
        }
};

class flip {
    public:
        float a, b;
        flip(float a, float b)
        {
            this->a = b;
            this->b = a;
        }

        void print_val()
        {
            cout << "a: " << this->a << "\tb: " << this->b << endl;
        }
};

void overload_me()
{
  cout << "Hi\n";
}

void overload_me(string a)
{
  cout << a << endl;
}

int main() {
    complex a(2, 3);
    complex b(3, 4);
    complex c = a + b; // This line demonstrates the overloaded '+' operator
    c.displaydata();
    easy num(3, 2.3);
    num.disp();

    flip me(3, 4);
    me.print_val();

    overload_me();
    overload_me("New String");

    return 0;
}
