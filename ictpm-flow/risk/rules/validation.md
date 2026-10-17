# Kiểm tra trước khi xin duyệt (Risk)

Đối chiếu: Fact + Decision Manual + ma trận A/B/C + nội dung JSON.

AI được sửa lỗi hình thức / khớp Fact (tối đa 3 vòng).  
Thiếu Decision → hỏi Manual.  
Qua kiểm tra ≠ `approved`.

---

## A. Trong file có thống nhất không?

- Tên dự án / gói thống nhất (Cover, Plan, Register).
- Mọi risk có đủ category, driver, risk statement.
- Probability ∈ {High, Middle, Low}; Impact ∈ {Big, Middle, Small}.
- Priority khớp ma trận analyze.md (tính lại nếu lệch).
- Strategy ∈ {Avoid, Transfer, Mitigate, Accept} với mọi rủi ro A (và B nếu đã điền).
- Không còn placeholder / TBD / dump `{confidence…}` trong value sẽ fill.



## B. Khớp Fact và khớp giữa các phần?

- `inputs.inventory` đã ghi; có ≥1 nguồn Fact `found` (hoặc Manual đã `skipped` có điều kiện + Fact thay thế).
- Rủi ro dẫn được về Fact/slot (hoặc Decision) — không generic vô căn cứ.
- Plan đủ 5 khối: methodology, roles, budgeting, timing, risk_categories.
- Categories dùng trong risks[] thuộc tập đã chốt ở Plan (hoặc giải thích mở rộng).
- Monitor có cadence + review_questions.



## C. Decision Manual đã có chưa?

- Budgeting (số/%) nếu đã điền số: phải có Decision.
- Owner mặc định / cadence monitor đã hỏi hoặc đề xuất rõ chờ chốt.
- Rủi ro A chọn Accept hoặc Transfer: đã hỏi / đã có Decision.
- Danh sách risks[] đã đưa Manual duyệt (giữ/sửa/xóa) hoặc đang trong questions.

