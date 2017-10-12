#include<stdlib.h>

void my_func (int *ptr)
{
    free (ptr);
}

int main (int argc, char **argv)
{

    int *p = malloc (1024);

    my_func(p);

    *p = 1234;    
        
    return 0;
}
