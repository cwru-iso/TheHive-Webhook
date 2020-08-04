# Webhook event types
EVENTS = {
    "AlertCreation": [],
    "AlertDelete": [],
    "AlertUpdate": [],
    "CaseArtifactCreation": [],
    "CaseArtifactDelete": [],
    "CaseArtifactJobCreation": [],
    "CaseArtifactJobDelete": [],
    "CaseArtifactJobUpdate": [],
    "CaseArtifactUpdate": [],
    "CaseCreation": [],
    "CaseDelete": [],
    "CaseTaskCreation": [],
    "CaseTaskDelete": [],
    "CaseTaskLogCreation": [],
    "CaseTaskLogDelete": [],
    "CaseTaskLogUpdate": [],
    "CaseTaskUpdate": [],
    "CaseUpdate": [],
}


def register_webhook(event_type, priority=10):
    if event_type not in EVENTS:
        raise ValueError("Unknown event type '{}'".format(event_type))

    def wrapper(func):
        EVENTS[event_type].append((func, priority))
        return func

    return wrapper


def get_webhooks(event_type):
    if event_type not in EVENTS:
        raise ValueError("Unknown event type '{}'".format(event_type))

    # Return webhook functions sorted by priority
    return sorted(EVENTS[event_type], key=lambda tup: tup[1])


def parse_event_type(object_type, operation):
    eventType = object_type + "_" + operation
    return "".join([i.title() for i in eventType.split("_")])
