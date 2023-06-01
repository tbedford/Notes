Quix:

- transport - Kafka
- computation engine - Python

Quix provides:

a good abstraction to enable data scientists to leverage streaming
without having to deal with the underlying distributed systems.

---

**Consumer group** - Kafka acts like queue, as each message is only
consumed by one consumer in the consumer group.


...


Status options:

[ QueuedForBuild, Building, Deleting, BuildFailed, BuildSuccessful, QueuedForDeployment, Deploying, Starting, DeploymentFailed, Running, Stopping, RuntimeError, Completed, Stopped ]

---

If you want Kafka to pick up from where it left off, rather than
whatever the latest event is, use:

``` python
topic_consumer = client.get_topic_consumer(topic_id_or_name = os.environ["input"], auto_offset_reset=qx.AutoOffsetReset.Earliest, consumer_group='test')
```

`qx.AutoOffsetReset.Earliest` goes back to the last commit marker, so
you will continue from where the last data was received, before you
shut down or rebooted.

## Install Quix Streams

python3 -m pip install quixstreams==0.5.3 


## Use cases

- Where you have disparate data sources producing data, and disparate
  data sinks consuming data. You need a data backbone or data bus to
  connect all these disparate services together in a unified way,
  simplifying architecture and reducing the complexity of system
  design.
  
  Notes, various services in the data processing pipeliune will
  process data from one or more topics and write it to one or more
  topics, which may then may then be processed in various ways by
  additional services. This creates a **graph** of services connected
  together via **topics** (persistent, time-ordered logs).

- Look for places where real-time data collection takes place
  e.g. credit card transactions, Oyster card (events), industrial
  process control e.g. temperature, flows, pressures (TimeseriesData)

- Look for use cases where a central data backbone is required within
  the organization i.e. multiple producers and consumers. Basically
  where Kafka would be a good use case.

- Real-time feedback loops. You can make decisions and create offers
  etc. while the customer is interacting with the site. You don't need
  to wait until some batch process runs before offering a flash sale,
  or making product recommendations - these can be done in real time.
  
- games are interesting event systems - a game is really just a whole
  series of events!
  

- Energy monitoring / billing
- Industrial manufacturing processes
- Call centre call monitoring (how many calls, how long was the average call, etc.)

events --> database --> record update events -> stream processing

## Deployment scenarios

1. Quix-hosted Kafka (Quix manages Kafka for you)
2. Company hosted Kafka (Kafka behind the firewall)
3. Kafka hosted in the cloud (e.g. Confluent)



## Concepts

### Stream

The topic "Streaming context" is a little confusing, as "streaming
context" isn't a thing, only "stream" is a thing:

https://quix.io/docs/client-library/features/streaming-context.html

It should just be renamed to "streams". A stream is the logical concept
that Quix Streams add to the idea of a topic. It allows you to
organize data more efficiently. For example, all data from car 1 is
written to stream 1. How this works is that when you create a stream,
the stream is allocated a unique ID. That stream ID is used as a
partitioning key that is used to select the underlying partition in
the topic. Quix Streams essentially chooses the partition for you
based on the stream ID. This is important because it means data
written (published ) to a stream is always written to the same
underlying partition. This means data will arrive in the order it is
published.

Note that if you had say three cars and the default 2 partitions, the
third car would be written to a partition, say 0, so there would be
two streams in a partition. This is fine, because it still means that
all of car 3 data will go to the same partition (partition 0), and
will therefore arrive in the order that the data was published.

The ability to add metadata to a stream is a nice feature, as it
allows you to further identify and organize your streams.

### Timestamp

### Replica

### Consumer group

### Producer

### Consumer




---

default partition in Quix for a topic is 2.

---

