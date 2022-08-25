### Static Arrays

## Key features - 
* Contiguous area of memory space
* Address of the array is what needs to be stored somewhere
* Constant time access - $array\_addr + elem\_size*(i-first\_index)$
* Multi-dimensional arrays
* Row-major indexing vs Column-major indexing

### Complexities

|               |Add    |Remove |
|---            |---    |---    |
|**Begin**      | $O(n)$| $O(n)$|
|**Middle**     | $O(n)$| $O(n)$|
|**End**        | $O(1)$| $O(1)$|

### Dynamic Arrays
A solution to the problem of static arrays is to make it a dynamically allocated array. Basically, you can create an array pointer of a particular element size and then point it at a fixed-size array stored in dynamic memory.

The problem is - What if the size is unknown at the time of allocation? One might not know the max_size when allocating the array. 

There's a saying in computer science that goes like this -
> All problems in computer science can be solved by a level of indirection

Solution:  store a pointer to a dynamically allocated fixed-size array and replace it with a newly allocated array as and when required.

> C++ - This is exactly what a vector does !
> Python lists are dynamic arrays :)
> Java - ArrayList

### Runtime analysis

## Jagged arrays


