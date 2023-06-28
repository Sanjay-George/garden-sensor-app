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
