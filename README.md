# Notes

Here is a collection of random notes/code samples that I will keep
here until I find a better place for them. I hope to have a website
up and running soon where a lot of this stuff can go.

## IoT notes

- Not all sensors have a MAC ID, and use of TCP/IP at edge of network is impractical.
- Because of very low cost requirements, sensors and IoT devices may
  be manufactired without references to centralized authority, leading
  to challenges around addressability.
- Machine to machine communication, rather than human to web server (therefore different requirement)
- Sensors are mostly generating data (asymmetrical comms)
- Sensors/control circuits need to be resposnive and deterministic (round trip nework protocols are not efficient here)
- Pub/Sub model works better than peer to peer
- Ultimately about connection into a network of unparalleled size


Architecture

- smart sensors (packet pumps) wirelessly feeding into router
- smart sensors have limited to no permanent storage
- routers have permanent storage so they can cache
- routers can transmit packet stream to pub/sub network
- smartphone (or smartphone type device) could become the router/concentrator
- management of software (updates, patches etc), device connections, device discovert is a big challenge
- we could be looking at 700+ billion IoT devices
- sensors need to be cheap enough to be disposable (they can easily be lost or damaged), whereas smart phone is not disposable
- sensor data is often infrequent, and tiny, compared to Internet human oriented apps such as web browsing and video streaming
- cost, battery life. 
- often sensor data will be quite compact - a few hundred bytes a day (but aggregated data from devices is vast)
- sensor will often be wireless (reduces cost and complexity, not need for cables, more practical)
- solar power
- example: oil rig would be a good testbed for low voltage wireless sensors connected to main logging unit
  - interesting issue. I put a level sensor in mud pit 3. Back at the
  logging unit how do I identify that sensor (it probably has a ID of
  some kind, but how to I associate that with location?)
- eample: car, multiple wireless sensors
- smart sensor would probably be Arduino (or less) in capability. Concentrators might be Pi level.




## RTOS course notes

1) Super loop
- Determinism (no)
- Responsiveness (variable)
- Polling periodicity - (variable: for loops, conditionals)

2) Foreground / background
- superloop + interrupts
- determinism affected by interrupts

3) RTOS
- deadlines (hard, form, soft)
- bounded response time to events
- kernel
  - objects (data types)
  - services (functions)
  - scheduler
    - algorithm
    - dispatcher
      - task context switching

kernel
- co-operative
- pre-emptive
  - low priority task can be pre-empted and a higher-priority task scheduled
  
Without RTOS you can end up with:
- excessive polling (can be alleviated with loop counters for multi-rate cycling) 
- busy waiting (waiting for some operation to complete - everything stops at this point)

Micrium
uC/OS-II
- 255 tasks - no two tasks can have the same priority
- 

## ISO dates on command line

Getting an ISO-8601 date/time:

date -u +"%Y-%m-%dT%H:%M:%SZ"

Output:

2011-08-27T23:22:37Z

or

date +%Y-%m-%dT%H:%M:%S%z

Output:

2011-08-27T15:22:37-0800

From:

https://stackoverflow.com/questions/7216358/date-command-on-os-x-doesnt-have-iso-8601-i-option#7216394

## UUID on command line

To generate UUID on command line use:

``` shell
uuidgen
```

Python:

``` python
import uuid
uuid.uuid4()
```

UUID('5361a11b-615c-42bf-9bdb-e2c3790ada14')

Need an article of parsing ISO-8601 date and time.

Worth scraping at some point?:

http://web.archive.org/web/20061008122852/http://www.diveintomark.org:80/archives/
http://web.archive.org/web/20090403051532/http://diveintomark.org/archives

Using Doxygen to analyze RocksDB:

1. brew update
2. brew install doxygen
3. doxygen --help
4. doxygen -g     (generates Doxyfile)
5. emacs Doxyfile
6. Set EXTRACT_ALL, EXTRACT_PRIVATE, RECURSIVE, HAVE_DOT, CALL_GRAPH, CALLER_GRAPH to YES
7. doxygen Doxyfile
8. Put kettle on
9. Browser -> index.html in html directory


Databases

Important to note, heavy write access patterns require a completely
different mindset, and database technology, to heavy read access. The
days of "one size (MySQL) fits all" are long gone. At web scale heavy
write use requires a different technology to the relational model.

---
Could be useful at some point:

https://en.wikipedia.org/wiki/Apache_Portable_Runtime

See also:

https://en.wikipedia.org/wiki/Memory_pool


