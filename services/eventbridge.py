from typing import Optional, Mapping, Sequence
from pydantic import BaseModel
from pulumi_aws.cloudwatch import EventTargetBatchTargetArgs, EventTargetDeadLetterConfigArgs, EventTargetEcsTargetArgs, \
    EventTargetInputTransformerArgs, EventTargetRetryPolicyArgs, EventTargetRunCommandTargetArgs, \
    EventTargetSqsTargetArgs, EventTargetHttpTargetArgs


class EventBusProperties(BaseModel):
    """Properties for an Event Bus."""

    event_source_name: Optional[str] = None,
    name: Optional[str] = None,
    tags: Optional[Mapping[str, str]] = None


class EventRulesProperties(BaseModel):
    """Properties for an Event Rule."""

    description: Optional[str] = None,
    event_bus_name: Optional[str] = None,
    event_pattern: Optional[str] = None,
    is_enabled: Optional[bool] = None,
    name: Optional[str] = None,
    name_prefix: Optional[str] = None,
    role_arn: Optional[str] = None,
    schedule_expression: Optional[str] = None,
    tags: Optional[Mapping[str, str]] = None


class EventTargetProperties(BaseModel):
    """Properties for an Event Target."""

    arn: Optional[str] = None,
    batch_target: Optional[EventTargetBatchTargetArgs] = None,
    dead_letter_config: Optional[EventTargetDeadLetterConfigArgs] = None,
    ecs_target: Optional[EventTargetEcsTargetArgs] = None,
    event_bus_name: Optional[str] = None,
    http_target: Optional[EventTargetHttpTargetArgs] = None,
    input: Optional[str] = None,
    input_path: Optional[str] = None,
    input_transformer: Optional[EventTargetInputTransformerArgs] = None,
    retry_policy: Optional[EventTargetRetryPolicyArgs] = None,
    role_arn: Optional[str] = None,
    rule: Optional[str] = None,
    run_command_targets: Optional[Sequence[EventTargetRunCommandTargetArgs]] = None,
    sqs_target: Optional[EventTargetSqsTargetArgs] = None,
    target_id: Optional[str] = None

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
