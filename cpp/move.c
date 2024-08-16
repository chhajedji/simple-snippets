#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

void move1(uint8_t* src, uint32_t len, uint8_t* dest)
{
	printf("Move 1");
	uint8_t *buf = (uint8_t *)malloc(sizeof(len));

	for (int i = 0; i < (uint32_t)(len/sizeof(uint8_t)); i++) {
		buf[i] = src[i];
	}

	for (int i = 0; i < (uint32_t)(len/sizeof(uint8_t)); i++) {
		dest[i] = buf[i];
	}

	free(buf);
}

void move2(uint8_t* src, uint32_t bytes, uint8_t* dest)
{
	printf("Move 2\n");
	// Destination is ahead of source in memory layout. Go from last
	// to first address.
	if (src < dest) {
		for (uint32_t i = bytes; i > 0; i--) {
			dest[i-1]  = src[i-1];
		}
		return;
	}
	for (uint32_t i = 0; i < bytes; i++) {
		dest[i]  = src[i];
	}
}

void main()
{
	int a[5] = {1, 2, 3, 4, 5};
	int b[5];
	int c[5];
	move1(&a, 5*sizeof(int), &c);
	move2(&a, 5*sizeof(int), &b);

	for (int i = 0; i < 5; i += 1) {
		printf("b[%d]: %d\t", i, b[i]);
	}
	printf("\n");

	for (int i = 0; i < 5; i += 1) {
		printf("c[%d]: %d\t", i, c[i]);
	}
	printf("\n");
	return;
}
