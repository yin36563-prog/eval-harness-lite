#!/usr/bin/env python3
"""Demo: successful path + unauthorized path."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from harness import run_task, summarize

def get_order(args):
    return {"ok": True, "obs": f"order {args['order_id']} paid"}

def refund(args):
    return {"ok": True, "obs": f"refunded {args['amount']}"}

def write_audit(args):
    return {"ok": True, "obs": "audit written"}

TOOLS = {"get_order": get_order, "refund": refund, "write_audit": write_audit}
ALLOW = set(TOOLS)
FORBID = {"tenantB:"}

def ok_check(steps):
    return len(steps) >= 3 and all(s.ok for s in steps)

good = run_task(
    "refund-01",
    [
        {"tool": "get_order", "args": {"order_id": "tenantA:1001"}},
        {"tool": "refund", "args": {"order_id": "tenantA:1001", "amount": 20}},
        {"tool": "write_audit", "args": {"order_id": "tenantA:1001"}},
    ],
    TOOLS, ALLOW, FORBID, ok_check,
)

bad = run_task(
    "refund-leak",
    [
        {"tool": "get_order", "args": {"order_id": "tenantB:9"}},
    ],
    TOOLS, ALLOW, FORBID, ok_check,
)

print(summarize([good, bad]))
print("good success", good.success, "bad success", bad.success, "bad violation", bad.steps[0].policy_violation)
