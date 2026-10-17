# Input động (Risk)

Không gắn cứng một tên file. Mỗi lần chạy: **quét → gắn slot → thiếu thì hỏi Manual**.

## Slot

| Slot | Bắt buộc? | Pattern / nơi tìm | Dùng cho |
|------|-----------|-------------------|----------|
| `hsmt_json` | Khuyến nghị | `ictpm-flow/hsmt/artifacts/01_hsmt.json` | Fact thầu, phạm vi, NFR |
| `rfp` | Khuyến nghị | `RFP.pdf`, `*RFP*` (root hoặc @) | Driver rủi ro từ yêu cầu |
| `hsdt` | Tuỳ | `artifacts/inputs/HSDT*.docx`, `*HSDT*.docx`, hoặc masterplan inputs | Cam kết thầu, tiến độ chào, nhân sự |
| `wbs` | Tuỳ | `*WBS*.xlsx` | Rủi ro tiến độ / phụ thuộc phase |
| `master_schedule` | Tuỳ | `*Schedule*.docx` | Cut-over / mốc liên quan rủi ro lịch |
| `masterplan_json` | Tuỳ | `ictpm-flow/masterplan/artifacts/01_masterplan.json` | Scope/schedule đã chốt trong PMP |
| `other` | Tuỳ | File / Fact Manual dán trong chat | Bổ sung |

**Tối thiểu để lập Risk:** ít nhất **một** nguồn Fact (`hsmt_json` | `rfp` | `hsdt` | `wbs` | `masterplan_json` | Manual dán Fact).  
Thiếu hết → hỏi Manual, **không** bịa register generic.

## Quy trình mỗi lần `pm:risk`

1. **Inventory** slot (path thật; file user @ thắng pattern).
2. Ghi JSON:
   ```json
   "inputs": {
     "inventory": {
       "hsmt_json": {"status": "missing", "path": null},
       "rfp": {"status": "found", "path": "RFP.pdf"},
       "hsdt": {"status": "found", "path": "ictpm-flow/masterplan/artifacts/inputs/HSDT.docx"},
       "wbs": {"status": "found", "path": "…/02_WBS.xlsx"}
     }
   }
   ```
3. Không có nguồn Fact nào `found` → `questions_for_manual` (Q-R-IN-01) và dừng đề xuất risks đầy đủ.
4. Có Fact nhưng thiếu budgeting / owner / cadence → hỏi như checklist Q-R0x (không đổi).
5. Manual bổ sung file hoặc `skipped` + Decision → cập nhật inventory, chạy tiếp.

## Ưu tiên Fact khi nhiều slot

1. Decision Manual  
2. HSMT JSON / HSDT (cam kết)  
3. WBS / Master Schedule / Masterplan JSON  
4. RFP  

Lệch nhau → hỏi Manual, không tự hòa.

## Cấm

- Hardcode một tên HSDT/WBS cụ thể.
- Lập `risks[]` chỉ từ “kinh nghiệm chung” khi inventory trống.
- Bịa số budgeting.
