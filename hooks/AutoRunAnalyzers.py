from . import register_webhook
import os
import logging
import time

from thehive4py.models import CaseObservable

# Name of the Cortex instance as defined in TheHive's configuration
CORTEX_ID = os.environ["CORTEX_ID"]

# These analyzers will NEVER be ran automatically
SKIP_ANALYZERS = set(e.strip() for e in os.getenv("SKIP_ANALYZERS", "").split(","))

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if os.getenv("DEBUG", False) else logging.INFO)


@register_webhook("CaseArtifactCreation")
def auto_run_analyzers(event, thehive, cortex):
    # Build CaseObservable object
    observable = CaseObservable(json=event["object"])

    # Skip any observables that contain the "no-analyze" tag
    if "no-analyze" in observable.tags:
        logger.debug("Skipped analyzer jobs for Observable '%s'", observable.id)
        return

    # Run each available analyzer against the observable
    for analyzer in cortex.analyzers.get_by_type(observable.dataType):
        # Skip any analyzers that were defined above
        if analyzer.name in SKIP_ANALYZERS or analyzer.id in SKIP_ANALYZERS:
            logger.debug("Skipping Analyzer '%s'", analyzer.name)
            continue

        # Run the analyzer
        res = thehive.run_analyzer(CORTEX_ID, observable.id, analyzer.id)
        logger.debug(res.json())
        if res.status_code in [200, 201]:
            logger.info(
                "Started '%s' job for Observable '%s'", analyzer.name, observable.id
            )
        else:
            logger.warn(
                "Error occurred when starting '%s' job for Observable '%s'",
                analyzer.name,
                observable.id,
            )
        time.sleep(0.5)
