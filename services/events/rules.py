import pulumi_aws as aws
from typing import Optional, Mapping
from pydantic import BaseModel


class EventRulesProperties(BaseModel):
    """Properties for an Event Rule."""

    description: Optional[str] = None
    event_bus_name: Optional[str] = None
    event_pattern: Optional[str] = None
    is_enabled: Optional[bool] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    role_arn: Optional[str] = None
    schedule_expression: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class EventRule(aws.cloudwatch.EventRule):
    """
    Custom AWS Event bridge rule class that inherits from pulumi_aws.cloudwatch.EventRule.

    :param name: The name to assign to the rule.
    :param props: An instance of `EventRulesProperties` containing the properties to apply to the rule.
    """

    def __init__(self, name: str, props: EventRulesProperties):
        super().__init__(
            name,
            description=props.description,
            event_pattern=props.event_pattern,
            is_enabled=props.is_enabled,
            name_prefix=props.name_prefix,
            role_arn=props.role_arn,
            schedule_expression=props.schedule_expression,
            tags=props.tags,
        )

    def create_rule(self):
        """
        Create the AWS EventBridge rule with the specified properties.

        :return: An instance of `pulumi_aws.cloudwatch.EventRule`.
        """
        return aws.cloudwatch.EventRule(
            self._name,  # Use the private name attribute
            description=self.description,
            event_pattern=self.event_pattern,
            is_enabled=self.is_enabled,
            name_prefix=self.name_prefix,
            role_arn=self.role_arn,
            schedule_expression=self.schedule_expression,
            tags=self.tags,
        )
