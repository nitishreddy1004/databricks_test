FROM bitnami/kafka:3.4

ENV KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181

# Copy SF_connect.properties to the Kafka config directory
COPY SF_connect.properties /opt/bitnami/kafka/config/

# Add plugin path to connect-standalone.properties
RUN echo "plugin.path=/opt/bitnami/kafka/libs" >> /opt/bitnami/kafka/config/connect-standalone.properties

# Download the Snowflake Kafka connector
RUN curl -o /opt/bitnami/kafka/libs/snowflake-kafka-connector-2.1.0.jar https://repo1.maven.org/maven2/com/snowflake/snowflake-kafka-connector/2.1.0/snowflake-kafka-connector-2.1.0.jar

# Copy the startup script and wait-for-it script
COPY --chmod=777 start-kafka.sh /opt/bitnami/scripts/start-kafka.sh
COPY --chmod=777 wait-for-it.sh /opt/bitnami/scripts/wait-for-it.sh

# Start Kafka with the custom configuration
CMD ["/opt/bitnami/scripts/wait-for-it.sh", "kafka:9092", "--", "/opt/bitnami/scripts/start-kafka.sh"]

