# Chương V Yêu cầu về kỹ thuật

## Việc cần làm

Điền yêu cầu kỹ thuật theo các mục trên Mẫu 5A. Nội dung lấy từ Fact (và Decision Manual). Mục 3 phải có bảng (không chỉ đoạn văn): NFR + chức năng nghiệp vụ đã breakdown, cùng bộ với Chương IV. Đây là cơ sở để Chương III đánh giá đề xuất.

## Cấu trúc mục trên mẫu (giữ đúng mẫu)

1. Giới thiệu chung
2. Mục tiêu công việc
3. Yêu cầu kỹ thuật
4. Giải pháp và phương pháp luận (yêu cầu nhà thầu đề xuất gì)
5. Kiểm tra, nghiệm thu

## Cách điền

- Mục 1-2: tóm tắt dự án / gói / mục tiêu từ Fact; thống nhất tên với Chương II.
- Mục tiêu có thể tách ý (kênh bán, đủ nhóm chức năng, tích hợp, an toàn dữ liệu) chỉ khi Fact hoặc suy luận có căn cứ (ghi confidence).
- Toàn bộ nội dung: **tiếng Việt có dấu**. Đầu mục (3.1, 3.2…) mỗi mục một dòng riêng.
- Bảng Word: **có kẻ** (Table Grid). Không chèn bảng không border.

### Mục 3: Bắt buộc dạng bảng

#### 3.1: Bảng NFR (phi chức năng)

Cột gợi ý: `STT | Nội dung | Yêu cầu`

- Mỗi NFR trong Fact = một dòng
- Cột Yêu cầu: diễn giải đo được / kiểm được từ Fact (giữ nguyên số liệu Fact; không bịa SLA mới)
- Có thể thêm bullet cách đạt / cách đo nếu giúp nghiệm thu; đánh proposed nếu là diễn giải

#### 3.2: Bảng chức năng nghiệp vụ

Cột gợi ý: `STT | Nội dung công việc | Yêu cầu`

Breakdown (cùng quy trình Ch IV):

1. Lấy nhóm chức năng / phân hệ / tích hợp / giai đoạn từ Fact
2. Trong mỗi nhóm: tách thành chức năng nghiệp vụ cụ thể (1.1, 1.2…)
3. Dòng nhóm (1, 2, 3…) có thể chỉ là tiêu đề nhóm (cột yêu cầu trống)
4. Dòng chi tiết: cột Yêu cầu = các bullet nhà thầu phải đáp ứng (hành vi hệ thống)
5. STT và tên khớp Ch IV (cùng 1.1 = cùng chức năng)

Thứ tự nhóm gợi ý (điều chỉnh theo Fact):

- Nhóm chức năng người dùng (theo phân hệ Fact)
- Nhóm CSDL (nếu Fact có)
- Nhóm tích hợp hệ thống hiện có
- Nhóm phân tích / thiết kế / kiểm thử / chuyển giao (nếu phạm vi Fact gồm cả vòng đời)

#### 3.3: Yêu cầu khác

- Loại trừ phạm vi (nếu Fact có)
- Deliverable tối thiểu
- Bảo hành / trách nhiệm / sở hữu theo Fact điều khoản

- Mục 4: yêu cầu nhà thầu trình bày giải pháp, phương pháp luận, kế hoạch: bám danh mục nội dung đề xuất trong Fact (nếu có).
- Mục 5: trình tự nghiệm thu / chấp nhận / thời hạn trách nhiệm theo Fact điều khoản (và mẫu); không mâu thuẫn chương khác.

## Khớp chương khác

- Mỗi nhóm yêu cầu chức năng ở đây nên có dòng phạm vi tương ứng ở Chương IV (cùng STT).
- Tiêu chí kỹ thuật Chương III nhóm B: một tiêu chí / nhóm (không tách B1 cho từng 1.1 trừ khi Manual yêu cầu).

## Output JSON

- `chuong_v.nfr_table[]`: `stt`, `noi_dung`, `yeu_cau`, `confidence`, `evidence`
- `chuong_v.chuc_nang_table[]`: `stt`, `noi_dung`, `yeu_cau`, `la_tieu_de_nhom` (bool), `confidence`, `evidence`
- Các mục 1, 2, 4, 5: text + confidence

## Nên làm

- Breakdown xong Ch V rồi mới khóa tên nhóm cho bảng điểm Ch III
- Hỏi manual nếu có các quyết định nào đó cần suy luận và lựa chọn ngoài Fact
- Hỏi Manual khi Fact chỉ có tên hệ thống, chưa có phân hệ

## Không được

- Chỉ mô tả chức năng bằng đoạn văn dài, không có bảng / list STT
- Bịa NFR hoặc chức năng ngoài Fact / Decision
- Lệch STT với Chương IV
- Ghi tên nguồn bị Manual cấm trong văn bản HSMT: diễn đạt như yêu cầu Chủ đầu tư
