# Kiểm tra trước duyệt (Supporting)

## A. Thống nhất

- Tên / mã / PM khớp Master Plan hoặc HSDT / Closeout.
- `inputs.inventory` đã ghi; `docs_requested` khớp phần `documents.*.enabled`.
- Không còn `{{placeholder}}` / TBD trong value sẽ fill.
- Không dump `{confidence, evidence}` vào xlsx/docx (tool chỉ lấy `value` / plain field).

## B. Fact

- Stakeholder / roles lấy từ nguồn `found`.
- Issue/action có evidence hoặc ghi `related_risk` / Decision.
- Peer score / survey Likert: trống hoặc có Decision — **không** số bịa.
- Phase exit status khớp deliverable/Fact nếu đánh Done.

## C. Decision

- Doc nào `enabled` cần Manual xác nhận (đặc biệt peer/survey/selection).
- Gate phase exit (nếu enabled).
- Duyệt `ready_for_review` → Manual `approved` rồi mới fill.

## D. Format draft

- Times New Roman 14 (nội dung).
- Không branding nguồn template (Smartsheet, PM², …) trong file giao nộp.
