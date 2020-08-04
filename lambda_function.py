from base64 import b64decode
import os
import json
import logging
import boto3

from thehive4py.api import TheHiveApi
from cortex4py.api import Api as CortexApi

# Import custom Webhooks
from hooks import AutoRunAnalyzers
import hooks

# Required options
THEHIVE_URL = os.environ["THEHIVE_URL"]
THEHIVE_KEY = os.environ["THEHIVE_KEY"]
CORTEX_URL = os.environ["CORTEX_URL"]
CORTEX_KEY = os.environ["CORTEX_KEY"]

# Decrypt variables
THEHIVE_KEY = (
    boto3.client("kms")
    .decrypt(
        CiphertextBlob=b64decode(THEHIVE_KEY),
        EncryptionContext={
            "LambdaFunctionName": os.environ["AWS_LAMBDA_FUNCTION_NAME"]
        },
    )["Plaintext"]
    .decode("utf-8")
)
CORTEX_KEY = (
    boto3.client("kms")
    .decrypt(
        CiphertextBlob=b64decode(CORTEX_KEY),
        EncryptionContext={
            "LambdaFunctionName": os.environ["AWS_LAMBDA_FUNCTION_NAME"]
        },
    )["Plaintext"]
    .decode("utf-8")
)

# TheHive and Cortex instances
thehive = TheHiveApi(THEHIVE_URL, THEHIVE_KEY)
cortex = CortexApi(CORTEX_URL, CORTEX_KEY)

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if os.getenv("DEBUG", False) else logging.INFO)


def lambda_handler(event, context):
    # Validate event before proceeding
    logger.debug(event)
    if not all(key in event for key in ["object", "objectType", "operation"]):
        raise ValueError("Missing 'object', 'objectType', and/or 'operation' in event")

    # Parse and validate event type
    event_type = hooks.parse_event_type(event["objectType"], event["operation"])

    # Run each function for the given event type
    for func, _ in hooks.get_webhooks(event_type):
        func(event, thehive, cortex)
