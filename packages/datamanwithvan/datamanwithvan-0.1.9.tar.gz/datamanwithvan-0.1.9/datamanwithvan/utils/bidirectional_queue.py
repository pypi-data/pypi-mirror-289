import asyncio
import random
import time
import logging

# Section 30 : Before anything else, set up the logger...
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_format = logging.Formatter(
    '%(asctime)s - %(name)s (%(levelname)s) : %(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)
try:
    file_handler = logging.FileHandler("/var/log/datamanwithvan/dmwv.log")
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s (%(levelname)s) : %(message)s')
    logger.addHandler(file_handler)
except Exception as e:
    logger.error(f"Error while trying to open log file: {e}")
console_handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
# End of Section 30


class BidirectionalQueue:
    """A simple class managing two-way
    communication using two asyncio queues."""

    def __init__(self):
        # Two separate queues for bidirectional communication
        self.queue_to_consumer = asyncio.Queue()  # Producer to Consumer
        self.queue_to_producer = asyncio.Queue()  # Consumer to Producer


class Producer:
    """The Producer class sends and receives messages asynchronously."""

    def __init__(self, communication: BidirectionalQueue, whoami):
        self.communication = communication
        self.whoami = whoami

    async def produce(self):
        """Asynchronously produce messages for the consumer."""
        for i in range(4):
            await asyncio.sleep(random.uniform(0.5, 1.5))
            message = f"Message {i} from Producer"
            f"{self.whoami} at {time.strftime('%X')}"
            print(f"[Producer] Sending: {message}")

            # Send message to the consumer
            await self.communication.queue_to_consumer.put(message)

            # Wait for acknowledgment from the consumer
            acknowledgment = await self.communication.queue_to_producer.get()
            print(f"[Producer] Received acknowledgment"
                  f"{self.whoami}: {acknowledgment}")

        # Send stop signal
        await self.communication.queue_to_consumer.put("STOP")
        print("[Producer] Sent STOP signal to Consumer.")


class Consumer:
    """The Consumer class sends and receives messages asynchronously."""

    def __init__(self, communication: BidirectionalQueue, whoami):
        self.communication = communication
        self.whoami = whoami

    async def consume(self):
        """Asynchronously consume messages from the producer."""
        while True:
            # Wait for a message from the producer
            message = await self.communication.queue_to_consumer.get()
            if message == "STOP":
                print("[Consumer] Received STOP signal. Stopping consumption.")
                break

            print(f"[Consumer] Received: {message}")

            # Send acknowledgment back to the producer
            acknowledgment = f"Ack '{message}'"
            f"{self.whoami} at {time.strftime('%X')}"
            await self.communication.queue_to_producer.put(acknowledgment)
            print(f"[Consumer] Sent acknowledgment {self.whoami}: "
                  f"{acknowledgment}")
