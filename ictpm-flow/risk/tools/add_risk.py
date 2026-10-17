#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thêm 1 (hoặc nhiều) rủi ro vào 01_risk.json sau khi agent đã phân tích.

Agent phân tích → ghi object JSON → chạy tool này để:
  - validate Category/Driver/Risk + P/I
  - tính Priority A/B/C theo ma trận
  - gán id R-00N
  - append vào risks[]
  - (tuỳ chọn) refill Excel nếu approved hoặc --refill --force

Ví dụ:
  python3 ictpm-flow/risk/tools/add_risk.py --file /tmp/new_risk.json
  python3 ictpm-flow/risk/tools/add_risk.py --stdin < risk.json
  python3 ictpm-flow/risk/tools/add_risk.py \\
    --category Technical --driver "..." --risk "..." \\
    --probability High --impact Middle --strategy Mitigate \\
    --response-actions "..." --owner "SA" --evidence "F11"

  # Chỉ in đánh giá, chưa ghi:
  python3 ictpm-flow/risk/tools/add_risk.py --file x.json --dry-run
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from risk_lib import (  # noqa: E402
    JSON_PATH,
    OUT_PATH,
    TEMPLATE_PATH,
    as_plain_text,
    normalize_risk,
    next_risk_id,
)


def load_items(args: argparse.Namespace) -> list[dict]:
    if args.file:
        raw = json.loads(Path(args.file).read_text(encoding="utf-8"))
    elif args.stdin:
        raw = json.load(sys.stdin)
    else:
        # CLI single risk
        raw = {
            "category": args.category,
            "driver": args.driver,
            "risk": args.risk,
            "probability": args.probability,
            "impact": args.impact,
            "strategy": args.strategy or "",
            "response_actions": args.response_actions or "",
            "owner": args.owner or "",
            "contingency": args.contingency or "",
            "residual": args.residual or "",
            "secondary": args.secondary or "",
            "evidence": args.evidence or "",
            "confidence": args.confidence or "trung_binh",
            "comments": args.comments or "",
        }
        if not (args.category and args.driver and args.risk and args.probability and args.impact):
            raise SystemExit(
                "Cần --file/--stdin hoặc đủ --category --driver --risk --probability --impact"
            )

    if isinstance(raw, dict) and "risks" in raw and isinstance(raw["risks"], list):
        return raw["risks"]
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        return [raw]
    raise SystemExit("JSON phải là 1 object rủi ro, mảng, hoặc {\"risks\": [...]}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Thêm rủi ro đã phân tích vào 01_risk.json")
    parser.add_argument("--file", "-f", help="File JSON 1 rủi ro / mảng / {risks:[]}")
    parser.add_argument("--stdin", action="store_true", help="Đọc JSON từ stdin")
    parser.add_argument("--category")
    parser.add_argument("--driver")
    parser.add_argument("--risk")
    parser.add_argument("--probability", choices=["High", "Middle", "Low"])
    parser.add_argument("--impact", choices=["Big", "Middle", "Small"])
    parser.add_argument("--strategy", choices=["Avoid", "Transfer", "Mitigate", "Accept"])
    parser.add_argument("--response-actions", dest="response_actions")
    parser.add_argument("--owner")
    parser.add_argument("--contingency")
    parser.add_argument("--residual")
    parser.add_argument("--secondary")
    parser.add_argument("--evidence")
    parser.add_argument("--confidence", default="trung_binh")
    parser.add_argument("--comments")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Chỉ validate + in đánh giá, không ghi JSON",
    )
    parser.add_argument(
        "--allow-invalid",
        action="store_true",
        help="Vẫn ghi dù có lỗi validate (không khuyến nghị)",
    )
    parser.add_argument(
        "--refill",
        action="store_true",
        help="Sau khi ghi, chạy fill_risk nếu approved (hoặc kèm --force-refill)",
    )
    parser.add_argument(
        "--force-refill",
        action="store_true",
        help="Refill Excel cả khi status chưa approved",
    )
    parser.add_argument(
        "--json-path",
        type=Path,
        default=JSON_PATH,
        help="Đường dẫn 01_risk.json (mặc định artifacts)",
    )
    args = parser.parse_args()

    items = load_items(args)
    if not args.json_path.exists():
        print(f"Thiếu {args.json_path}", file=sys.stderr)
        return 1

    data = json.loads(args.json_path.read_text(encoding="utf-8"))
    risks = list(data.get("risks") or [])

    added = []
    all_errors = []
    existing_ids = {str(r.get("id")) for r in risks}
    for raw in items:
        wanted = as_plain_text(raw.get("id"))
        if wanted and wanted not in existing_ids and wanted not in {a["id"] for a in added}:
            rid = wanted
        else:
            rid = next_risk_id(risks + added)
        normalized, errors = normalize_risk(raw, assign_id=rid)

        print("---")
        print(f"ID       : {normalized['id']}")
        print(f"Category : {normalized['category']}")
        print(f"Driver   : {normalized['driver']}")
        print(f"Risk     : {normalized['risk']}")
        print(f"P / I    : {normalized['probability']} / {normalized['impact']}")
        print(f"Priority : {normalized['priority']}  (theo ma trận Probability × Impact)")
        print(f"Strategy : {normalized['strategy'] or '(chưa)'}")
        if errors:
            print("Lỗi:")
            for e in errors:
                print(f"  - {e}")
            all_errors.extend(errors)
            if not args.allow_invalid:
                continue
        added.append(normalized)

    if not added:
        print("Không có rủi ro nào được thêm (lỗi validate).", file=sys.stderr)
        return 2

    if args.dry_run:
        print(f"\n[dry-run] Sẽ thêm {len(added)} rủi ro — chưa ghi file.")
        return 0 if not all_errors else 2

    risks.extend(added)
    data["risks"] = risks
    data.setdefault("audit", {})
    log = data["audit"].setdefault("add_risk_log", [])
    log.append(
        {
            "at": datetime.now(timezone.utc).isoformat(),
            "added_ids": [r["id"] for r in added],
            "count": len(added),
        }
    )
    # Nếu đã approved rồi thêm risk mới → hạ xuống ready_for_review để Manual xem lại
    if data.get("status") == "approved":
        data["status"] = "ready_for_review"
        data.setdefault("validation", {})["ket_luan"] = (
            "Đã thêm rủi ro mới sau approved — cần Manual duyệt lại trước fill."
        )
        print(
            "Cảnh báo: status chuyển approved → ready_for_review (có rủi ro mới).",
            file=sys.stderr,
        )

    args.json_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"\nĐã ghi {len(added)} rủi ro vào {args.json_path}")
    print(f"Tổng risks[] = {len(risks)}")

    if args.refill or args.force_refill:
        # local import to avoid circular issues at module load
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from fill_risk import build_template, fill_from_json

        if not TEMPLATE_PATH.exists():
            build_template(TEMPLATE_PATH)
        if data.get("status") != "approved" and not args.force_refill:
            print(
                "Chưa refill Excel (status chưa approved). "
                "Dùng --force-refill để thử, hoặc approved rồi chạy fill_risk.py.",
                file=sys.stderr,
            )
        else:
            # reload after status change
            data = json.loads(args.json_path.read_text(encoding="utf-8"))
            # force path: temporarily treat as fillable
            if args.force_refill and data.get("status") != "approved":
                print("Refill với --force-refill (status chưa approved).", file=sys.stderr)
            fill_from_json(data, TEMPLATE_PATH, OUT_PATH)

    return 0 if not all_errors else 0  # đã ghi thành công các item hợp lệ


if __name__ == "__main__":
    raise SystemExit(main())
