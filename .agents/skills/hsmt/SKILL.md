---
name: hsmt
description: >-
  Lập E-HSMT Mẫu 5A từ RFP theo module ictpm-flow/hsmt: phân tích Fact, đề xuất
  JSON kèm confidence, hỏi Manual khi thiếu, validate, report; chỉ fill Word
  sau approved. Dùng khi user nói pm:hsmt, lập HSMT, hồ sơ mời thầu, E-HSMT.
---

# Skill HSMT

Toàn bộ tài nguyên nằm trong `ictpm-flow/hsmt/`.

Đọc toàn bộ `ictpm-flow/hsmt/rules/` trước khi làm.

Trả lời **tiếng Việt**. Không tự `approved`.

## Input

| Cái | Path |
|-----|------|
| RFP | `RFP.pdf` (OCR nếu scan) |
| Template | `ictpm-flow/hsmt/templates/5. Mẫu số 5A E-HSMT Phi tư vấn 1 túi.docx` |
| Rule | `ictpm-flow/hsmt/rules/` |
| Bản chuẩn (không copy) | `ictpm-flow/hsmt/artifacts/chuan/` |

## Output

| File | Khi nào |
|------|---------|
| `ictpm-flow/hsmt/artifacts/01_hsmt.json` | Sau phân tích + đề xuất + validate |
| `ictpm-flow/hsmt/artifacts/bao_cao_kiem_tra.md` | Mỗi vòng validate |
| `ictpm-flow/hsmt/artifacts/01_hsmt_draft.docx` | Chỉ khi `status=approved` + chạy tool |

## Pipeline

1. Phân tích RFP → `facts[]`.
2. Đọc rule → đề xuất Ch II–V; thiếu thì `questions_for_manual[]`.
3. Mỗi phần: nội dung + confidence + evidence.
4. Validate theo `rules/validation.md` (≤3 vòng A/B; C hỏi Manual).
5. `ready_for_review` + báo cáo — dừng chờ Manual.
6. Manual `approved` → chạy:

```bash
python3 ictpm-flow/hsmt/tools/fill_hsmt.py
```

## Checklist hỏi Manual (không bỏ)

Trước `ready_for_review`, `questions_for_manual` **phải** có (hoặc Decision đã chốt) các mục sau:

| Mã | Hỏi gì |
|----|--------|
| E-CDNT **5.1** | Tên **và địa chỉ** đầy đủ CĐT (`chu_dau_tu_day_du`) — cấm chỉ dùng tên ngắn |
| E-CDNT **18.4** | Số ngày hoàn trả BĐDT (≤14) — **hỏi riêng**, kể cả khi 18.9 = Không áp dụng |
| E-CDNT **28.2** + **31.4** | Sau khi chốt giá thấp nhất / giá đánh giá: điền bằng cách **chọn 1 nhánh**, xóa dòng hướng dẫn. Cấm "giữ template" còn cả 2 nhánh |
| E-CDNT **31.5** | Loại hợp đồng → chọn đúng 1 câu căn cứ giá gói thầu |
| Ch III **Bảng số 01 năng lực** | Năm mốc TT1; doanh thu TT3 (số hoặc "Không áp dụng"); HĐ tương tự TT4 — tách với hỏi nhân sự |

## Cấm

- Sự không nhất quán giữa các nội dung và các lựa chọn giữa các chương.
- Tự quyết định một dữ liệu nào đó dựa vào suy luận mà không báo cáo lại trong output.
- Fill Word khi chưa `approved`.
- Sửa Ch I, VI, Mục 1 Ch III.
- Với ô dạng "Chọn phương pháp A thì trích xuất / Chọn phương pháp B thì trích xuất": để nguyên cả hai nhánh hoặc ghi "giữ template".
