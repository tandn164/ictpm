# Chương III Tiêu chuẩn đánh giá E-HSDT

## Việc cần làm

Quy định cách xét E-HSDT: hợp lệ, năng lực, kỹ thuật, tài chính dựa vào tính chất và yêu cầu của dự án.

## Cách điền

## Rule chung:

- Chỉ điền các mục phù hợp với tính chất của dự án và theo các lựa chọn của chương II.
- Không đưa tiêu chí giá vào phần kỹ thuật.
- Tiếng Việt **có dấu**. Bảng chèn vào Word phải **có kẻ** (Table Grid).

### Mục 1: Hợp lệ

- Giữ nguyên theo template. Không soạn lại.

### Mục 2: Năng lực và kinh nghiệm

Có **hai** phần riêng — đều phải xử lý (hỏi + điền). Không được chỉ làm nhân sự mà bỏ bảng số 01.

#### 2.1 Bảng số 01 — Tiêu chuẩn đánh giá về năng lực và kinh nghiệm (webform / bảng trong mẫu)

Bảng có các dòng (TT 1–4). AI **bắt buộc hỏi Manual** và ghi vào JSON `chuong_iii.muc_2_nang_luc.bang_tieu_chuan[]` (hoặc field tương đương), rồi tool mới được điền:

| TT | Nội dung | Cần Decision / điền gì |
|----|----------|-------------------------|
| 1 | Lịch sử không hoàn thành HĐ | **Năm** bắt đầu mốc (ô `năm ___`) — hỏi Manual (vd. 2023) |
| 2 | Nghĩa vụ thuế | Thường giữ theo mẫu; không bịa |
| 3 | Doanh thu bình quân | Hỏi: **Áp dụng** (kèm số tiền) hay ghi cột Yêu cầu **"Không áp dụng"** |
| 4 | Hợp đồng tương tự | Hỏi: số HĐ tối thiểu, khoảng thời gian (từ năm …), mô tả "tương tự" là gì; ghi vào cột Yêu cầu |

- **Cấm** để nguyên `năm ___` hoặc để trống cột Yêu cầu dòng 3/4 vì "rule nói bỏ qua doanh thu" mà không hỏi / không ghi "Không áp dụng".
- "Bỏ qua doanh thu" = sau khi Manual xác nhận, **điền chữ "Không áp dụng"** vào cột Yêu cầu dòng 3 — không phải bỏ qua cả bảng.

#### 2.2 Nhân sự chủ chốt

- Nhân sự chủ chốt: Dựa trên tính chất và yêu cầu của dự án để đưa ra số lượng / kinh nghiệm hợp lý. Tối thiểu phải có đủ các role sau: PM, SA, BA, Designer, Dev, QA, DevOp
- Kinh nghiệm: **phải đề xuất con số** (năm hoặc số hợp đồng tương tự) kèm confidence + lý do; hỏi Manual nếu chưa chắc. **Cấm** ghi kiểu "theo yêu cầu gói thầu" (đây chính là chỗ tạo yêu cầu).
- Chứng chỉ / trình độ: nếu không yêu cầu thì ghi rõ **"Không yêu cầu"**, không để trống.
- Tên vị trí ưu tiên tiếng Việt hành chính (có thể kèm tên role kỹ thuật).

### Mục 3: Kỹ thuật

- Chọn phương pháp: đạt/không đạt hoặc chấm điểm: Đề xuất lựa chọn phù hợp dựa vào tính chất của dự án và nêu lý do
- Gợi ý chấm điểm khi Fact có nhiều yêu cầu kỹ thuật / NFR đo được và nhiều hạng mục đề xuất cần phân biệt mức đáp ứng. Ngược lại có thể đề xuất đạt/không đạt.
- Manual chốt phương pháp; AI chỉ đề xuất.

#### Khi đề xuất hoặc chọn chấm điểm: bắt buộc ra bảng trong JSON

Không dừng ở một câu "nên chấm điểm". Phải dựng bảng gợi ý với các cột:

