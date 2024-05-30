from time import sleep
from json import dumps
from kafka import KafkaProducer
import random
import six
import sys

if sys.version_info>=(3,12,0):
	sys.modules['kafka.vendor.six.moves']=six.moves

topic_name='test_topic3'
publisher_1 = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))

for e in range(1):
    publisher_1_data ={
    "publisher_id":'st1',
    "publisher_name":'Store 1',
    "publisher_address":'Store 1 Address',
    "txn_id":f"st1_{e}",
    "txn_amount": random.randint(100,1000)
    }
    print(publisher_1_data)
    publisher_1.send(topic_name, value=publisher_1_data)
    sleep(0.5)
