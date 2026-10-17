---
name: risk
description: >-
  Lập Risk Management Plan + Risk Register theo module ictpm-flow/risk: inventory
  input động, Fact, đề xuất Plan/risks kèm confidence, hỏi Manual khi thiếu
  nguồn Fact, validate A/B/C, JSON; thêm rủi ro; chỉ fill Excel sau approved.
  Dùng khi pm:risk, thêm rủi ro, kế hoạch quản lý rủi ro, risk register, RMP.
---

# Skill Risk Management

Toàn bộ tài nguyên nằm trong `ictpm-flow/risk/`.

Đọc **`rules/inputs.md`** + toàn bộ `rules/` trước khi làm.

Trả lời **tiếng Việt**. Không tự `approved`.

## Input động (không hardcode tên file)

Chi tiết slot / pattern: `rules/inputs.md`.

| Slot | Vai trò |
|------|---------|
| `hsmt_json` | Fact HSMT đã lập |
| `rfp` | RFP.pdf hoặc tương đương |
| `hsdt` | HSDT (thường ở masterplan `artifacts/inputs/`) |
| `wbs` / `master_schedule` | Tiến độ / phase → rủi ro lịch |
| `masterplan_json` | PMP đã có |
| `@file` trong chat | Ưu tiên gắn đúng slot |

### Bước 0 — bắt buộc mỗi lần chạy

1. Quét slot → ghi `inputs.inventory` (`found` / `missing` / `skipped` + `path`).
2. **Không có nguồn Fact nào** → Q-R-IN-01 hỏi Manual (gửi HSMT/RFP/HSDT/WBS/… hoặc dán Fact); **không** bịa `risks[]`.
3. Manual bổ sung / skip có điều kiện → cập nhật inventory, chạy tiếp.
4. File đổi tên hoặc user @ file mới → inventory lại.

Template fill (cố định): `ictpm-flow/risk/templates/risk-management.xlsx`.

## Output

| File | Khi nào |
|------|---------|
| `ictpm-flow/risk/artifacts/01_risk.json` | Sau inventory + đề xuất + validate |
| `ictpm-flow/risk/artifacts/bao_cao_kiem_tra.md` | Mỗi vòng (kèm inventory) |
| `ictpm-flow/risk/artifacts/01_risk_draft.xlsx` | Chỉ khi `status=approved` + chạy tool |

## Pipeline

1. **Inventory input** (`rules/inputs.md`).
2. Thu thập Fact từ slot `found`.
3. Đọc rule → đề xuất `plan{}` + `risks[]`; thiếu Decision → `questions_for_manual[]`.
4. Analyze: P/I; **priority = ma trận A/B/C** (`rules/analyze.md`).
5. Respond: mọi rủi ro **A** (và B nên có) đủ strategy + actions.
6. Validate `rules/validation.md` (≤3 vòng A/B; C hỏi Manual).
7. `ready_for_review` + báo cáo — **dừng chờ Manual**.
8. Manual `approved` →:

```bash
python3 ictpm-flow/risk/tools/fill_risk.py
```

## Thêm rủi ro (`pm:risk add` / “thêm rủi ro …”)

Khi user mô tả rủi ro mới (hoặc dán danh sách):

1. Đọc `rules/identify.md` + `analyze.md` + `respond.md`.
2. Phân tích → đề xuất object: `category`, `driver`, `risk`, `probability`, `impact`, `strategy`, `response_actions`, `owner`, `evidence`, `confidence`.
3. **Priority không tự bịa** — để tool tính theo ma trận.
4. Hiện bảng đánh giá cho Manual (P / I / Priority / Strategy). Priority **A** + Accept/Transfer → hỏi xác nhận.
5. Manual đồng ý → ghi file tạm JSON rồi chạy:

```bash
python3 ictpm-flow/risk/tools/add_risk.py --file /tmp/new_risk.json --dry-run
python3 ictpm-flow/risk/tools/add_risk.py --file /tmp/new_risk.json
python3 ictpm-flow/risk/tools/add_risk.py --file /tmp/new_risk.json --refill --force-refill
```

6. JSON đang `approved` mà thêm risk → tool **hạ** về `ready_for_review`.

Evidence của risk mới: ghi rõ slot/path Fact (vd. `hsdt:…/HSDT.docx`) khi có.

## Checklist hỏi Manual

| ID | Khi nào |
|----|---------|
| Q-R-IN-* | Không có / thiếu nguồn Fact — gửi file hoặc dán Fact? |
| Q-R01 | Ưu tiên nguồn nào khi nhiều slot `found`? |
| Q-R02 | Risk categories |
| Q-R03 | Budgeting %/số |
| Q-R04 | Cadence Monitor + Owner mặc định |
| Q-R05 | Rủi ro A chọn Transfer/Accept |
| Q-R06 | Quantitative? (mặc định Không) |
| Q-R07 | Duyệt `risks[]` trước fill |

## Ma trận Priority

| P \\ I | Big | Middle | Small |
|--------|-----|--------|-------|
| High | A | A | B |
| Middle | A | B | C |
| Low | B | C | C |

## Cấm

- Tự `approved` / fill khi chưa approved.
- Hardcode tên file input cụ thể.
- Lập register khi inventory trống (không có Fact).
- Priority lệch ma trận; rủi ro A thiếu strategy.
- Bịa số budgeting / điều khoản pháp lý.
- Dump `{confidence, evidence…}` vào ô Excel (chỉ `value`).
