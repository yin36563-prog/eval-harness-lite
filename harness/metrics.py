from __future__ import annotations
from typing import List, Dict, Any
from .types import TaskResult

def summarize(results: List[TaskResult]) -> Dict[str, Any]:
    n = len(results) or 1
    successes = sum(1 for r in results if r.success)
    unauth = sum(sum(1 for s in r.steps if s.policy_violation) for r in results)
    total_steps = sum(len(r.steps) for r in results) or 1
    costs = [r.cost_usd for r in results if r.success]
    return {
        "tasks": len(results),
        "success_rate": round(successes / n, 4),
        "unauthorized_steps": unauth,
        "unauthorized_rate": round(unauth / total_steps, 4),
        "cost_per_success": round(sum(costs) / len(costs), 4) if costs else None,
        "avg_latency_s": round(sum(r.latency_s for r in results) / n, 4),
    }
