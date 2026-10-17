# 3.5 Chuyển giao vận hành (M&O Transition)

## JSON

```json
"transition_intro": "...",
"transition": [
  {
    "item": "Deliverable sẵn sàng hỗ trợ vận hành",
    "ready": "Yes|No",
    "mitigation_if_no": ""
  }
]
```

## Gợi ý checklist ICT

- Deliverable / hệ thống sẵn sàng vận hành  
- Môi trường & quyền truy cập  
- Tài liệu vận hành / handover  
- Đào tạo end-user  
- UAT signed-off  
- Go-live / cut-over plan  
- Hypercare / support sau go-live  

`ready` = No → bắt buộc `mitigation_if_no` hoặc hỏi Manual.
