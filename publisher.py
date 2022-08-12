import os
from google.cloud import pubsub_v1
from dotenv import load_dotenv

load_dotenv(verbose=True)

credential_path = os.getenv("CREDENTIAL_PATH")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

publisher = pubsub_v1.PublisherClient()
topic_path = ""
topic_path = os.getenv("TOPIC_PATH")

data = "Book"
data = data.encode('utf-8')
attributes = {
    'book_name': 'helicopter',
    'author': 'dezeto',
    'publisher': 'DZ Corp.'
}

future = publisher.publish(topic_path, data, **attributes)
print(f"published message id {future.result()}")
