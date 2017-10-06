#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>

void* malloc(size_t sz, char *file, int line)
{
    void *p;
    void *(*libc_malloc)(size_t) = dlsym(RTLD_NEXT, "malloc");
    p = libc_malloc(sz);
    printf("malloc: %s %d %zu %p\n", file, line, sz, p);
    return p;
}

void free(void *p)
{
    printf("free: %p\n", p);
    void (*libc_free)(void*) = dlsym(RTLD_NEXT, "free");
    libc_free(p);
}

int main()
{
    void *m = malloc(1024, __FILE__, __LINE__);

    // do interesting stuff

    free(m);
    return 0;
}
