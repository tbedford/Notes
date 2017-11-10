#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BITS 8

void to_binary (int *bin_array, unsigned int num)
{
    unsigned int base = 2;
    unsigned int res, rem;

    int i=BITS-1;
    int entropy_bits = 0;
    while (num > 0)
    {
        res = num / base;
        rem = num % base;

        bin_array[i] = rem;
        i--;
        num = res;
        entropy_bits++;
    }
    printf("Entropy Bits: %d\n", entropy_bits);
}

void clear_array (int *array)
{
    for (int i = 0; i < BITS; i++)
    {
        array[i] = 0;
    }

}

void print_array (int *array)
{
    for (int i = 0; i < BITS; i++)
    {
        printf("%d", array[i]);
    }
    printf("\n");    
}

int main (int argc, char **argv)
{
    int bin_array[BITS];

    if (argc == 1)
    {
        printf("Example usage: to_binary 123\n");
        exit(-1);
    }

    clear_array(bin_array);
    to_binary(bin_array, atoi(argv[1]));
    print_array(bin_array);

    return 0;
}

