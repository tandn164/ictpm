---
name: closeout
description: >-
  Lập Báo cáo tổng kết dự án (Project Closeout) trong ictpm-flow/closeout:
  inventory input động, Fact, đề xuất JSON kèm confidence, hỏi Manual khi thiếu,
  validate, chỉ fill Word sau approved. Dùng khi pm:closeout, báo cáo tổng kết,
  đóng dự án, lessons learned, project closeout.
---

# Skill Báo cáo tổng kết dự án

Toàn bộ tài nguyên: `ictpm-flow/closeout/`.

Đọc `SOURCE_AND_MAP.md` + **`rules/inputs.md`** + toàn bộ `rules/` trước khi làm.

Trả lời **tiếng Việt**. Không tự `approved`.

## Template

- Làm việc: `templates/closeout.docx`
- Upstream: `templates/_source/` (PDF gốc — không sửa; **không** ghi tên nguồn ngoài vào draft)

## Input động

Chi tiết: `rules/inputs.md`.

| Slot | Vai trò |
|------|---------|
| `masterplan_json` | Meta, baseline |
| `risk_json` | Lessons / rủi ro còn lại |
| `wbs` / `hsdt` / `master_schedule` | Tiến độ, cam kết, đối chiếu |
| `@file` | Biên bản nghiệm thu, UAT… |

### Bước 0

1. Inventory → `inputs.inventory`.  
2. Thiếu định danh dự án hoặc actual (ngày đóng / nghiệm thu / cost) → hỏi Manual.  
3. Không bịa “đã nghiệm thu” khi chưa có Fact/Decision.

## Output

| File | Khi nào |
|------|---------|
| `artifacts/01_closeout.json` | Sau đề xuất + validate |
| `artifacts/bao_cao_kiem_tra.md` | Mỗi vòng |
| `artifacts/01_closeout_draft.docx` | Chỉ khi `approved` + tool |

## Pipeline

1. Inventory.  
2. Fact từ Master Plan / Risk / WBS / HSDT / @file.  
3. Điền overview, effectiveness, lessons, admin/contract/archive.  
4. Validate → `ready_for_review` — dừng chờ Manual.  
5. `approved` →:

```bash
python3 ictpm-flow/closeout/tools/fill_closeout.py
```

## Checklist hỏi Manual

| ID | Nội dung |
|----|----------|
| Q-CO-IN-* | Slot missing |
| Q-CO-ACT-01 | Ngày đóng / ký nghiệm thu thực tế? |
| Q-CO-ACT-02 | Cost actual — số hay giữ planned? |
| Q-CO-ACT-03 | Deliverable nào đã chấp nhận? |
| Q-CO-ACT-04 | Hợp đồng đóng hay còn bảo hành? |
| Q-CO-06 | Duyệt toàn bộ → approved + fill? |

## Cấm

- Tự `approved` / fill khi chưa approved.  
- Hardcode tên file input.  
- Bịa actual / nghiệm thu.  
- Dump `{confidence…}` vào Word.  
- Ghi branding nguồn template vào draft.
