# Notes

TODO:

1. Ant Allocator - simple memory allocator
2. DitaShark - clean up project
3. MCDS - clean up project
4. Start blog via GitHub pages
5. Move public writing into repo (off cloud)
6. Move personal writing into private repo

Notes:

* powerline - using in terminal you need to install patched fonts. Plus you need to select the font for the terminal to use.

Scratchpad:

I was reading something on compression and it mentioned in passing that you can convert from base 10 to base 2 by simply dividing by the base to convert to, and then collecting the remainder digits. So for base 10 to base 2 conversion you simply keep dividing by two and collecting the remainders. I'd never heard of that before, so I had to try it out in code immediately, as it seemed like magic. I spent a few minutes coming up with some code to test it out and yes, it works! 

It seems like the sort of thing that should be doable in 3 lines or so, but my version is a bit long winded. It also seems like it should be amenable to recursion too. I'll come back to it at some point, but had to prove to myself that it worked.

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// size hardcoded at 8 bits

void to_binary (int *bin_array, unsigned int num)
{
    unsigned int base = 2;
    unsigned int res, rem;

    int i=7;
    while (num > 0)
    {
        res = num / base;
        rem = num % base;

        bin_array[i] = rem;
        i--;
        num = res;
    }
    
}

void clear_array (int *array)
{
    for (int i = 0; i < 8; i++)
    {
        array[i] = 0;
    }

}

void print_array (int *array)
{
    for (int i = 0; i < 8; i++)
    {
        printf("%d", array[i]);
    }
    printf("\n");    
}

int main (int argc, char **argv)
{
    int bin_array[8];

    clear_array(bin_array);
    to_binary(bin_array, 19);
    print_array(bin_array);
    
    return 0;
}
```





