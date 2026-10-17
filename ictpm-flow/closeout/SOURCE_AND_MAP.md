# Báo cáo tổng kết dự án — nguồn & map

## Nguồn gốc (upstream, không sửa)

| | |
|--|--|
| Template | **Project Closeout Document** (Connecticut DSS / CT-METS) |
| URL | https://portal.ct.gov/-/media/Departments-and-Agencies/DSS/CT-METS/Library/General/CTDSSProjectCloseoutReportv11.pdf |
| File lưu | `templates/_source/CTDSS_ProjectCloseoutReport_v11.pdf` |

Tham chiếu thêm (cấu trúc đóng dự án IT): Texas DIR *PM Essentials Project Closure*  
https://dir.texas.gov/resource-library-item/pm-essentials-project-closure-template  

**Draft / JSON / Word làm việc:** không ghi tên nguồn ngoài vào nội dung giao cho khách.

## Cấu trúc gốc → ICTPM

| Gốc (EN) | ICTPM (Việt) |
|----------|--------------|
| Project Information | Thông tin dự án (bìa) |
| Revision History | Lịch sử phiên bản |
| Management Effectiveness | Hiệu quả quản lý (baseline vs thực tế) |
| Lessons Learned | Bài học kinh nghiệm |
| Administrative Closure | Đóng hành chính / nghiệm thu |
| Contract Closure | Đóng hợp đồng |
| Information Distribution & Archive | Lưu trữ & phân phối |
| Appendix A Approval | Phê duyệt đóng dự án |
| Appendix B References | Tham chiếu |
| *(bổ sung ICTPM)* | Bảng deliverable chấp nhận; hạng mục còn mở |

## Map Fact

| Section | Slot / module |
|---------|----------------|
| Meta / kết quả | `masterplan_json`, `hsdt` |
| Baseline vs thực tế | `wbs`, `master_schedule`, `masterplan_json` |
| Lessons / rủi ro còn lại | `risk_json`, Manual |
| Nghiệm thu / bàn giao | Manual, WBS transition |
| Cost thực tế | Manual Decision (thường thiếu → hỏi) |
| Archive | Manual liệt kê hoặc đề xuất từ artifact ICTPM |

Input động: `rules/inputs.md`.
