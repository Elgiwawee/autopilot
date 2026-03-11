# actions/services/orchestrator.py

from actions.state_machine import assert_transition
from actions.executors.ec2 import execute_stop
from actions.simulations.ec2 import simulate_stop
from ai_engine.risk_engine import compute_final_risk

def run_execution(execution, aws_client):
    assert_transition(execution.state, "EXECUTING")
    execute_stop(execution, aws_client)
