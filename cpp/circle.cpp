#include <iostream>
#include <cmath>

void draw(int);

int main()
{
	draw(20);
	return 0;
}

void draw(int r)
{
	int x, y;
	float curve = 2;
	std::cout << "Radius: " << r << std::endl;

	for (y = 2*r; y >= 0; y--) {
		// Getting x coordinate by solving for equation:
		// (x-r)^2 + (y-r)^2 = r^2
		// Center at (r, r).
		x = (int)((2*r - (r + sqrt(y*(2*r - y)))) * curve);

		for (int j = 0; j < x; j++) {
			std::cout << " ";
		}
		// std::cout << "x";

		for (int i = 0; i < ((int)(2*curve*r - 2*x)); i++) {
			std::cout << "+";
		}
		// std::cout << "x\n";
		std::cout << "\n";
	}
}
