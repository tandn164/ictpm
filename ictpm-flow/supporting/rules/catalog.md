# Catalog

| ID | File template | Draft sau approved |
|----|---------------|--------------------|
| `stakeholder_analysis` | `templates/01_stakeholder_analysis.xlsx` | `artifacts/stakeholder_analysis_draft.xlsx` |
| `issues_actions` | `templates/02_issues_actions.xlsx` | `artifacts/issues_actions_draft.xlsx` |
| `phase_exit_checklist` | `templates/03_phase_exit_checklist.docx` | `artifacts/phase_exit_checklist_draft.docx` |
| `peer_evaluation` | `templates/04_peer_evaluation.docx` | `artifacts/peer_evaluation_draft.docx` |
| `selection_matrix` | `templates/05_selection_matrix.xlsx` | `artifacts/selection_matrix_draft.xlsx` |
| `portfolio` | `templates/06_portfolio.xlsx` | `artifacts/portfolio_draft.xlsx` |
| `stakeholder_post_eval` | `templates/07_stakeholder_post_evaluation.docx` | `artifacts/stakeholder_post_evaluation_draft.docx` |
| `post_impl_survey` | `templates/08_post_implementation_survey.docx` | `artifacts/post_implementation_survey_draft.docx` |
| `project_review_closure` | *(alias)* | `pm:closeout` → `fill_closeout.py` |

```bash
python3 ictpm-flow/supporting/tools/fill_supporting.py --list
python3 ictpm-flow/supporting/tools/fill_supporting.py --doc stakeholder_analysis
python3 ictpm-flow/supporting/tools/fill_supporting.py --all
python3 ictpm-flow/supporting/tools/fill_supporting.py --all --force   # chỉ khi debug
```