- STT: nhóm (A, B, C…) và tiêu chí con (A1, B1…)
- Nội dung đánh giá: tên tiêu chí (đánh giá đề xuất trên HSDT, không phải sản phẩm chạy thật)
- Điểm tối đa
- Điểm tối thiểu (sàn tiêu chí/nhóm nếu có) — **bắt buộc có số**, không để trống
- Thang điểm chi tiết: cách cho điểm đủ rõ để chấm được (ví dụ: đủ mô tả = max; chỉ cam kết chung = min; không có = 0)

Cách dựng bảng từ Fact (làm theo thứ tự) — **tham chiếu cấu trúc bản chuẩn**:

1. Có **hàng nhóm** A / B / C (tổng điểm nhóm + sàn nhóm)
2. Nhóm A: Phi chức năng
  - Mỗi NFR trong Fact thành một tiêu chí con A1, A2…
  - Tổng điểm nhóm A khoảng 30-40% thang (gợi ý; điều chỉnh và ghi lý do)
  - Thang chi tiết: HSDT có mô tả cách đạt / chỉ cam kết chung / không có
3. Nhóm B: Chức năng theo phân hệ
  - Lấy danh sách nhóm nghiệp vụ đã breakdown ở Chương V (cùng tên nhóm với Ch IV/V)
  - Mỗi nhóm (không phải từng dòng 1.1) thành một tiêu chí B1, B2…
  - Nội dung dạng: Đề xuất [tên nhóm], đủ theo yêu cầu KT Ch V
  - Tổng nhóm B thường là phần lớn còn lại của thang kỹ thuật
4. Nhóm C: Phạm vi / tiến độ / bàn giao
  - Từ Fact: phạm vi in/out, mốc vận hành/cut-over, danh sách deliverable, thời hạn trách nhiệm (nếu có)
  - Mỗi ý lớn thành một tiêu chí C1, C2…
5. Tổng hợp:
  - Tổng điểm tối đa = 100
  - Sàn tổng (gợi ý >= 70) và sàn từng nhóm A/B/C nếu dùng
  - Ghi rõ: đạt KT trên HSDT khi tổng >= sàn và (nếu có) đủ sàn từng nhóm
6. Điểm cụ thể:
  - AI đề xuất phân bổ điểm + confidence + lý do (bám Fact)
  - Đánh proposed; hỏi Manual nếu cần chốt số
  - Không lấy số từ HSMT gói khác

Output JSON gợi ý: `chuong_iii.bang_cham_diem[]` với các field: `stt`, `noi_dung`, `diem_toi_da`, `diem_toi_thieu`, `thang_chi_tiet`, `evidence_fact`, `confidence`.

#### Khi chọn đạt/không đạt:

- Mỗi tiêu chí có điều kiện Đạt rõ, dẫn về Ch V hoặc Fact.
- Vẫn nên nhóm theo NFR / phân hệ / phạm vi, bàn giao cho dễ đối chiếu.

### Mục 4: Tài chính

- Đề xuất mặc định theo thông lệ mẫu nếu phù hợp với dự án.
- Phương án kỹ thuật thay thế: không cần.

## Phạm vi cung cấp (đối chiếu Ch IV khi điền cùng gói)

- Địa điểm thực hiện: lấy từ Fact hoặc hỏi Manual. **Cấm** để `TBD` trong bản điền Word.

## Nên làm

- Hỏi manual nếu có các quyết định nào đó cần suy luận và lựa chọn ngoài Fact
- Đồng bộ tên nhóm chức năng với Ch IV và Ch V

## Không được

- Chỉ viết "chấm điểm 100, sàn 70" mà không có bảng tiêu chí
- Bịa giá, trọng số, số lượng nhân sự
- Chấm giá trong tiêu chí kỹ thuật
- Copy tiêu chí từ HSMT khác không cùng đầu vào
- Để trống điểm tối thiểu / thang chi tiết khi đã chọn chấm điểm
