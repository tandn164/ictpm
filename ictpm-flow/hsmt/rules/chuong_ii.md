# Chương II Bảng dữ liệu đấu thầu

## Việc cần làm

Điền thủ tục gói thầu trên E-BDL: chủ đầu tư, tên gói/dự án, lịch, bảo đảm dự thầu, hiệu lực HSDT, nhà thầu phụ, liên hệ, và các chỗ đầu vào khác hình thức đấu thầu qua mạng.

## Thông tin bổ sung:

- Có nhờ bên Công ty công nghệ cổ phần Ekotek hỗ trợ tư vấn thiết kế kỹ thuật
- Không chấp nhận các đề xuất thay thế

## Cách điền

- Với các mục [Hệ thống tự động trích xuất] hoặc tương tự thì bỏ qua.
- Các phần liên quan đến các thông tin liên hệ, thông tin chủ đầu tư cần bám sát tài liệu Fact
- Với các mục không tìm được thông tin cần thiết hay suy luận được thông tin cần thiết thì phải báo cáo hoặc hỏi lại.
- Với các phần được template nêu rõ lựa chọn 1 trong các phần để trích dẫn thì cần lựa chọn phù hợp dựa vào tính chất của dự án. Nêu rõ lý do và confidence trong output
- Với các phần cần suy luận để điền nội dung thì phải nêu rõ lý do và confidence trong output.
- Văn bản HSMT: **tiếng Việt có dấu**. Đầu mục / gạch đầu dòng: **xuống hàng** đúng cấu trúc template.
- Khi điền Word: **giữ khung pháp lý** của template (đoạn NĐ-CP, câu hướng dẫn). Chỉ thay chỗ trống hoặc dòng lựa chọn. Không xóa phần còn lại của ô.
- Thiếu Decision → **không điền**, để trống theo template và hỏi Manual. Không đoán.

### Ghi chú theo từng E-CDNT (bắt buộc tuân thủ)

- **5.1**: Template yêu cầu **tên và địa chỉ** Chủ đầu tư. **Bắt buộc hỏi Manual** chuỗi đầy đủ (vd. "Công ty Cổ phần ABC Wear, địa chỉ …"). **Cấm** tự điền chỉ từ tên ngắn trong Fact (vd. "ABC Wear") rồi coi như xong. Giữ nguyên các đoạn trường hợp công ty mẹ/con.
- **7.5 Hội nghị tiền đấu thầu**: Chỉ ghi Có/Không sau **Decision Manual**. Thuyết trình nộp đề xuất trong Fact **không** đồng nghĩa hội nghị tiền đấu thầu. Không tự chốt.
- **10.8 Tài liệu nộp kèm**: Suy luận danh mục từ yêu cầu gói + thông lệ pháp lý Việt Nam (đăng ký DN, năng lực, nhân sự…). Nếu không có yêu cầu thêm thì ghi rõ **"không yêu cầu"**. Không bịa số hiệu văn bản ngoài những gì đã có trong template/rule.
- **18.2 / 18.4 / 18.9** (cặp bảo đảm dự thầu):
  - Hỏi Manual: **Áp dụng** hay **Không áp dụng**.
  - Nếu **Không áp dụng**: 18.9 ghi "Không áp dụng"; **không** tự điền % vào 18.2; giữ khung 18.2 theo template nếu chưa có giá trị hệ thống.
  - **18.4 luôn phải hỏi riêng** số ngày hoàn trả (≤14), kể cả khi 18.9 = Không áp dụng (không được bỏ quên vì đã chọn Không áp dụng).
  - Nếu **Áp dụng**: hỏi thêm giá trị/% (18.2 chỉ thay chỗ giá trị, giữ đoạn NĐ-CP).
- **28.2** (dạng chọn 1 trong 2 — hay điền sai):
  - Template đang để **hai dòng hướng dẫn** ("Chọn phương pháp giá thấp nhất thì trích xuất: …" / "Chọn phương pháp giá đánh giá thì trích xuất: …").
  - Cách điền đúng: sau khi Manual chốt phương pháp tài chính ở 29.1, **xóa cả hai dòng hướng dẫn**, chỉ giữ **một** câu đã trích (đúng như bản chuẩn). Giữ câu mở đầu về NĐ-CP.
  - **Sai**: để nguyên cả hai nhánh / ghi "giữ template" / copy nguyên khối hướng dẫn.
  - Giá thấp nhất → câu có "…vào **giá dự thầu** trừ đi giá trị giảm giá…". Giá đánh giá → câu có "…vào **giá đánh giá**…".
- **28.8**: Hỏi Manual; mặc định đề xuất "không có" nếu Fact/rule không nêu ưu đãi khác.
- **29.1**: Viết đúng 3 gạch đầu dòng như template (năng lực / kỹ thuật / tài chính). Văn phong hành chính, không nhét mã Decision/Q0x.
- **29.3**: Chọn câu xếp hạng khớp phương pháp tài chính ở 29.1 (giá thấp nhất hoặc giá đánh giá).
- **31.4** (cùng kiểu chọn 1 trong 2 với 28.2 — hay điền sai):
  - Template có khối `[Hệ thống trích xuất…]` với **hai** nhánh. Điền đúng: bỏ khối hướng dẫn, chỉ còn **một** dòng đã chọn + **giữ** đoạn "Đối với gói thầu được chia làm nhiều phần (lô)…".
  - Giá thấp nhất → "Nhà thầu có giá dự thầu sau khi trừ đi giá trị giảm giá (nếu có) thấp nhất".
  - Giá đánh giá → "Nhà thầu có giá đánh giá thấp nhất".
  - **Sai**: để nguyên cả hai dòng "Chọn phương pháp…".
- **31.5**: Template có chỗ trống + **hai** nhánh theo loại hợp đồng trong ngoặc vuông. **Bắt buộc hỏi Manual** loại hợp đồng (trọn gói / đơn giá / thời gian / kết quả đầu ra / tỷ lệ %). Điền đúng: ghi một câu tương ứng vào sau "Giá gói thầu để làm căn cứ xét duyệt trúng thầu:" và **xóa** khối hướng dẫn trong `[…]`. Không tự chọn loại hợp đồng.
- **34.1 / 34.2 / 38.1 / 38.2**: Mỗi mã một nội dung riêng. Hỏi Manual tỷ lệ tăng/giảm, tùy chọn mua thêm, người có thẩm quyền, quy trình kiến nghị. **Cấm** copy cùng một đoạn vào nhiều ô.

## Nên làm

- Hỏi manual nếu có các quyết định nào đó cần suy luận và lựa chọn ngoài Fact

## Không được

- Bịa số liệu thủ tục.
- Bịa các nghị định hay các vấn đề liên quan đến pháp luật
- Tự quyết định các quyết định quan trọng có liên quan đến tiền hay hợp đồng.
- Đồng nhất hóa / ghi đè nhầm mã E-CDNT (ví dụ ô 3 làm hỏng 31.x, 34.x, 38.x).
