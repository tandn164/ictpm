# Module Master Plan

Lập **Project Management Plan** (kế hoạch quản lý dự án tổng thể) cho ICTPM.

Map: [`SOURCE_AND_MAP.md`](SOURCE_AND_MAP.md) · Input động: [`rules/inputs.md`](rules/inputs.md).

```text
ictpm-flow/masterplan/
  templates/_source/     # upstream nội bộ (không sửa)
  templates/masterplan.docx
  rules/
  tools/fill_masterplan.py
  artifacts/
    inputs/
```

Lệnh: `pm:masterplan`

```bash
python3 ictpm-flow/masterplan/tools/fill_masterplan.py
python3 ictpm-flow/masterplan/tools/fill_masterplan.py --force
```
