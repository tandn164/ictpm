# Kiểm tra trước khi xin duyệt

Đối chiếu: Fact + Decision Manual + Mẫu 5A + nội dung đề xuất trong JSON.

AI được sửa lỗi hình thức / khớp Fact (tối đa 3 vòng).  
Thiếu Decision → hỏi Manual.  
Qua kiểm tra ≠ `approved`.

---

## A. Trong file có thống nhất không?

- Không sửa các phần mẫu cấm (Ch I, Ch VI, Mục 1 Ch III…).
- Cùng một mốc ngày không lệch giữa các chương.
- Tên gói / dự án / chủ đầu tư thống nhất.
- Chỗ đã điền không còn placeholder mẫu.
- Dòng phạm vi Chương IV đủ khối lượng và đơn vị tính (khi đã điền).

## B. Có khớp Fact và khớp giữa các chương không?

- Mục tiêu / phạm vi in–out / NFR / deliverable / điều khoản trách nhiệm quan trọng trong Fact đều có chỗ trong II–V (hoặc lệch có căn cứ + tương đương).
- Lịch Chương II khớp Fact sau khi đã xử lý năm / Decision.
- Chương IV và V cùng phạm vi.
- Chương III kỹ thuật bám Chương V; không chấm giá trong tiêu chí kỹ thuật.
- Phương pháp đánh giá kỹ thuật đã chọn thì viết đủ theo rule Chương III.
- Thủ tục đầu vào khác mạng đã có giải pháp tương đương (nếu phát sinh).
- Không thêm yêu cầu ngoài Fact trừ Decision Manual.



## C. Decision Manual đã có chưa?

- Mọi ô cần số ngày / % / tiền / trọng số / năm mà Fact không có: đã có câu trả lời Manual hoặc ghi chờ rõ — không số bịa.
- Phương pháp đánh giá kỹ thuật đã được Manual chốt (hoặc đang chờ trong `questions_for_manual`).

