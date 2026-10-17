# Perform Risk Analysis — qualitative

## Việc cần làm

Chấm **Probability** và **Impact**, suy ra **Priority A/B/C** theo ma trận chuẩn của dự án.  
V1: **chỉ qualitative**. Quantitative chỉ khi Manual yêu cầu.

## Thang Probability

- **High**: từng xảy ra nhiều lần trong quá khứ (dự án / tổ chức tương tự)
- **Middle**: từng xảy ra vài lần
- **Low**: hiếm hoặc chưa xảy ra

## Thang Impact

- **Big**: tổ chức phải xử lý (ảnh hưởng lợi nhuận lớn, kiện tụng, khủng hoảng truyền thông…)
- **Middle**: cần team / đơn vị khác hỗ trợ mới xử lý được
- **Small**: team dự án tự xử trong buffer hiện có

## Ma trận Priority (bắt buộc — không tự bịa lệch)

| Probability \\ Impact | Big | Middle | Small |
|----------------------|-----|--------|-------|
| High | A | A | B |
| Middle | A | B | C |
| Low | B | C | C |

- **A**: ưu tiên ứng phó trước
- **B**: theo dõi và có phương án
- **C**: chấp nhận theo dõi nhẹ / Accept có điều kiện

`priority` trong JSON **phải** khớp bảng trên (tool tính lại khi thêm rủi ro / fill).  
Trên Excel, ma trận nằm **cùng sheet Register** phía trên sổ rủi ro.

Đánh giá lúc nhận diện ghi vào **Initial**. Sau ứng phó, đánh giá lại vào **Current** (cùng thang High/Middle/Low và Big/Middle/Small).

## Không được

- Dùng thang số tùy ý làm priority chính thay cho A/B/C
- Để trống P hoặc I rồi vẫn gán A/B/C
