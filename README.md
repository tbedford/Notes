# Notes

Here is a collection of random notes/code samples that I will keep
here until I find a better place for them. I hope to have a website
up and running soon where a lot of this stuff can go.

## Contact

My email is:

``` shell
tony.bedford_NOSPAM AT live DOT co DOT uk
```

You will need to remove the _NOSPAM and replace the DOTs by actual
dots of course.

## TODO

1. Ant Allocator - simple memory allocator + article ONGOING
2. DitaShark - ARCHIVED
3. MCDS - ARCHIVED

## Notes

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

