# Báo cáo kiểm tra — Supporting Toolkit

- **Status:** `approved`
- **Ngày:** 2026-10-17
- **Rules:** ictpm-flow/supporting/rules @ 2026-10-17

## Decision Manual (2026-10-17)

| ID | Quyết định |
|----|------------|
| Q-SUP-PEER | Điểm peer 1–5 (agent đề xuất theo vai trò) |
| Q-SUP-SURVEY | Respondent + Likert |
| Q-SUP-GATE | Conditional Go |
| Q-SUP-SEL | Tính totals selection |
| Q-SUP-POST-RATING | Rating post-eval 1–5 |
| Q-SUP-06 | approved + fill toàn bộ draft |

## Selection totals

- Trọng số tổng: 1.0
- Phương án A: **4.1**

## Fill

```bash
python3 ictpm-flow/supporting/tools/fill_supporting.py --all
```

Validate: meta khớp Master Plan; điểm peer/Likert/rating có Decision; gate Conditional Go; không dump confidence vào file.
