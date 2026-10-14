from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

@dataclass
class Step:
    tool: str
    args: Dict[str, Any]
    ok: bool
    observation: str
    policy_violation: bool = False

@dataclass
class TaskResult:
    task_id: str
    success: bool
    steps: List[Step] = field(default_factory=list)
    cost_usd: float = 0.0
    latency_s: float = 0.0

ToolFn = Callable[[Dict[str, Any]], Dict[str, Any]]
