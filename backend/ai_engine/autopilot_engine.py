# ai_engine/autopilot_engine.py

import logging
from django.utils import timezone

from ai_engine.models import AutopilotRun
from ai_engine.autopilot.learning import learn_from_outcome
from cloud.services.accounts import get_active_cloud_accounts
from monitoring.services.metrics_collector import collect_metrics
from ai_engine.services.recommendation_service import generate_recommendations
from actions.services.decision_service import make_decision
from actions.services.executor import execute_plan

from ai_engine.autopilot.safety import can_act
from ai_engine.autopilot.rollback import rollback_if_needed
from ai_engine.time_gate import within_maintenance_window

logger = logging.getLogger(__name__)


class AutopilotEngine:
    """
    Main autonomous cloud optimizer.
    """

    def run_for_organization(self, organization):

        # Track this autopilot run
        run = AutopilotRun.objects.create(
            organization=organization
        )

        plans_generated = 0
        plans_executed = 0

        try:

            # 1️⃣ Global safety gate
            if not can_act(organization):
                logger.warning(
                    "Autopilot blocked by safety policy for org %s",
                    organization.id,
                )
                run.status = "blocked"
                run.finished_at = timezone.now()
                run.save()
                return

            # 2️⃣ Maintenance window check
            if not within_maintenance_window(organization):
                logger.info(
                    "Autopilot outside maintenance window for org %s",
                    organization.id,
                )
                run.status = "outside_window"
                run.finished_at = timezone.now()
                run.save()
                return

            accounts = get_active_cloud_accounts(organization)

            for account in accounts:

                logger.info(
                    "Running autopilot for account %s",
                    account.id,
                )

                try:

                    # 3️⃣ Collect metrics
                    metrics = collect_metrics(account)

                    # 4️⃣ Generate optimization plans
                    plans = generate_recommendations(
                        account,
                        metrics,
                    )

                    plans_generated += len(plans)

                    for plan in plans:

                        if not plan.resource:
                            logger.warning(
                                "Plan %s has no resource",
                                plan.id,
                            )
                            continue

                        # 5️⃣ Decision engine
                        decision = make_decision(plan)

                        if not decision.auto_execute_allowed:
                            logger.info(
                                "Plan %s blocked by decision engine",
                                plan.id,
                            )
                            continue

                        try:

                            execution = execute_plan(plan)

                            learn_from_outcome(plan, execution)

                        except Exception:

                            logger.exception(
                                "Execution failed for plan %s",
                                plan.id,
                            )

                            learn_from_outcome(
                                plan,
                                execution,
                            )

                except Exception:

                    logger.exception(
                        "Autopilot failed for account %s",
                        account.id,
                    )

            # 6️⃣ Post-action verification
            rollback_if_needed(organization)

            # Save metrics
            run.plans_generated = plans_generated
            run.plans_executed = plans_executed
            run.status = "completed"
            run.finished_at = timezone.now()
            run.save()

        except Exception:

            logger.exception(
                "Autopilot crashed for org %s",
                organization.id,
            )

            run.status = "failed"
            run.finished_at = timezone.now()
            run.save()