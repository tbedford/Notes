# Notes

Here is a collection of random notes/code samples that I will keep
here until I find a better place for them. I hope to have a website
up and running soon where a lot of this stuff can go.

## Contact

My email is:

``` Bash
tony.bedford_NOSPAM AT live DOT co DOT uk
```

You will need to remove the _NOSPAM and replace the DOTs by actual
dots of course.

## TODO

1. Ant Allocator - simple memory allocator
2. DitaShark - clean up project
3. MCDS - clean up project
4. Start blog via GitHub pages
5. Move public writing into repo (off cloud)
6. Move personal writing into private repo

## Notes

* powerline - using in terminal you need to install patched
  fonts. Plus you need to select the font for the terminal to use.

* I noticed Microsoft are keeping all their .NET docs in GitHub now. I
  think that's a good idea and I need to write something up on that
  topic.

* Neocities.org - a real throw back. Wonderful idea and there's some
  real creativity there. 

* [NTP research](https://www.eecis.udel.edu/~mills/ntp.html)

## Presentations

Some recently watched presentations:

* [Excellent talk on Rust and Concurrency by David
  Sullins](https://www.youtube.com/watch?v=oIikwmeGVYY). As a
  programmer it's really important to understand concepts of
  Resources, Ownership, Lifetime, Scope - and this is critical in a
  concurrent context. One minor point, scope is not necessarily the
  same thing as lifetime, at least in C (you can have a static
  variable in a function with global lifetime but local scope).

* [Kavya Joshi on Keeping Time in Real
  Systems](https://youtu.be/BRvj8PykSc4). Great talk on clocks and
  clock synchronization in distributed systems.
  
* [You can be a kernel hacker by Julia
  Evans](https://www.youtube.com/watch?v=0IQlpFWTFbM). Wonderful talk
  by Julia Evans. She is a "high energy" presenter - you won't be
  bored. I really like it when Julia uses /proc to recover a deleted
  file. Cool. She is also very, very funny - the piece on how to
  submit a kernel patch around 18 minutes in is hilarious. I _loved_
  this talk! One of the best presenters I've seen in a while.
  
## Scratchpad (or a brain dump in progress)

Having written the basis of a simple memory allocator, I was thinking
about debugging memory allocations. Of course there are various tools
out there such as `dmalloc`, Electric Fence, Valgrind and so on. I had a 
quick look at `dmalloc` and realized I could spend a week figuring it out. So
I wondered what could be put together in a few minutes. Basically I 
wanted to at least print out the line number and file that a `malloc()` was
called from. 

The approach I took, which I think is quite common, is to interject
a fake malloc which does my tracing and possible other clever stuff, 
before calling the real `malloc()`. 

My first attempt used functions pointers and was an epic fail. I created
a `fake_malloc()` and the idea was to do this:

1. Set a function pointer `real_malloc` with `malloc`. `real_malloc` now
   points at `malloc` - if you call `real_malloc()`, `malloc()` actually gets
   called. This bit worked fine.
2. Create a new function `fake_malloc` which has my tracing in it. 
3. Set `malloc = fake_malloc`, so that whereever I have `malloc` my 
   `fake_malloc` would actually get called. I couldn't get this to work. 
   The compiler doesn't like you assigning something to `malloc` - even
   a function pointer.
   
I then tried another approach where I tried to #define malloc to
fake_malloc, but I couldn't quite get the syntax right to make this
work. Does anyone out there know?

So, after a bit of reading on Stack Overflow I discovered there are
another couple of cool ways you can do this. The first was using GCC's
--wrap=malloc option. This allows you to wrap any function with a
wrapper function of your own design. But, this only works for GCC. I'm
using `clang` on Mac and I couldn't find a similar option.

Anyway, I ended up modifiying something on Stack Overflow which seemed
to work fine on Mac.

Here's what I used:

``` C
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
```

It works fine, but there's a couple of problems:

1. I have to modify my original malloc calls to accept 
   the filename and line number as parameters. That's a bit
   of a no-no in a large codebase.
2. What other useful checks might I do in the fake malloc call?

You can build and run with:

``` Bash
clang -ldl fake_malloc.c -o test
./test
```

You do get a warning though when you compile. The system knows enough
to know that changing `malloc(size_t)` to `malloc(size_t, ...)` is
probably a dodgy thing to do: 

``` Bash
fake_malloc.c:5:7: warning: incompatible redeclaration of library function
      'malloc' [-Wincompatible-library-redeclaration]
```

The code runs though.

It also worked without the `-ldl` option. 

So, a work in progress. Maybe it's time to learn Valgrind?
   

xxx

Brain malfunction ...

