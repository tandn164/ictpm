---
name: masterplan
description: >-
  Lập Project Management Plan (Master Plan) trong ictpm-flow/masterplan: inventory
  input động, Fact, đề xuất JSON kèm confidence, hỏi Manual khi thiếu slot,
  validate, chỉ fill Word sau approved. Dùng khi pm:masterplan, master plan,
  PMP, kế hoạch quản lý dự án tổng thể.
---

# Skill Master Plan

Toàn bộ tài nguyên: `ictpm-flow/masterplan/`.

Đọc `SOURCE_AND_MAP.md` + **`rules/inputs.md`** + toàn bộ `rules/` trước khi làm.

Trả lời **tiếng Việt**. Không tự `approved`.

## Template

- Làm việc: `templates/masterplan.docx`
- Upstream nội bộ: `templates/_source/` (không sửa; không nêu nguồn ngoài trong draft/JSON)

## Input động (không hardcode tên file)

Chi tiết: `rules/inputs.md`.

| Slot | Vai trò |
|------|---------|
| `hsdt` | Hồ sơ dự thầu (docx) |
| `wbs` | WBS (xlsx) |
| `master_schedule` | Bảng tiến độ (docx) |
| `hsmt_json` / `risk_json` / `rfp` | Module / RFP nếu có |
| `@file` trong chat | Ưu tiên gắn đúng slot |

Thư mục gợi ý: `ictpm-flow/masterplan/artifacts/inputs/`.

### Bước 0 — mỗi lần chạy

1. Quét slot → `inputs.inventory` (`found` / `missing` / `skipped` + `path`).
2. Thiếu định danh dự án **hoặc** nguồn tiến độ → hỏi Manual (Q-MP-IN-*), không bịa.
3. Manual gửi file / skip → cập nhật inventory rồi đề xuất.
4. Đổi file → inventory lại.

## Output

| File | Khi nào |
|------|---------|
| `artifacts/01_masterplan.json` | Sau inventory + đề xuất + validate |
| `artifacts/bao_cao_kiem_tra.md` | Mỗi vòng validate (kèm inventory) |
| `artifacts/01_masterplan_draft.docx` | Chỉ khi `status=approved` + chạy tool |

## Pipeline

1. Inventory input.  
2. Fact từ slot `found`.  
3. Rule → overview, roles, communications, schedule, issues, risks_top, transition, phụ lục.  
4. Risk: tóm tắt từ `risk_json`; không copy full register.  
5. Validate → `ready_for_review` — dừng chờ Manual.  
6. `approved` → `python3 ictpm-flow/masterplan/tools/fill_masterplan.py`

## Checklist hỏi Manual

| ID | Khi nào |
|----|---------|
| Q-MP-IN-* | Slot khuyến nghị missing |
| Q-MP01–06 | Fact module, ngày, roles, cost, quality, duyệt fill |
| Q-MP08 | Ngày/giá lệch giữa slot found |

## Cấm

- Tự `approved` / fill khi chưa approved.
- Hardcode tên file input.
- Bịa ngày / số tiền khi thiếu Fact.
- Nhét full Risk Register vào Master Plan.
- Dump `{confidence, evidence…}` vào Word.
- Ghi tên / URL nguồn template bên ngoài vào artifact hoặc nội dung draft.
