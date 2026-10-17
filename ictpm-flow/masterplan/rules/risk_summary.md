# 3.4 Quản lý rủi ro — tóm tắt

**ICTPM:** chi tiết ở `ictpm-flow/risk/` (Plan + Register A/B/C).

## JSON

```json
"risk_summary": "Tham chiếu 01_risk.json / 01_risk_draft.xlsx. …",
"risks_top": [
  {
    "id": "R-001",
    "title": "...",
    "description": "...",
    "date_identified": "",
    "originator": "PM",
    "priority": "A",
    "response": "Mitigate: …"
  }
]
```

## Quy tắc

- Priority dùng **A/B/C** (không dùng High/Low của Mini gốc).
- Ưu tiên lấy từ `01_risk.json` nếu có (top A, rồi B).
- Không copy toàn bộ register vào Master Plan.
- Chưa có module risk → đề xuất 3–5 rủi ro tóm tắt + hỏi Manual có lập risk đầy đủ không.
