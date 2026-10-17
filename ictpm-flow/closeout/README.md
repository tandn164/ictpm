# Module Báo cáo tổng kết dự án (Closeout)

Lập **Project Closeout Report** — đánh giá kết quả, lessons learned, đóng hành chính/HĐ, lưu trữ.

Nguồn upstream (nội bộ): xem [`SOURCE_AND_MAP.md`](SOURCE_AND_MAP.md).  
Input động: [`rules/inputs.md`](rules/inputs.md).

```text
ictpm-flow/closeout/
  templates/_source/     # PDF gốc (tham chiếu)
  templates/closeout.docx
  rules/
  tools/fill_closeout.py
  artifacts/
```

Lệnh: `pm:closeout`

```bash
python3 ictpm-flow/closeout/tools/fill_closeout.py
python3 ictpm-flow/closeout/tools/fill_closeout.py --force
```
