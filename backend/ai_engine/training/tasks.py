from celery import shared_task
from ai_engine.training.train_model import train_risk_model


@shared_task(bind=True)
def train_models(self):

    train_risk_model()