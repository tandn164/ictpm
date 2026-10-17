# Kiểm tra trước khi xin duyệt (Master Plan)

Đối chiếu: Fact + Decision + JSON + (nếu có) risk/HSMT.  
AI sửa lỗi hình thức ≤3 vòng. Thiếu Decision → hỏi Manual.  
Qua kiểm tra ≠ `approved`.

---

## A. Trong file có thống nhất không?

- Tên dự án / mã / PM thống nhất trên bìa và nội dung.
- Có đủ: summary, scope_in, scope_out, roles (≥ Sponsor + PM), communications (≥1 dòng), schedule (≥1 mốc), transition (≥ vài hạng mục).
- Risk tóm tắt: priority ∈ {A,B,C}; có `risk_summary` trỏ module risk nếu đã có.
- Không còn `{{placeholder}}` / TBD trong value sẽ fill.
- Không dump `{confidence, evidence}` vào ô Word.

## B. Khớp Fact / module khác?

- `inputs.inventory` đã ghi; đủ tối thiểu định danh + tiến độ (hoặc Manual đã skip/Decision).
- Scope và milestone dẫn được về slot `found` (wbs / master_schedule / hsdt / hsmt…) hoặc Decision.
- Ngày `schedule[]` khớp (hoặc giải thích lệch) giữa các slot tiến độ `found`.
- Meta dự án / giá (nếu điền) khớp slot `hsdt` hoặc có Decision khi lệch.
- Nếu có `01_risk.json`: top risks không mâu thuẫn priority/strategy.
- Ngày schedule không mâu thuẫn lẫn nhau (start ≤ end).

## C. Decision Manual?

- Ngày milestone quan trọng / ngân sách số: đã hỏi hoặc đã có Decision.
- Owner các mốc chính đã rõ hoặc đang trong questions.
- Danh sách roles / schedule đã đưa Manual duyệt (giữ/sửa/xóa).
