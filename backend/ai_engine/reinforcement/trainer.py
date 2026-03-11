# ai_engine/reinforcement/trainer.py

from ai_engine.reinforcement.reward_engine import compute_reward


class RLTrainer:

    def update(self, action_id):

        reward = compute_reward(action_id)

        # simple adaptive exploration
        if reward > 2:
            exploration = 0.05
        elif reward < 0:
            exploration = 0.2
        else:
            exploration = 0.1

        return {
            "reward": reward,
            "exploration_rate": exploration,
        }