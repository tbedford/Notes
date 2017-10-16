# Notes

Here is a collection of random notes/code samples that I will keep
here until I find a better place for them. I hope to have a website
up and running soon where a lot of this stuff can go.

## TODO

1. Ant Allocator - simple memory allocator + article ONGOING
   - Attempt 1 complete
   - Attempt 2 complete and documented. 
       - Requires more testing code.
       - Documentationneeds cleanup/editing.
2. DitaShark - ARCHIVED
3. MCDS - ARCHIVED

## Midnight code

Projects I can do late at night:

- Custom Emacs key bindings
- C colour printf
- A nice project idea: profile assets for a game: you generate a
  histogram of asset sizes. Could for example just try it on the Doom
  WAD and Quake PAK files


## Notes

# Ever expanding console memory

| Model         | Year   |  RAM (MB) | VRAM (MB) 
|---------------|:------:|:----------|:---------
| Playstation 1 |  1994  | 2         | 1 
| Playstation 2 |  2000  | 32        | 4 
| Playstation 3 |  2006  | 256       | 256 
| Playstation 4 |  2013  | 8000      | 256
| Playstation 5 |  2020? |  ??       | ??


| Model         | Year   |  RAM (MB) | VRAM (MB) 
|---------------|:------:|:----------|:---------
| Xbox          |  2001  | 64        | ? 
| Xbox 360      |  2005  | 512       | ? 
| Xbox One      |  2013  | 8000      | ?
| Xbox One X    |  2017  | 12000     | ?


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

