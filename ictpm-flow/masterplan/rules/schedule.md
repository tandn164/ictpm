# 3.2 Quản lý tiến độ

## JSON

```json
"schedule": [
  {
    "milestone": "Kickoff",
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD",
    "actual_or_pct": "",
    "owner": "PM"
  }
]
```

## Gợi ý phase ICT

Kickoff → Phân tích/Thiết kế → Xây dựng → Kiểm thử tích hợp → UAT → Go-live / Cut-over → Ổn định (hypercare).

## Nguồn ngày / mốc

1. Slot **`wbs`** (nếu found): mốc cấp 1–2 + Bắt đầu/Kết thúc/Phụ trách.  
2. Slot **`master_schedule`**: ngày theo danh mục dịch vụ — bổ sung hoặc đối chiếu.  
3. Lệch nhau → Q-MP08 (Manual chốt baseline).  
4. Cả hai missing → hỏi Manual ngày (Q-MP02 / Q-MP-IN-*).

Ngày thiếu → không bịa. Không dump toàn bộ WBS/Gantt vào bảng Schedule Mini.
