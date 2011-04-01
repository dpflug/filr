import boto
from kombu import BrokerConnection, Exchange, Queue

connection = BrokerConnection()
channel = connection.channel()
android_exchange = Exchange("android")
consumer = Consumer(exchange)
android_queue = Queue("android", android_exchange)

execfile('.private-settings')

sdb = boto.connect_sdb(key_id, sec_key)
domain = sdb.create_domain('android')
item = domain.new_item('kral_step1')

for key,value in kral_step.items():
    item[key] = value
