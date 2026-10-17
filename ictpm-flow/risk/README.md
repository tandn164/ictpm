# Module Risk Management

Lập Risk Management Plan + Risk Register theo PMP (Plan → Identify → Analyze → Respond → Monitor).

```text
ictpm-flow/risk/
  rules/                 # inputs.md (động) + plan/identify/analyze/respond/monitor/validation
  templates/             # risk-management.xlsx
  tools/fill_risk.py
  artifacts/             # JSON, report, draft
```

**Input động:** mỗi lần `pm:risk` quét slot (HSMT/RFP/HSDT/WBS/…) → thiếu hỏi Manual (`rules/inputs.md`).

Khi chạy: skill `.agents/skills/risk/SKILL.md` + `rules/` (+ template/tool khi approved).  
Lệnh: `pm:risk` · thêm rủi ro: `pm:risk add` / “thêm rủi ro …”

```bash
# Thêm rủi ro đã phân tích vào JSON (+ optional refill Excel)
python3 ictpm-flow/risk/tools/add_risk.py --file risk_item.json
python3 ictpm-flow/risk/tools/add_risk.py --file risk_item.json --dry-run
python3 ictpm-flow/risk/tools/fill_risk.py   # sau approved
```
