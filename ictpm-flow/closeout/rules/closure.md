# Đóng hành chính, hợp đồng, lưu trữ

## Administrative

```json
"admin_closure": {
  "summary": "...",
  "deliverables": [
    {"name": "...", "accepted": "Yes|No|Partial", "evidence": "…", "date": "YYYY-MM-DD"}
  ],
  "open_items": [
    {"item": "...", "owner": "...", "due": "...", "status": "Open|Closed"}
  ]
}
```

## Contract

```json
"contract_closure": {
  "summary": "...",
  "contracts": [{"name": "...", "status": "Closed|Pending", "note": "..."}]
}
```

## Archive

```json
"archive": {
  "summary": "...",
  "items": [{"item": "...", "location": "...", "distributed_to": "..."}]
}
```

Thiếu biên bản nghiệm thu / trạng thái HĐ → hỏi Manual.
