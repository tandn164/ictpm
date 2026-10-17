#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared helpers for risk tools."""
from __future__ import annotations

from pathlib import Path

MODULE = Path(__file__).resolve().parents[1]
JSON_PATH = MODULE / "artifacts" / "01_risk.json"
TEMPLATE_PATH = MODULE / "templates" / "risk-management.xlsx"
OUT_PATH = MODULE / "artifacts" / "01_risk_draft.xlsx"

PROBABILITIES = ("High", "Middle", "Low")
IMPACTS = ("Big", "Middle", "Small")
STRATEGIES = ("Avoid", "Transfer", "Mitigate", "Accept")
DEFAULT_CATEGORIES = ("System", "Technical", "Organization")

PRIORITY_MATRIX = {
    ("High", "Big"): "A",
    ("High", "Middle"): "A",
    ("High", "Small"): "B",
    ("Middle", "Big"): "A",
    ("Middle", "Middle"): "B",
    ("Middle", "Small"): "C",
    ("Low", "Big"): "B",
    ("Low", "Middle"): "C",
    ("Low", "Small"): "C",
}


def compute_priority(probability: str, impact: str) -> str:
    return PRIORITY_MATRIX.get((probability.strip(), impact.strip()), "")


def as_plain_text(cur, default: str = "") -> str:
    if cur is None:
        return default
    if isinstance(cur, dict):
        if "value" in cur or "proposed" in cur:
            v = cur.get("value")
            if v is None or (isinstance(v, str) and not str(v).strip()):
                v = cur.get("proposed")
            if v is None:
                return default
            if isinstance(v, (list, tuple)):
                return ", ".join(str(x) for x in v)
            if isinstance(v, dict):
                return as_plain_text(v, default=default)
            return str(v).strip()
        return default
    if isinstance(cur, (list, tuple)):
        return ", ".join(str(x) for x in cur)
    return str(cur).strip()


def next_risk_id(risks: list) -> str:
    nums = []
    for r in risks:
        rid = str(r.get("id") or "")
        if rid.upper().startswith("R-"):
            tail = rid.split("-", 1)[-1]
            if tail.isdigit():
                nums.append(int(tail))
    n = (max(nums) + 1) if nums else 1
    return f"R-{n:03d}"


def normalize_risk(raw: dict, *, assign_id: str | None = None) -> tuple[dict, list[str]]:
    """Chuẩn hóa 1 rủi ro + tính priority. Trả (risk, errors)."""
    errors: list[str] = []
    category = as_plain_text(raw.get("category"))
    driver = as_plain_text(raw.get("driver"))
    risk_txt = as_plain_text(raw.get("risk"))
    prob = as_plain_text(raw.get("probability"))
    impact = as_plain_text(raw.get("impact"))
    strategy = as_plain_text(raw.get("strategy"))

    if not driver:
        errors.append("Thiếu driver (nguyên nhân/kích hoạt)")
    if not risk_txt:
        errors.append("Thiếu risk (hậu quả)")
    if not category:
        errors.append("Thiếu category")
    if prob not in PROBABILITIES:
        errors.append(f"probability phải ∈ {PROBABILITIES}, nhận {prob!r}")
    if impact not in IMPACTS:
        errors.append(f"impact phải ∈ {IMPACTS}, nhận {impact!r}")

    priority = compute_priority(prob, impact) if not errors else ""
    if strategy and strategy not in STRATEGIES:
        errors.append(f"strategy phải ∈ {STRATEGIES}, nhận {strategy!r}")
    if priority == "A" and not strategy:
        errors.append("Rủi ro Priority A bắt buộc có strategy")
    if priority == "A" and strategy and not as_plain_text(raw.get("response_actions")):
        errors.append("Rủi ro Priority A bắt buộc có response_actions")

    # Current = đánh giá lại sau ứng phó (optional)
    prob_c = as_plain_text(raw.get("probability_current"))
    impact_c = as_plain_text(raw.get("impact_current"))
    if prob_c and prob_c not in PROBABILITIES:
        errors.append(f"probability_current phải ∈ {PROBABILITIES}, nhận {prob_c!r}")
    if impact_c and impact_c not in IMPACTS:
        errors.append(f"impact_current phải ∈ {IMPACTS}, nhận {impact_c!r}")
    if (prob_c and not impact_c) or (impact_c and not prob_c):
        errors.append("Current cần đủ cả probability_current và impact_current")
    priority_c = ""
    if prob_c and impact_c and prob_c in PROBABILITIES and impact_c in IMPACTS:
        priority_c = compute_priority(prob_c, impact_c)

    out = {
        "id": assign_id or as_plain_text(raw.get("id")) or "",
        "category": category,
        "driver": driver,
        "risk": risk_txt,
        "probability": prob,
        "impact": impact,
        "priority": priority,
        "probability_current": prob_c,
        "impact_current": impact_c,
        "priority_current": priority_c,
        "strategy": strategy,
        "response_actions": as_plain_text(raw.get("response_actions")),
        "owner": as_plain_text(raw.get("owner")),
        "contingency": as_plain_text(raw.get("contingency")),
        "residual": as_plain_text(raw.get("residual")),
        "secondary": as_plain_text(raw.get("secondary")),
        "contract_link": as_plain_text(raw.get("contract_link")),
        "evidence": as_plain_text(raw.get("evidence")),
        "confidence": as_plain_text(raw.get("confidence")) or "trung_binh",
        "comments": as_plain_text(raw.get("comments")),
    }
    return out, errors
