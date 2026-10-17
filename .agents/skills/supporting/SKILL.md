---
name: supporting
description: >-
  Bộ phụ trợ QLDA (stakeholder, issues/actions, phase exit, peer eval, selection
  matrix, portfolio, post-eval, post-impl survey) trong ictpm-flow/supporting:
  inventory input động, Fact, đề xuất JSON kèm confidence, hỏi Manual khi thiếu,
  validate, chỉ fill sau approved. Dùng khi pm:supporting, pm:toolkit, phụ trợ,
  checklist phase, peer evaluation, portfolio, post-impl survey.
---

# Skill Supporting Toolkit

Toàn bộ: `ictpm-flow/supporting/`.

Đọc `SOURCE_AND_MAP.md` + **`rules/inputs.md`** + `rules/content.md` + `rules/validation.md` + `rules/catalog.md`.

Trả lời **tiếng Việt**. Không tự `approved`.

## Input động

Chi tiết: `rules/inputs.md`.

| Slot | Vai trò |
|------|---------|
| `masterplan_json` | Meta, roles, communications, schedule |
| `risk_json` | Issues/watch từ risk A/B |
| `closeout_json` | Post-eval / survey / phase đóng |
| `hsdt` / `wbs` / `master_schedule` | Bổ sung Fact |
| `@file` | Điểm peer, khảo sát thô… |

### Bước 0

1. Inventory → `inputs.inventory` + `docs_requested`.  
2. Thiếu định danh dự án → hỏi Manual (Q-SUP-IN-*).  
3. Không bịa điểm peer / Likert / issue không có Fact.

## Output

| File | Khi nào |
|------|---------|
| `artifacts/01_supporting.json` | Sau inventory + đề xuất + validate |
| `artifacts/bao_cao_kiem_tra.md` | Mỗi vòng |
| `artifacts/*_draft.xlsx\|docx` | Chỉ khi `approved` + tool |

## Pipeline

1. Inventory slot (`rules/inputs.md`).  
2. Fact từ slot `found`.  
3. Đề xuất `documents.<id>` theo `rules/content.md`; thiếu → `questions_for_manual[]`.  
4. Validate `rules/validation.md` → `ready_for_review` — **dừng chờ Manual**.  
5. Manual `approved` →:

```bash
python3 ictpm-flow/supporting/tools/fill_supporting.py --all
# hoặc
python3 ictpm-flow/supporting/tools/fill_supporting.py --doc stakeholder_analysis
```

## Catalog

| ID | Tài liệu |
|----|----------|
| `stakeholder_analysis` | Phân tích stakeholder |
| `issues_actions` | Issues & Action Items |
| `phase_exit_checklist` | Phase Exit Checklist |
| `peer_evaluation` | Peer Evaluation |
| `selection_matrix` | Selection Decision Matrix |
| `portfolio` | Portfolio |
| `stakeholder_post_eval` | Post Project Evaluation |
| `post_impl_survey` | Post-Implementation Survey |
| `project_review_closure` | → `pm:closeout` |

## Checklist hỏi Manual

| ID | Khi nào |
|----|---------|
| Q-SUP-IN-* | Slot missing / thiếu định danh |
| Q-SUP-DOC | Lập doc nào (`docs_requested`)? |
| Q-SUP-PEER | Điểm peer 1–5 (hoặc bỏ qua điểm)? |
| Q-SUP-SURVEY | Likert / respondent thực tế? |
| Q-SUP-GATE | Quyết định phase exit? |
| Q-SUP-SEL | Tiêu chí/trọng số selection? |
| Q-SUP-06 | Duyệt JSON → `approved` + fill? |

## Cấm

- Tự `approved` / fill khi chưa approved.  
- Hardcode tên file input.  
- Bịa điểm peer, Likert, issue không có Fact/Decision.  
- Duplicate Closeout Report.  
- Dump `{confidence…}` vào file giao nộp.  
- Branding nguồn template trong draft.
