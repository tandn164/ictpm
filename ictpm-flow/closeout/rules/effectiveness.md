# Hiệu quả quản lý (Management Effectiveness)

So sánh **baseline** (kế hoạch) với **thực tế**.

## JSON

```json
"effectiveness": {
  "summary": "...",
  "baselines": [
    {"area": "Scope|Schedule|Cost|Quality|Risk|…", "planned": "...", "actual": "...", "variance": "..."}
  ]
}
```

- Schedule/Cost planned: từ Master Plan / WBS / HSDT.  
- Actual: **chỉ khi có Fact hoặc Decision Manual** — thiếu → hỏi (Q-CO-ACT-*).
