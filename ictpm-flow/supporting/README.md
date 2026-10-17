# Module Supporting Toolkit

Bộ form phụ trợ QLDA — cùng pipeline lõi: inventory → Fact → JSON → Manual `approved` → fill.

- Map nguồn: [`SOURCE_AND_MAP.md`](SOURCE_AND_MAP.md)
- Rules: [`rules/`](rules/)
- JSON: `artifacts/01_supporting.json`
- Skill: `.agents/skills/supporting/SKILL.md`

```bash
python3 ictpm-flow/supporting/tools/build_templates.py   # tạo lại template
python3 ictpm-flow/supporting/tools/fill_supporting.py --list
python3 ictpm-flow/supporting/tools/fill_supporting.py --all   # cần status=approved
```

Closure Report → `pm:closeout`.
