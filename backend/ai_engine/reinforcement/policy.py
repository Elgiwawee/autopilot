import random


class OptimizationPolicy:

    def __init__(self):
        self.exploration_rate = 0.1

    def should_execute(self, risk_score, estimated_savings):

        if risk_score > 0.7:
            return False

        if estimated_savings < 5:
            return False

        # exploration
        if random.random() < self.exploration_rate:
            return True

        return True