PAXOS -> [RAFT](https://en.wikipedia.org/wiki/Raft_(computer_science))

Problem with some database as a service providers - Lock in!

[DuckDuckGo video (architecture)](https://www.youtube.com/watch?v=-IIE6IWi3-M)

---
- Buffered I/O = Stream I/O
    fopen, f*
- Unbuffered I/O = Low-level I/O
    open, close, read, write etc.

Tracing data into a file can be a bit of an overhead in a game. You
can get around this by creating your own buffer and using the
low-level I/O routines. When the buffer is full you write it out to
the filesystem/disk. You can put the dump procedure on its own thread.

- Synchronous I/O
- Asynchronous I/O

File loading:
- Seek time
- Time to Open file 
- Time to read data into memory

Due to these times game resources are often packed into a single file,
which reduces all three of the above.

Compressed data loads faster into memory as it is smaller. Yes, it
needs to be decompressed, but decompression times would be small
relative to disk access times. Note both PS4 and XBox One do *not* use
SSDs - so spinning lumps of magentized metal is still the norm
there. Note this is even more true for DVD and BluRay drives which are
very slow.

---

Stack-based allocator. Interesting. You would do something like this:

1. Load global data (think of it as game static)
2. Mark the stack point A
3. Load level 1
4. Mark the stack point B

At end of level 1:

1. Reset marker to A
2. Load level 2
3. Mark stack pointer C

etc.

This assumes all data for a level can fit on a stack. It also assumes
you are OK with a "level loading" message at the beginning of each
level.

---
Notes on strings:

* strcmp() is slow. Faster way: hash a string, hash another string,
then, when you need to compare, compare the hashes.

* Do the hash before run time if possible.

* CRC32 possible hashing algorithm.


Simple memory leak detector

depends on trace file:

    malloc:0x12345678:n bytes:__FILE__:__LINE__
    ...
    free:0x12345678:__FILE__:__LINE__
    ...

Process the trace file in an efficient way so that you match up
mallocs and frees. Every malloc should have a corresponding free.


John Lakos
Memory allocators
https://www.youtube.com/watch?v=nZNd5FjSquk

Shocked to see this:

http://www.cplusplus.com/reference/cuchar/

I thought the world was moving to UTF-8?

More trouble with C pointers:

``` C
int * my_func ()
{
    int *p;
    int my_array[1024];
    
    p = my_array;
    
    return p;
} // my_array destroyed (was local on stack). p points to something that
  // no longer exists - should this be a compile time error?
```

Static allocation in program code. 

``` C
typedef {unsigned char} byte;

memory_sz = 4 // MB

byte memory[memory_sz * 1024 * 1024]
```

Memory can then be accessed through array indexes.

An allocated memory block would then need to contain:

- index
- size (in bytes)

Free blocks would need the same info.

These memory blocks could be stored in another memory area, such as
another array. Wasteful but very simple.

So, with this approach you would give back a "handle" which is an
index into an array of memory blocks. The memory block data structure
would have an index and size into the main memory area.

You could then add allocated blocks to an allocated list and
freed blocks to a freed list

Look into Stack allocators
- Simple
- Downside you don't have arbitrary free
- Rollback marker 

Double-ended stack allocators
- bottom used for level allocations
- top used for temporary allocations freed every frame
- Hydro Thunder used this

Worth implementing a double-ended stack allocator class.

Follow up / update to pool allocators - I forgot to mention one big
advantage : no fragmentation!

Single-frame allocators
Double-buffered allocators

Aside: does anyone remember disk defragmenters? They were quite
commonly used on DOS machines.

Worth doing a little implementation for handle-based memory
allocation:

handle = ant_alloc (size_t size)
bool ant_free (handle)

Also need to do an application memory pool implementation in C and
C++.

Defragmenting allocator is feasible if you amortize the cost over
multiple frames.

Implement an extendable array:
- allocate new array of new required size
- copy data cross (in an optimized manner - use asm?)
- destroy the original array 

NOTE: when you grow the array do so by a reasonable amount e.g. double
it.

Aside: If you have two processes and one sends a message to the other
if you use a doubly-linked list (queue) and process 1 adds to head and
process 2 removes from tail then I don't believe any locking of the
list structure would be required. Would have to think through how this
is different to using mailboxes.

I'm thinking "local allocators" are basically application-level
allocators.

Implement a circular list (doubly-linked).


## Big O Notation

O(1) constant time. For example, adding a node to the beginning of a
list is a constant time operation. Walking a list is not a constant
time operation because the duration of the operation would depend on
how many items in the list.

## Single address space

* Single process with single address space shared with kernel. While
it may sound "dodgy" there are advantages to having a single address
space containing the main process and possibly threads, as well as the
kernel, all sharing the same address space:

1. You no longer need to copy (potentially) large chunks of data from
   one address space to another. You can simply pass a pointer around.
2. Switching between threads (lightweight processes) is much lower
   overhead than switching between memory protected (heavyweight)
   processes.
3. The memory manager is a lot simpler (and faster).

* Intel calling conventions (32-bit):

Caller:
  1. Push EAX, ECX, EDX
  2. Push arguments in reverse order
  3. Execute `call` (pushes return address onto stack).

Callee:
  1. Push EBP, EBX, EDI, ESI
  2. Push space for local variables
  3. Set EBP and ESP
  4. Return (and pop off the stack).

* Made a little progress on the "website". This is interesting though:

https://tools.pingdom.com/#!/bg1kRA/https://coffeeandcode.neocities.org

The bulk of the processing is for the very simple stylesheet and the
syntax colouring library. The syntax colouring is an annoying
overhead - but probably worth it. 

* It started with a simple question "I wonder what system calls
  RocksDB uses?" So by system calls I really mean library calls, which
  in turn call down to into the kernel (via syscalls) at some point
  (e.g. `sys_open`).  I couldn't think of a good way - you can grep
  for the usual suspects. Then I was thinking I could do something in
  Python and here's what I came up with in about five minutes:
  
``` python
#!/usr/bin/env python

import fileinput
import re
import os

calls = [
    r'open[\s]*?\([\s\S]*?\);',
    r'fopen[\s]*?\([\s\S]*?\);',
    r'read[\s]*?\([\s\S]*?\);',
    r'write[\s]*?\([\s\S]*?\);',
    r'sys_[\S]*?\([\s\S]*?\);'
]

def find_call (s, t, filename):
    m = re.search (s, t)
    if m:
        print ("File: "+filename)
        print (m.group(0))


# Read filename from stdin
for filename in fileinput.input():
    
    # chomp
    filename = filename.rstrip()
    
    # open file
    fin = open (filename, 'r')

    # Grab all of the things
    things = fin.read()

    # Search for system/library calls
    for call in calls:
        find_call(call, things, filename)
    
    # close down open files
    fin.close()
``` 
  
I could then run this like:

``` shell
find ../rocksdb -name "*.cc" | ./syscalls.py
```
  
This is obviously not a very good way to do it. But it does seem like
a thing you would want to know. 

A couple of other ways seem a bit tedious:

1. Manually grep through the code.
2. Use GDB to set a breakpoint and then step into the code (this seems especially tedious)

Surely there must be a better way?

I did find the [kernel grok site](http://syscalls.kernelgrok.com)
though. Very cool, but not quite what I was looking for.


## Markdown converter:

``` shell
brew install npm
npm install markdown-to-html -g
```

* `grip README.md --export --no-inline index.html` - This could be
  post-processed with a little Python to make the basis of a really
  simple static website generator (from GFM source).

* (Web tier, app tier, database tier) x N these days

    - Provision
    - Configure
    - Deploy

* NAT rewrites packet data but not application data (that may contain
  device network details).

* I didn't know this really basic thing - the following address
  ranges are for private use only!

    - 10.0.0 to 10.255.255.255
    - 172.16.0.0 to 172.31.255.255
    - 192.168.0.0 to 192.168.255.255 

These are forbidden from being routed over the public Internet! How
did I not know that!?

* Python libraries:
  - [Standard libraries](https://docs.python.org)
  - [Third-party](https://pypi.python.org)

* sudo less /etc/services - lists well-known ports. For example:

``` shell
sudo less /etc/services | grep mysql
```

* powerline - using in terminal you need to install patched
  fonts. Plus you need to select the font for the terminal to use.

* I noticed Microsoft are keeping all their .NET docs in GitHub now. I
  think that's a good idea and I need to write something up on that
  topic.

* Neocities.org - a real throw back. Wonderful idea and there's some
  real creativity there. 

* [NTP research](https://www.eecis.udel.edu/~mills/ntp.html)

  
## Threads vs event-driven (brief notes)

Event-driven is essentially:

1. Single-threaded
2. Non-blocking (asynchronous)
3. Has event loop

There are various ways event-driven software can be implemented.

Example - for an asynchronous read:

1. Main app sets up callback handlers to handle various 
   events of interest.
2. Perform reada(...) return immediately.
3. Main loop then sleeps (to conserve CPU/battery resource). 
4. I/O operation (reada()) completes and registered callback is invoked.
5. Callback runs and returns to main code.

Example - event polling from main loop

1. Main app sets up callback handlers to handle various 
   events of interest.
2. Main loop polls for events.
3. When event is received the corresponding event handler is invoked.

