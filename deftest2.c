#include <stdio.h>
#include <stdlib.h>

void * malloc2 (size_t size, char *file, int line)
{
    void *p;

    p = malloc (size);
    printf("test3: %zu %s %d %p\n", size, file, line, p);

    return p;
}

#define malloc(s)                              \
    malloc2((s), __FILE__, __LINE__)

int main (int argc, char **argv)
{
    void *p;
    
    p = malloc(1024); 

    printf("%p\n", p);

    free (p);
    return 0;
}
