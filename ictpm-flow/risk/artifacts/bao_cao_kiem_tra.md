# Báo cáo kiểm tra Risk — vòng 3 (đủ điều kiện chờ `approved`)

**JSON:** `ictpm-flow/risk/artifacts/01_risk.json` · 16 rủi ro (A=7, B=6, C=3) · `status=ready_for_review`

## Decision Manual đã đủ (Q-R01 → Q-R09)
| Câu | Chốt |
|-----|------|
| Q-R01 | Úu tiên WBS làm baseline lịch duy nhất |
| Q-R02 | Bổ sung category Regulatory + Vendor |
| Q-R03 | (đã thay bởi Q-R09) |
| Q-R04 | Cadence hằng tuần + mốc M0–M6; owner mặc định PM Nguyễn Đức Tân |
| Q-R05 | Toàn bộ rủi ro A dùng Mitigate |
| Q-R06 | Có định lượng EMV |
| Q-R07 | **Duyệt toàn bộ 16 rủi ro** |
| Q-R08 | Lệch BĐDT: ưu tiên HSDT (Áp dụng 1% = 8.976.000 VNĐ) |
| Q-R09 | **Dự phòng rủi ro 10% = 89.760.000 VNĐ** |

## Định lượng cuối
- Tổng EMV rủi ro A: **141.000.000 VNĐ (15,7% ngân sách)**
- Dự phòng (Q-R09): **89.760.000 VNĐ (10%)**
- Chênh lệch còn lại: **51.240.000 VNĐ** → xử lý bằng change request / mở rộng dự phòng nếu cần.

## Kiểm tra A/B/C
- Không còn câu hỏi mở (`questions_for_manual` rỗng).
- 0 vi phạm ma trận/priority; rủi ro A đủ strategy + action; category ⊂ Plan.
- Plan đủ 5 khối; Monitor có cadence + review_questions.

## Việc kéo theo
- `01_hsmt.json` (đang `approved`) có 18.9 = "Không áp dụng" → lệch với Q-R08 (ưu tiên HSDT, Áp dụng 1%). Cần mở lại HSMT (`ready_for_review`) rồi fill lại nếu bạn muốn đồng bộ.
- Đóng Excel đang mở (`~$01_risk_draft.xlsx`) trước khi fill.

## Dừng chờ Manual
Ghi `approved` → chạy:
```bash
python3 ictpm-flow/risk/tools/fill_risk.py
```
