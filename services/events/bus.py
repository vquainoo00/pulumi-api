from typing import Optional, Mapping
from pulumi_aws.cloudwatch import EventBus
from pydantic import BaseModel


class EventBusProperties(BaseModel):
    """Properties for an Event Bus."""

    opts: Optional[Mapping[str, str]] = None
    event_source_name: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CustomEventBus(EventBus):
    """
    Custom AWS Event Bus class that inherits from pulumi_aws.cloudwatch.EventBus.

    :param bus_name: The name to assign to the event bus.
    :param props: An instance of `EventBusProperties` containing the properties to apply to the bus.
    """

    def __init__(self, resource_name: str, props: EventBusProperties):
        super().__init__(
            resource_name=resource_name,
            event_source_name=props.event_source_name,
            tags=props.tags,
            opts=props.opts,
        )
