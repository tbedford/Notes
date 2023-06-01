## Event processing design patterns

1. Copier
2. Filter
3. Splitter
4. Sharder
5. Merger

**Copier** - pretty simple. Copies events from one channel to two or more
channels. It duplicates events.

**Filter** - for incoming events, it filters out certain events. For
example, a filter may filter out bad events (events that do not have
the correct structure).

**Splitter** - a splitter is similar to a filter, but rather than just
not passing on events, it diverts events to certain streams depending
on the event type. For example, if you have events representing
factory items that have passed QC, and some that have failed QC, then
the splitter would send events to either the QC passed stream, or QC
failed stream, for further processing. An example of the further
processing might be to flag up a possible fault in the production
line.

**Sharder** - not quite sure how this would be implemented in
Quix. Usually used to implement fault-tolerance. Imagine you have a
sharder that splits events to two streams, processed by two consumer
groups for horizontal scaling and fault tolerance. Imagine one of
these consumer groups fails (for whatever reason). How would the
sharder route all events to the working deployment?

**Merger** - this takes two event streams and combines them into a
single event stream.

---
