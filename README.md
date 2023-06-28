# garden-sensor-app
A dummy app to learn Kafka, Telegraf, and influxDB.


## Installation
1. Prerequisites
    1. Python
    2. [Docker](https://docs.docker.com/engine/install/)
    3. [Telegraf](https://docs.influxdata.com/telegraf/v1.21/introduction/installation/)
2. Run `docker compose -f docker-compose.yaml` to run Apache Zookeeper and Apache Kafka on docker.
3. Run `docker start influxdb` to get influx DB running on docker.
    1. By default, it runs on port 8086. Open [localhost:8086](http://localhost:8086) to set up InfluxDB for the first time.
4. Run `telegraf --config  telegraf.conf` to get the telegraf agent to run according to the configuration specified.
5. Run the python program `python garden_sensor_gateway.py` to simulate sending sensor data.


## Platforms and Services used

### Apache Kafka

- Apache Kafka is an open-source distributed event streaming platform
used for high-performance data pipelines, streaming analytics, data
integration, and mission-critical applications.
- It allows client applications to read and write data from/to many
brokers simultaneously by distributing data across multiple Kafka
brokers.
- Kafka uses topics and partitions to organize and store data. Events
with the same key are written to the same partition, and consumers will
always read events from a partition in the order they were written.
- Kafka provides features like durability, scalability, fault
tolerance, and real-time data processing, making it suitable for
handling high-throughput and real-time data feeds.

### Apache Zookeeper

Apache ZooKeeper is an open-source server used for **coordinating and managing the configuration of cloud applications in a distributed environment**. It provides a reliable and simple service for distributed systems, offering a **hierarchical key-value store** used for a distributed configuration service, **synchronization service,** and **naming registry (URN)** for large distributed systems.

Alternatives:

- etcd - HA, strongly consistent distributed key-value store (CNCF project)
- Consul - highly available, distributed, multi-datacenter service discovery system with key/value store and health checking.

### InfluxDB

### Telegraf
