# ai_engine/training/auto_retrain.py

import logging

from ai_engine.models import ActionOutcome
from ai_engine.training.train_model import train_risk_model

logger = logging.getLogger(__name__)


def maybe_trigger_retraining():

    samples = ActionOutcome.objects.count()

    if samples % 500 != 0:
        return

    logger.info("Triggering ML retraining with %s samples", samples)

    train_risk_model()