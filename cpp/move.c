#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

void move1(uint8_t* src, uint32_t bytes, uint8_t* dest)
{
	printf("Move 1");
	uint8_t *buf = (uint8_t *)malloc(bytes);

	for (uint32_t i = 0; i < (uint32_t)(bytes); i++) {
		buf[i] = src[i];
	}

	for (uint32_t i = 0; i < (uint32_t)(bytes); i++) {
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
	int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	int b[10];
	int c[10];
	move1(&a, 10*sizeof(int), &c);
	move2(&a, 10*sizeof(int), &b);

	for (int i = 0; i < 10; i += 1) {
		printf("b[%d]: %d\t", i, b[i]);
	}
	printf("\n");

	for (int i = 0; i < 10; i += 1) {
		printf("c[%d]: %d\t", i, c[i]);
	}
	printf("\n");
	return;
}
