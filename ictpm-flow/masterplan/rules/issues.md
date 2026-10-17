# 3.3 Quản lý vấn đề (Issue)

Issue = đã xảy ra / đang tranh chấp; khác Risk (chưa xảy ra).

## JSON

```json
"issues": [
  {
    "title": "...",
    "description": "...",
    "date_identified": "YYYY-MM-DD",
    "originator": "...",
    "impact": "High|Middle|Low",
    "resolution": "..."
  }
]
```

Lúc kickoff thường `issues: []` + `issues_intro` mô tả quy trình (log, owner, escalation). Không bắt buộc có issue sẵn.
