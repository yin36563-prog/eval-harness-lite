"""Minimal runner with allowlist + resource ACL hooks."""
from __future__ import annotations
import time
from typing import Any, Dict, List, Set
from .types import Step, TaskResult, ToolFn

def run_task(
    task_id: str,
    plan: List[Dict[str, Any]],
    tools: Dict[str, ToolFn],
    allow_tools: Set[str],
    forbid_resource_prefixes: Set[str],
    success_check,
    cost_per_step: float = 0.01,
) -> TaskResult:
    steps: List[Step] = []
    t0 = time.time()
    for call in plan:
        name = call["tool"]
        args = dict(call.get("args") or {})
        if name not in allow_tools:
            steps.append(Step(name, args, False, "tool not allowed", True))
            break
        # naive ACL: string args starting with forbidden prefix
        violated = False
        for v in args.values():
            if isinstance(v, str):
                for p in forbid_resource_prefixes:
                    if v.startswith(p):
                        violated = True
        if violated:
            steps.append(Step(name, args, False, "resource ACL blocked", True))
            break
        if name not in tools:
            steps.append(Step(name, args, False, "tool missing", False))
            break
        out = tools[name](args)
        steps.append(Step(name, args, bool(out.get("ok")), str(out.get("obs")), False))
        if not out.get("ok"):
            break
    success = False
    try:
        success = bool(success_check(steps))
    except Exception:
        success = False
    return TaskResult(
        task_id=task_id,
        success=success and not any(s.policy_violation for s in steps),
        steps=steps,
        cost_usd=round(cost_per_step * max(len(steps), 1), 4),
        latency_s=round(time.time() - t0, 4),
    )
