# ICTPM — hướng dẫn agent

## HSMT

Khi chat có `pm:hsmt` / `@hsmt` / lập HSMT: đọc `.agents/skills/hsmt/SKILL.md`.

Module: **`ictpm-flow/hsmt/`**

- Rule: `ictpm-flow/hsmt/rules/`
- Template: `ictpm-flow/hsmt/templates/`
- Artifact: `ictpm-flow/hsmt/artifacts/`
- Tool: `ictpm-flow/hsmt/tools/fill_hsmt.py`

## Risk Management

Khi chat có `pm:risk` / `@risk` / kế hoạch quản lý rủi ro / risk register / **thêm rủi ro**: đọc `.agents/skills/risk/SKILL.md`.

Module: **`ictpm-flow/risk/`**

- Rule: `ictpm-flow/risk/rules/` (**input động:** `inputs.md`)
- Template: `ictpm-flow/risk/templates/`
- Artifact: `ictpm-flow/risk/artifacts/`
- Tool: `ictpm-flow/risk/tools/fill_risk.py`, `add_risk.py` (append rủi ro đã phân tích)

## Master Plan

Khi chat có `pm:masterplan` / `@masterplan` / PMP / kế hoạch quản lý dự án tổng thể / master plan: đọc `.agents/skills/masterplan/SKILL.md`.

Module: **`ictpm-flow/masterplan/`**

- Map: `SOURCE_AND_MAP.md`
- **Input động** (`rules/inputs.md`): slot `hsdt` / `wbs` / `master_schedule` / … — thiếu hỏi Manual; `artifacts/inputs/` hoặc user `@`
- Rule / template / artifact / tool: trong module như trên

## Báo cáo tổng kết dự án (Closeout)

Khi chat có `pm:closeout` / `@closeout` / báo cáo tổng kết / đóng dự án / lessons learned / project closeout: đọc `.agents/skills/closeout/SKILL.md`.

Module: **`ictpm-flow/closeout/`**

- Map: `SOURCE_AND_MAP.md` (upstream Closeout Document — chỉ trong `_source`, không ghi vào draft)
- **Input động** (`rules/inputs.md`): `masterplan_json` / `risk_json` / `wbs` / `hsdt` / …
- Template: `templates/closeout.docx`
- Tool: `tools/fill_closeout.py`

## Supporting Toolkit

Khi chat có `pm:supporting` / `pm:toolkit` / stakeholder analysis / issues actions / phase exit / peer evaluation / selection matrix / portfolio / post-impl survey: đọc `.agents/skills/supporting/SKILL.md`.

Module: **`ictpm-flow/supporting/`**

- Map: `SOURCE_AND_MAP.md`
- **Input động** (`rules/inputs.md`): `masterplan_json` / `risk_json` / `closeout_json` / …
- Rule / template / artifact / tool: trong module như trên
- Tool: `tools/fill_supporting.py` (`--list` / `--doc <id>` / `--all`) — chỉ sau `approved`
- Closure Report trong list → dùng `pm:closeout`, không duplicate

---

Trả lời tiếng Việt. Không tự `approved`.  
**Input:** không hardcode tên file; mỗi lần chạy inventory slot → thiếu hỏi Manual.
