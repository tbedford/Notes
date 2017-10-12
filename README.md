# Notes

Here is a collection of random notes/code samples that I will keep
here until I find a better place for them. I hope to have a website
up and running soon where a lot of this stuff can go.

## TODO

1. Ant Allocator - simple memory allocator + article ONGOING
2. DitaShark - ARCHIVED
3. MCDS - ARCHIVED

## Notes

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


* Thinking about Rust. First here's some C code:

``` C
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
```

Can you see the problem? With clang this compiles and actually runs
without error. The most likely reason it doesn't crash is because we
only just freed up that memory so nothing else is using it. If that
memory was in use we have potential data corruption or a crash. Of
course you could argue if you do stupid things like the above what do
you expect? This is true. It would be nice if the compiler caught such
problems. Could Rust do it better?

* Markdown converter:

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

## Presentations

Some recently watched presentations:

* [Deconstructing the OS](https://www.youtube.com/watch?v=h7D88U-5pKc)
  Absolutely brilliant talk by Alfred Bratterud. Alfred is a great
  presenter and this is a wonderful talk. Say what you like about the
  old DOS days but you _were_ in control of your system. You could
  write directly to the hardware (get a pointer to VGA memory, put a
  byte, and yay a pixel in one of 256 colours). Of course with that
  power came a certain danger. If a pointer went awry you could bring
  your system down. With a single (protected) address space that is
  less likely. DOS DPMI was the "protected mode" - you could have a
  crash control handler that would get invoked if your code started to
  write to places it shouldn't. Some of the "demoscene" demoes had
  built-in crash protection handlers, which was pretty cool. On DOS
  you could access hardware directly, and do things like intercept
  timer interrupts, reprogram the CTC, read and write various ports
  and so on. I do like the idea of Microkernels which this talk is
  about. Definitely one worth watching.
  
* [Unicode strings](https://www.youtube.com/watch?v=ysh2B6ZgNXk)
  Interesting presentation. Interesting that U+21B4 requires three
  bytes if encoded in UTF-8 and only two bytes with UTF-16 - which
  explains why UTF-16 is commonly used for non-latin (e.g. Japanese)
  character encoding - it's a lot more efficient at encoding those
  non-latin characters. I think what they are doing with
  [CopperSpice](http://www.copperspice.com/index.html) is also
  interesting. It's amazing the state (i.e. mess) of many legacy
  libraries when it comes to encodings. Also have a [YouTube
  channel](https://www.youtube.com/copperspice). Documentation on
  [string
  terminology](http://www.copperspice.com/docs/cs_string/overview_terminology.html).

* [Python, Fabric, Ansible by Tim
  Henderson](https://www.youtube.com/watch?v=4qav2EuXsGU) Not many
  presentations start with a poem, but this one does and it's
  great. Very good presenter who speaks clearly and at the right
  pace. Very useful presentation on managing systems.

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

