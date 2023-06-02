import pulumi
from services.events.rules import EventRulesProperties, EventRule
import pulumi.automation as auto


def ensure_plugins():
    ws = auto.LocalWorkspace()
    ws.install_plugin("aws", "v4.0.0")


event_rule_props = EventRulesProperties(description="My Event Rule", event_pattern="...", is_enabled=True,
                                        name="my-event-rule", )


def run_program():
    event_rule = EventRule(name="vincents-event-rule", props=event_rule_props).create_rule()
    pulumi.export("event_rule_arn", event_rule.arn)


project_name = "inline_s3_project"
stack_name = "dev"
stack = auto.create_or_select_stack(stack_name=stack_name, project_name=project_name, program=run_program)

stack.workspace.install_plugin("aws", "v4.0.0")

stack.set_config("aws:region", auto.ConfigValue(value="eu-west-1"))
stack.refresh(on_output=print)
up_res = stack.up(on_output=print)
