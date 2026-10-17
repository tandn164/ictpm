# Input động (Supporting Toolkit)

Không hardcode tên file. Mỗi lần chạy: **quét → gắn slot → thiếu hỏi Manual**.

## Slot

| Slot | Bắt buộc? | Pattern / nơi tìm | Dùng cho |
|------|-----------|-------------------|----------|
| `masterplan_json` | Khuyến nghị | `ictpm-flow/masterplan/artifacts/01_masterplan.json` | Meta, roles, communications, schedule, issues |
| `risk_json` | Khuyến nghị | `ictpm-flow/risk/artifacts/01_risk.json` | Issues/watch từ risk; lessons |
| `closeout_json` | Tuỳ | `ictpm-flow/closeout/artifacts/01_closeout.json` | Post-eval, survey, phase exit (nếu đã đóng) |
| `hsdt` | Tuỳ | `HSDT*.docx` (masterplan inputs hoặc @) | Stakeholder / org / cam kết |
| `wbs` | Tuỳ | `*WBS*.xlsx` | Phase exit / milestone |
| `master_schedule` | Tuỳ | `*Schedule*.docx` | Phase / go-live |
| `hsmt_json` / `rfp` | Tuỳ | HSMT JSON / RFP | Bối cảnh gốc |
| `other` | Tuỳ | Biên bản UAT, khảo sát thô, @file | Peer score, survey actual |

**Tối thiểu:** định danh dự án từ `masterplan_json` | `hsdt` | `closeout_json` | Manual dán Fact.  
**Không bịa:** điểm peer, Likert survey, issue chưa có Fact/Decision, kết quả selection nếu Manual chưa chọn tiêu chí/trọng số.

## Inventory JSON

```json
"inputs": {
  "docs_requested": ["stakeholder_analysis", "issues_actions"],
  "inventory": {
    "masterplan_json": {"status": "found", "path": "…"},
    "risk_json": {"status": "found", "path": "…"},
    "closeout_json": {"status": "missing", "path": null}
  }
}
```

`docs_requested`: danh sách ID cần lập; `["all"]` = đủ catalog (trừ closeout alias).  
`status`: `found` | `missing` | `skipped`.

## Ưu tiên Fact

1. Decision Manual  
2. `closeout_json` (nếu doc hậu dự án)  
3. `masterplan_json` / `risk_json`  
4. `hsdt` / `wbs` / `@file`
