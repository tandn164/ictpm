# Input động (Báo cáo tổng kết)

Không hardcode tên file. Mỗi lần chạy: **quét → gắn slot → thiếu hỏi Manual**.

## Slot

| Slot | Bắt buộc? | Pattern / nơi tìm | Dùng cho |
|------|-----------|-------------------|----------|
| `masterplan_json` | Khuyến nghị | `ictpm-flow/masterplan/artifacts/01_masterplan.json` | Meta, scope, baseline lịch/cost |
| `risk_json` | Khuyến nghị | `ictpm-flow/risk/artifacts/01_risk.json` | Lessons / rủi ro còn mở |
| `wbs` | Tuỳ | `*WBS*.xlsx` (masterplan inputs hoặc @) | So sánh tiến độ / deliverable |
| `hsdt` | Tuỳ | `HSDT*.docx` | Cam kết thầu, giá, NFR |
| `master_schedule` | Tuỳ | `*Schedule*.docx` | Đối chiếu ngày |
| `rfp` / `hsmt_json` | Tuỳ | RFP / HSMT JSON | Bối cảnh gốc |
| `other` | Tuỳ | Biên bản nghiệm thu, UAT… do Manual @ | Administrative closure |

**Tối thiểu:** có định danh dự án từ `masterplan_json` | `hsdt` | Manual dán Fact.  
Thiếu số liệu thực tế (ngày đóng, cost actual, ký nghiệm thu) → hỏi Manual, không bịa.

## Inventory JSON

```json
"inputs": {
  "inventory": {
    "masterplan_json": {"status": "found", "path": "…"},
    "risk_json": {"status": "missing", "path": null}
  }
}
```

`status`: `found` | `missing` | `skipped`.
