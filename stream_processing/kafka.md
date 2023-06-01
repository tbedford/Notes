## How to run Kafka

1. Start zookeeper:

``` sh
bin/zookeeper-server-start.sh config/zookeeper.properties
```

2. Start Kafka broker:

``` sh
bin/kafka-server-start.sh config/server.properties
```

3. Create a topic (optionally with compression):

``` sh
bin/kafka-topics.sh --create --topic nginx-log-topic-compression --bootstrap-server localhost:9092 --config compression.type=gzip
```

