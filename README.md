Steps followed: 
- Install & setup python3.11, IDE, Anaconda, podman (works like docker), etc., on mac.
- Commands: 
  - `pip install virtualenv`
  - `python3.11 -m venv venv`
  - Choose an interpretor in pycharm, preferably anaconda.
  - `source venv/bin/activate`
  - `python3 -m pip install apache-flink`
  - `pip3 install pyarrow`
  - Sometimes terminal may cache old state sometimes not reflecting new changes, so restart ide or create new terminal to run commands. 
  - If podman is installed fine, else clean uninstall and reinstall podman desktop again: https://github.com/containers/podman/issues/11319
  - `brew install kafka`
  - Good blog to setup Kafka in mac: https://learn.conduktor.io/kafka/how-to-install-apache-kafka-on-mac-with-homebrew/. Though I run kafka/zookeeper in containers (dockerfile), hence not needed.
  - `cd` into the root project directory and run: `podman-compose up --build --no-cache` to spin up the containers defined in compose file. 
  - If you get errors like container already running or port already used, change the port mapping or stop processes running in port using: `sudo lsof -i :<port_number>`, eg: `lsof -i :2181`. 
- A sample kafka producer code is written in producer.py file.
- Useful commands to check workings inside kafka container, you first need to go inside the container: 
  - `podman exec -it kafka /bin/bash`
  - `kafka-topics --bootstrap-server kafka:9092 --list`
  - `kafka-console-consumer --bootstrap-server localhost:9092 --topic topic_events_data --from-beginning`
  - `kafka-consumer-groups --bootstrap-server localhost:29092 --list`
  - `topic_events_data` is defined in the producer code. 
- Sample postgres table which can be created from getting inside postgres terminal: 
    - `podman exec -it postgres /bin/bash`
    - `psql -U postgres`
    - `CREATE TABLE events (id SERIAL PRIMARY KEY, event_id VARCHAR(50) NOT NULL, user_name VARCHAR(50) NOT NULL, location VARCHAR(100) NOT NULL);`
    - `select * from events;`


    
------------

Good blogs to read:
- https://www.redpanda.com/guides/event-stream-processing-flink-vs-spark
- https://www.datacamp.com/blog/flink-vs-spark
- https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/concepts/stateful-stream-processing/
- https://stackoverflow.com/questions/69854764/pyflink-performance-compared-to-scala

------------

Things to take care in future: 
- Anchor package versions using poetry.
- Handle parsing which involves pre/post processors calling external db's. 


