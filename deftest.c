#include <stdio.h>
#include <stdlib.h>

void * test3 (size_t size, char *file, int line)
{
    void *p;

    p = malloc (size);
    printf("test3: %zu %s %d %p\n", size, file, line, p);

    return p;
}

#define test1(s)                              \
    test3((s), __FILE__, __LINE__)

int main (int argc, char **argv)
{
    void *p;
    
    p = test1(1024); 

    printf("%p\n", p);

    free (p);
    return 0;
}
