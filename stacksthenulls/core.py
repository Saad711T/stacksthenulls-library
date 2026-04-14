"""
stacksthenulls.core
Core public API for stacksthenulls.

This module exposes the main user-facing tools:
- Stack tracing
- Null inspection
- Execution timeline
- Result explanation
- Synthetic bug injection
- Data flow tracking
- Complexity analysis
- Void scan
"""

from __future__ import annotations

import ast
import inspect
import sys
import time
from functools import wraps
from typing import Any, Callable, Dict, List, Optional



# 1) Stack Visualizer

def trace_stack(func: Callable) -> Callable:
    """
    Decorator that prints a simple nested call trace.
    """

    call_depth = {"value": 0}

    @wraps(func)
    def wrapper(*args, **kwargs):
        indent = "    " * call_depth["value"]
        print(f"{indent}└── {func.__name__}()")
        call_depth["value"] += 1
        try:
            return func(*args, **kwargs)
        finally:
            call_depth["value"] -= 1

    return wrapper



# 2) Null Inspector

def nullcheck(value: Any, name: str = "value") -> Dict[str, Any]:
    """
    Inspect whether a value is None and return a small diagnostic report.
    """
    report = {
        "name": name,
        "is_null": value is None,
        "type": type(value).__name__,
        "repr": repr(value),
        "message": f"{name} is None" if value is None else f"{name} is not None",
    }
    return report





# 3) Execution Timeline

def timeline_run(func: Callable, *args, **kwargs) -> Dict[str, Any]:
    """
    Measure execution time and return a simple timeline report.
    """
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()

    return {
        "function": func.__name__,
        "started_at": start,
        "finished_at": end,
        "duration_sec": round(end - start, 6),
        "result": result,
    }


# 4) Why did this happen ? Analyzer

def explain(value: Any, name: str = "result") -> str:
    """
    Return a human-readable explanation for a value.
    """
    if value is None:
        return f"{name} became None. This usually means a function returned nothing or an expected value was missing."

    if isinstance(value, bool):
        return f"{name} is a boolean with value {value}."

    if isinstance(value, (int, float)):
        return f"{name} is numeric with value {value}."

    if isinstance(value, str):
        return f"{name} is a string of length {len(value)}."

    if isinstance(value, (list, tuple, set)):
        return f"{name} is a {type(value).__name__} containing {len(value)} item(s)."

    if isinstance(value, dict):
        return f"{name} is a dictionary containing {len(value)} key(s)."

    return f"{name} is of type {type(value).__name__}."



# 5) Synthetic Bug Generator
def inject_bug(kind: str = "null_pointer") -> str:
    """
    Simulate a bug pattern for testing/demo purposes.
    """
    supported = {
        "null_pointer": "Simulated null-pointer style issue: attempted operation on None.",
        "index_error": "Simulated index error: attempted out-of-range access.",
        "type_error": "Simulated type mismatch: unsupported operation between incompatible types.",
        "logic_bug": "Simulated logic bug: condition passes unexpectedly.",
    }

    if kind not in supported:
        raise ValueError(f"Unsupported bug type: {kind}")

    return supported[kind]





# 6) Data Flow Tracker

def track_flow(stages: List[str]) -> Dict[str, Any]:
    """
    Track a simple pipeline flow from stage to stage.
    """
    if not stages:
        return {"flow": [], "message": "No stages provided."}

    return {
        "flow": stages,
        "pretty": " -> ".join(stages),
        "steps_count": len(stages),
    }




# 7) Function Complexity Analyzer

def analyze(func: Callable) -> Dict[str, Any]:
    """
    Analyze a function source code in a lightweight way.
    """
    try:
        source = inspect.getsource(func)
        tree = ast.parse(source)
    except OSError:
        return {
            "function": func.__name__,
            "error": "Could not retrieve source code.",
        }

    loops = sum(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree))
    conditionals = sum(isinstance(node, ast.If) for node in ast.walk(tree))
    calls = sum(isinstance(node, ast.Call) for node in ast.walk(tree))
    returns = sum(isinstance(node, ast.Return) for node in ast.walk(tree))

    return {
        "function": func.__name__,
        "loops": loops,
        "conditionals": conditionals,
        "calls": calls,
        "returns": returns,
        "source_lines": len(source.splitlines()),
    }





# 8) Void Scan

def voidscan_code(source_code: str) -> Dict[str, Any]:
    """
    Scan source code for simple signs of 'voids':
    - pass
    - unused placeholders
    - empty except/finally blocks style hints
    """
    findings: List[str] = []

    if "pass" in source_code:
        findings.append("Found 'pass' statement(s), which may indicate unfinished logic.")

    if "TODO" in source_code or "FIXME" in source_code:
        findings.append("Found TODO/FIXME markers.")

    if "except:" in source_code:
        findings.append("Found bare except, which may hide real errors.")

    if not findings:
        findings.append("No obvious void patterns detected.")

    return {
        "findings": findings,
        "count": len(findings),
    }