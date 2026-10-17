# 1. Tóm tắt dự án (Project Summary)

## Nội dung bắt buộc

| Field JSON | Ý nghĩa |
|------------|---------|
| `project_summary` | Tình trạng hiện tại + nhu cầu / cơ hội + cách dự án giải quyết + deliverables chính |
| `scope_in` | Việc **làm** (bullet hoặc đoạn) |
| `scope_out` | Việc **không làm** |
| `assumptions` | Giả định |
| `constraints` | Ràng buộc (thời gian, ngân sách, pháp lý, hạ tầng…) |
| `management_approach` | Cách quản lý tổng thể (waterfall / agile / hybrid; cổng giai; họp…) |

## Nguồn Fact

1. Slot **`hsdt`** (nếu `found`) — tên gói, CĐT/nhà thầu, giải pháp & kế hoạch triển khai  
2. Slot **`wbs`** — deliverable → `scope_in`  
3. Slot **`hsmt_json`** / **`rfp`** — bổ sung / đối chiếu  

Thiếu scope/ngày/tiền → hỏi Manual, không bịa. Chi tiết: `inputs.md` (input động).

## Confidence

Mỗi field: `value` + `confidence` (`fact` / `de_xuat` / `can_manual`) + `evidence`.
