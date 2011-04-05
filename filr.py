import boto
from kombu import BrokerConnection, Exchange, Queue, Consumer

connection = BrokerConnection()
connection.connect()

channel = connection.channel()
exchange = Exchange(
    name="android", 
    type="fanout", 
    channel=channel, 
    durable=True,
)
exchange.declare()

channel = connection.channel()
queue = Queue(
    name='filr',
    exchange=exchange,
    durable=True,
    auto_delete=False,
    channel=channel,
    routing_key='filr',
)
queue.declare();

def fetch(b,m):
    print b,m

consumer = Consumer(
    channel=connection.channel(),
    queues=queue,
    auto_declare=False,
    callbacks = [fetch]
)
consumer.consume(no_ack=False);

while(True):
    connection.drain_events()
    pass

#execfile('.private-settings')

#sdb = boto.connect_sdb(key_id, sec_key)
#domain = sdb.create_domain('android')
#item = domain.new_item('kral_step1')

#for key,value in kral_step.items():
#    item[key] = value
