# Notes
Random notes

Simple heap memory allocator. Shows the basic design / data structures:

![Heap Memory Allocator](./Memory_allocator_1.png)

It helps to visualize the blocks (used and free) as separate from the nodes that manage the blocks.

Basic node data structure would look something like (in dodgy pseudo-code):

```C
// node for managing a block
typedef node_s struct {
    block_ptr *b; // points to a memory block
    unsigned int size; // size of block, look into size_t
    boolean_t used; // used: true or false
    node_s *next;
    node_s *prev;	   
 } node_t;
```

This is not the most efficient data structure though, but serves to get a very basic design up and running.  
