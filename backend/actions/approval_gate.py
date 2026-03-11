def approval_required(action_plan):
    policy = action_plan.resource.cloud_account.organization.autopilot_policy
    return policy.require_approval
