from typing import Dict
import pulumi_aws as aws
from pydantic import BaseModel


class QueueProperties(BaseModel):
    """
    Pydantic model to define core properties for creating an AWS SQS queue.

    :param delay_seconds: The time in seconds that the delivery of all messages in the queue will be delayed.
    :param max_message_size: The limit of how many bytes a message can contain before Amazon SQS rejects it.
    :param message_retention_seconds: The number of seconds that Amazon SQS retains a message.
    :param receive_wait_time_seconds: The time for which a ReceiveMessage call will wait for a message to arrive.
    :param redrive_policy: A dictionary representing the configuration of the queue's dead-letter queue.
    :param tags: A dictionary of key-value pairs that represent metadata for the queue.
    """

    delay_seconds: int = 1
    max_message_size: int = 2048
    message_retention_seconds: int = 86400
    receive_wait_time_seconds: int = 1
    redrive_policy: Dict = {}
    tags: Dict = {}


class Queue(aws.sqs.Queue):
    """
    Custom AWS SQS queue class that inherits from pulumi_aws.sqs.Queue.

    :param queue_name: The name to assign to the queue.
    :param props: An instance of `QueueProperties` containing the properties to apply to the queue.
    """

    def __init__(self, queue_name: str, props: QueueProperties):
        super().__init__(
            queue_name,
            delay_seconds=props.delay_seconds,
            max_message_size=props.max_message_size,
            message_retention_seconds=props.message_retention_seconds,
            receive_wait_time_seconds=props.receive_wait_time_seconds,
            tags=props.tags,
        )


# Example usage:
queue_parameters = QueueProperties(delay_seconds=2, tags={"Environment": "production"})
queue = Queue("weekend_queue", queue_parameters)
