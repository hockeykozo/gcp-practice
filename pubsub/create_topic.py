# -*- coding:utf-8 -*-
from google.cloud import pubsub

def create_topic(topic_name):
  # Instantiates a client
  client = pubsub.Client()

  #initialize topic
  topic = client.topic(topic_name)
  
  # The name for the new topic
  assert not topic.exists()
  topic.create()           
  assert topic.exists() 

  print("Topic %s is created" % topic.name)

def create_subscription(topic_name,sub_name):
  client = pubsub.Client()
  topic = client.topic(topic_name)
  sub = topic.subscription(sub_name)
  assert not sub.exists()
  sub.create()
  assert sub.exists()

  print("Subscription %s is created" % sub.name)

def publish_message(topic_name, data):
  client = pubsub.Client()
  topic = client.topic(topic_name)

  assert topic.exists()
  data = data.encode('utf-8')

  message_id = topic.publish(data)

  print('Message {} published.'.format(message_id))


"""
def pull_message(topic_name,sub_name):
  client = pubsub.Client()

  topic = client.topic(topic_name)
  sub = client.subscription(sub_name)

  assert sub.exists()


def test():
  for topic in client.list_topics():
    for sub in topic.list_subscriptions():
      print("%s : %s") % (topic.name,sub.name)
"""

if __name__ == "__main__":
  client = pubsub.Client()
  topic_name = "tazoe_test_topic"
  sub_name = "tazoe_test_subscription"
#  create_topic("tazoe_test_topic")  
#  create_subscription(topic_name,sub_name)  
  publish_message(topic_name,"hello world")
