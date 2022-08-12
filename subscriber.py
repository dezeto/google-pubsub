import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError
from dotenv import load_dotenv

load_dotenv(verbose=True)

credential_path = os.getenv("CREDENTIAL_PATH")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

timeout = 5.0

subscriber = pubsub_v1.SubscriberClient()
subcription_path = os.getenv("SUBSCRIPTION_PATH")


def callback(message):
    print(f"Receieved message: {message}")
    print(f"data: {message.data}")

    if message.attributes:
        print("Attributes:")
        for key in message.attributes:
            value = message.attributes.get(key)
            print(f"{key}: {value}")

    message.ack()


streaming_pull_future = subscriber.subscribe(
    subcription_path, callback=callback)
print(f"Listening for messages on {subcription_path}")


with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()
