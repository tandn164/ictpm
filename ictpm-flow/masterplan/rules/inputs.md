# Input động (Master Plan)

Không gắn cứng một tên file. Mỗi lần chạy: **quét → gắn slot → thiếu thì hỏi Manual**.

## Slot

| Slot | Bắt buộc? | Pattern tìm (ưu tiên `artifacts/inputs/`, rồi root, rồi file user @) | Dùng cho |
|------|-----------|---------------------------------------------------------------------|----------|
| `hsdt` | Khuyến nghị | `HSDT*.docx`, `*HSDT*.docx` | Meta gói, giá, giải pháp, cam kết |
| `wbs` | Khuyến nghị | `*WBS*.xlsx` | Scope, milestone, phụ trách |
| `master_schedule` | Khuyến nghị | `*Master*Schedule*.docx`, `*Schedule*.docx` | Ngày dịch vụ / đối chiếu tiến độ |
| `hsmt_json` | Tuỳ | `ictpm-flow/hsmt/artifacts/01_hsmt.json` | Fact thầu đã có |
| `risk_json` | Tuỳ | `ictpm-flow/risk/artifacts/01_risk.json` | `risks_top` |
| `rfp` | Tuỳ | `RFP.pdf`, `*RFP*` | Đối chiếu yêu cầu |
| `other` | Tuỳ | File Manual @ hoặc khai trong chat | Bổ sung |

**Tối thiểu để lập PMP:** có ít nhất **một** nguồn định danh dự án (`hsdt` | `hsmt_json` | `rfp` | Manual dán Fact) **và** ít nhất **một** nguồn tiến độ (`wbs` | `master_schedule` | Manual chốt ngày).  
Thiếu → ghi `questions_for_manual`, **không bịa**.

## Quy trình mỗi lần `pm:masterplan`

1. **Inventory** — liệt kê file tìm thấy theo slot (path thật). User @ file → ưu tiên path đó cho slot tương ứng.
2. Ghi vào JSON:
   ```json
   "inputs": {
     "inventory": {
       "hsdt": {"status": "found", "path": "…/HSDT.docx"},
       "wbs": {"status": "found", "path": "…/02_WBS.xlsx"},
       "master_schedule": {"status": "missing", "path": null},
       "risk_json": {"status": "found", "path": "…/01_risk.json"}
     }
   }
   ```
   `status`: `found` | `missing` | `skipped` (Manual bảo bỏ qua).
3. Slot khuyến nghị mà `missing` → thêm câu hỏi (vd. Q-MP-IN-01: thiếu WBS — gửi file / path / hoặc skip?).
4. Manual trả file hoặc `skipped` + Decision → cập nhật inventory, chạy tiếp.
5. Mâu thuẫn ngày/giá giữa các slot `found` → hỏi baseline (không tự chọn).

## Map nội dung (khi slot found)

### WBS (xlsx)

- Sheet WBS: `Mã WBS`, tên, sản phẩm bàn giao, phụ trách, bắt đầu, kết thúc.
- PMP chỉ lấy milestone cấp 1–2 (+ Kick-off / UAT / Go-live). Không dump Gantt.

### Master Schedule (docx)

- Bảng tiến độ dịch vụ → đối chiếu / bổ sung `schedule[]`.

### HSDT (docx)

- Tên gói, CĐT, nhà thầu, giá, bảo đảm, giải pháp KT, kế hoạch triển khai → overview / cost / quality.

## Cấm

- Hardcode tên file cụ thể trong skill (vd. chỉ nhận `HSDT_Nhom_9-2.docx`).
- Coi file cũ còn đúng khi Manual đã thay file mới (@ path mới).
- Bịa ngày/giá khi slot `missing`.
