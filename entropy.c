#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main (int argc, char **argv)
{

    if (argc == 1)
    {
        printf("Example usage: entropy 123\n");
        exit(-1);
    }

    
    double x = atof(argv[1]);;

    double log2x = ceil(log10(x+1)/log10(2));

    printf ("entropy: %f\n", log2x);
    
    return 0;
}
