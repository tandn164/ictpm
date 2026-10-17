# Plan Risk Responses

## Việc cần làm

Với mỗi rủi ro (bắt buộc mọi **A**, khuyến nghị mọi **B**): chọn chiến lược và hành động.

## Chiến lược (threat) — chọn đúng 1

- **Avoid**: đổi kế hoạch để loại bỏ mối đe dọa
- **Transfer**: chuyển tác động / trách nhiệm cho bên thứ ba (bảo hiểm, thầu phụ, điều khoản HĐ) — cần Decision / `contract_link` nếu liên quan HSMT
- **Mitigate**: giảm xác suất hoặc tác động
- **Accept**: chấp nhận; có thể kèm contingency (active) hoặc không làm gì thêm (passive)

## Sau khi chọn strategy — ghi đủ khi có

- **response_actions**: việc cụ thể ai làm gì
- **contingency**: Plan B nếu rủi ro xảy ra
- **residual**: rủi ro còn lại sau ứng phó
- **secondary**: rủi ro mới do chính phương án ứng phó tạo ra
- **owner**: người chịu trách nhiệm theo dõi

## Initial vs Current (bắt buộc hiểu khi điền Register)

Giống sổ rủi ro chuẩn dự án:

- **Initial** (`probability` / `impact` / `priority`): lúc nhận diện — trước khi thực hiện ứng phó
- **Current** (`probability_current` / `impact_current` / `priority_current`): đánh giá lại **sau** khi đã có response (mức residual còn lại)

Khi Mitigate/Avoid/Transfer có hiệu lực: Current thường thấp hơn Initial.  
Khi chưa triển khai ứng phó: để Current trống (không copy Initial cho có).

## Nên làm

- Rủi ro A mà Accept: hỏi Manual xác nhận
- Transfer: hỏi Manual điều khoản hợp đồng / bảo hiểm liên quan
- Cập nhật Current khi monitor thấy thay đổi

## Không được

- Để rủi ro A không có strategy + action
- Bịa điều khoản pháp lý / số tiền bảo hiểm
- Coi Current = Initial mãi khi đã Mitigate xong (phải đánh giá lại)

