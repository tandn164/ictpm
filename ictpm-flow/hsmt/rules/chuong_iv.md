# Chương IV Phạm vi cung cấp

## Việc cần làm

Chuyển Fact về sản phẩm bàn giao và phạm vi công việc thành từng dòng trong biểu phạm vi cung cấp. Phải breakdown thành list chức năng nghiệp vụ dạng bảng, không gộp một dòng chung.

## Cách điền

### Bước 1: Lấy nguyên liệu từ Fact

Liệt kê:

- Sản phẩm bàn giao (đặc tả, quy trình, CSDL, menu…)
- Nhóm chức năng / phân hệ / hình hệ thống (nếu Fact chỉ nêu tên nhóm)
- Việc tích hợp hệ thống hiện có
- Công việc từ phân tích đến kiểm thử / vận hành / chuyển giao (nếu Fact có phạm vi giai đoạn)
- Phạm vi loại trừ (không đưa vào bảng)

### Bước 2: Tách thành dòng nghiệp vụ (quan trọng)

Fact thường chỉ có tên nhóm. Agent phải breakdown mỗi nhóm thành các chức năng nghiệp vụ cụ thể mà người dùng / hệ thống thực hiện được.

Cách làm:

1. Với mỗi nhóm chức năng trong Fact, liệt kê các việc nghiệp vụ tối thiểu hợp lý với ngữ cảnh đó (luồng người dùng đầu-cuối)
2. Mỗi việc = một dòng bảng
3. Đánh số dạng `nhóm.dòng` (1.1, 1.2, 2.1…) hoặc STT tuần tự, thống nhất với Chương V
4. Dòng tích hợp / CSDL / giai đoạn dự án (phân tích, thiết kế, kiểm thử, go-live): tách riêng theo Fact, không nhét vào một dòng "xây website"

Mức chi tiết kỳ vọng: đủ để nhà thầu hiểu chào gì (ví dụ trong nhóm thành viên: đăng ký, đăng nhập, quên mật khẩu, hồ sơ… nếu phù hợp Fact).

Không bịa tính năng ngoài ngữ cảnh Fact. Nếu phải suy luận chi tiết thì ghi `confidence: trung_binh` hoặc `thap` kèm lý do; hỏi Manual khi nghi ngờ.

### Bước 3: Ghi đủ cột mẫu

Mỗi dòng cần:

- STT
- Tên (nên dạng `Nhóm: chức năng` cho dễ khớp Ch V)
- Mô tả ngắn (1-2 ý nghiệm thu được)
- Khối lượng + đơn vị (thường 01 + Chức năng hoặc Gói)
- Địa điểm (từ Fact / Manual)
- Ngày hoàn thành không muộn hơn mốc vận hành/cut-over trong Fact (sau khi có năm)

### Bước 4: Khớp Chương V

- Cùng bộ STT / tên nhóm-chức năng với bảng yêu cầu chức năng Ch V
- Ch III nhóm B chỉ chấm theo nhóm; Ch IV vẫn giữ từng dòng chi tiết

## Output JSON

`chuong_iv.hang_muc[]`: `stt`, `ten`, `mo_ta`, `khoi_luong`, `don_vi`, `dia_diem`, `ngay_hoan_thanh`, `confidence`, `evidence`

## Nên làm

- Hỏi manual nếu có các quyết định nào đó cần suy luận và lựa chọn ngoài Fact
- Hỏi Manual nếu Fact quá mỏng để breakdown
- Ưu tiên breakdown chức năng người dùng trước, deliverable/giai đoạn sau

## Không được

- Một dòng chung cho cả gói
- Thêm hạng mục ngoài Fact khi Manual chưa đồng ý
- Đưa phạm vi loại trừ vào bảng
- Để dòng chung chung không chào được
