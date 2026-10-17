# Map nội dung theo tài liệu

Mỗi object trong `documents.<id>`: chỉ `value` plain khi fill; confidence/evidence giữ trong JSON.

## `stakeholder_analysis`

Nguồn: `roles[]` + `communications[]` (Master Plan) + HSDT.  
Mỗi dòng: `name`, `role`, `power` (High/Middle/Low), `interest` (High/Middle/Low), `strategy` (Manage Closely / Keep Satisfied / Keep Informed / Monitor), `owner`, `engagement`, `notes`.  
Ma trận Quyền lực–Quan tâm: cùng tập stakeholder; không bịa người ngoài Fact.

## `issues_actions`

Nguồn: `masterplan.issues[]`, `closeout.admin_closure.open_items[]`, rủi ro Priority A/B còn theo dõi (ghi rõ `related_risk`).  
Mỗi dòng: `id`, `type` (Issue|Action), `description`, `priority` (High/Middle/Low), `status`, `owner`, `due`, `action`, `related_risk`.  
Master Plan `issues=[]` và không có open item → hỏi Manual hoặc để `items=[]` + ghi rõ.

## `phase_exit_checklist`

Nguồn: WBS phase / schedule + closeout deliverables (nếu có).  
Header: `phase`, `gate_decision`, `gate_conditions`, `review_date`.  
`items[]`: `item`, `status` (Done|Open|N/A), `evidence`, `owner`.  
Thiếu Decision gate → hỏi Q-SUP-GATE-*.

## `peer_evaluation`

Nguồn: `roles[]` (thành viên team).  
`evaluator`, `members[]` (`name`, `role`, `contribution`, `collaboration`, `quality`, `reliability`, `comment` — thang 1–5).  
**Cấm bịa điểm.** Chưa có Fact/Decision điểm → để trống + hỏi Manual; vẫn được điền tên/vai trò từ Fact.

## `selection_matrix`

Org-level. Cột tiêu chí + trọng số + phương án.  
Có thể đưa dự án hiện tại làm 1 phương án nếu Manual yêu cầu.  
Thiếu tiêu chí/trọng số → hỏi Manual, không tự chấm điểm “thắng”.

## `portfolio`

Danh mục dự án: `code`, `name`, `sponsor`, `pm`, `phase_or_status`, `budget`, `priority`, `risk_flag`, `notes`.  
Ít nhất 1 dòng từ dự án hiện tại nếu có Fact; không bịa danh mục tổ chức đầy đủ.

## `stakeholder_post_eval`

Nguồn: closeout lessons / effectiveness + Manual.  
`stakeholder_name`, `what_went_well`, `main_challenges`, `recommendations`, ratings (nếu có Decision).  
Không bịa rating Likert.

## `post_impl_survey`

Nguồn: closeout + Manual respondent.  
`respondent`, `role`, câu hỏi Likert + `improve_now`, `best_practice`.  
Không bịa điểm khảo sát thực tế.

## `project_review_closure`

Không lập trong module này → `pm:closeout`.
