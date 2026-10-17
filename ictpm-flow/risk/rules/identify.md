# Identify Risks

## Việc cần làm

Xác định rủi ro có thể ảnh hưởng dự án và ghi đặc trưng: **Category → Risk Driver → Risk**.

## Cách điền mỗi rủi ro

- **Category**: System / Technical / Organization (hoặc category đã chốt trong Plan)
- **Driver**: nguyên nhân / điều kiện kích hoạt (không để trống)
- **Risk**: hậu quả đối với mục tiêu dự án (lịch, phạm vi, chất lượng, chi phí…)
- Evidence: dẫn Fact (id hoặc trích ngắn)
- Confidence + đánh dấu proposed nếu suy luận

## Gợi ý seed từ Fact (chỉ khi khớp dự án — không copy mù)

- Yêu cầu chưa rõ → trễ chốt requirement / rework
- Hệ thống lớn / nhiều phân hệ → ước lượng khó, trễ tiến độ
- NFR cao (24/7, đáp ứng nhanh…) → áp lực lịch và kiểm thử
- Công nghệ / tích hợp mới → debug và ổn định lâu hơn
- Package / hệ thống sẵn có khó tùy biến
- End-user / nghiệp vụ không tham gia đủ → thiếu nhu cầu
- Thiếu kỹ sư / role chủ chốt → trễ bàn giao



## Nên làm

- Ưu tiên rủi ro bám phạm vi in/out, cut-over, tích hợp, nhân sự trong Fact
- Đồng bộ tên dự án / gói với HSMT nếu cùng nguồn



## Thêm rủi ro sau lần lập đầu (incremental)

- User / Manual mô tả rủi ro mới → AI phân tích đủ Category–Driver–Risk + P/I + strategy.
- Ghi vào `01_risk.json` bằng tool:

```bash
python3 ictpm-flow/risk/tools/add_risk.py --file <risk.json>
```

- Tool tự gán `R-00N`, tính **Priority A/B/C**, từ chối thiếu driver/risk hoặc P/I sai thang.
- Không sửa tay Excel làm nguồn sự thật — nguồn là JSON, rồi fill lại.



## Không được

- List rủi ro generic không driver / không evidence
- Bịa rủi ro pháp lý / tiền bạc ngoài Fact + Decision
- Thêm rủi ro A mà thiếu strategy / response_actions

