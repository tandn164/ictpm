# Master Plan — cấu trúc & map ICTPM

## Template làm việc

| | |
|--|--|
| File | `templates/masterplan.docx` |
| Upstream (nội bộ, không sửa) | `templates/_source/pmp_mini_upstream.docx` |

## Cấu trúc tài liệu

1. **Tóm tắt dự án** — nhu cầu, scope in/out, giả định, ràng buộc, cách quản lý  
2. **Vai trò và trách nhiệm** — Name / Role / Responsibility  
3. **Kế hoạch thành phần**
   - Quản lý giao tiếp  
   - Quản lý tiến độ (milestone)  
   - Quản lý vấn đề  
   - Quản lý rủi ro (tóm tắt → module risk, priority A/B/C)  
   - Chuyển giao vận hành (M&O)  
4. **Phụ lục A — Cost** · **Phụ lục B — Quality** · Phê duyệt  

## Map section → nguồn Fact

| Section | Slot / module |
|---------|----------------|
| Bìa / meta | `hsdt`, Manual |
| Tóm tắt / scope | `hsdt`, `wbs`, `hsmt_json` |
| Roles | `wbs` (Phụ trách), `hsdt` (nhân sự), Manual |
| Communications | Manual, WBS họp tiến độ |
| Schedule | `wbs`, `master_schedule` |
| Issues | Runtime / Manual |
| Risk tóm tắt | `risk_json` |
| M&O Transition | `wbs` (go-live), Manual |
| Cost | `hsdt` |
| Quality | `hsdt`, deliverable WBS |

Input động: `rules/inputs.md`.
