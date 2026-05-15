# Prompt Bắt Đầu - SMS Marketing Project

## PROMPT 0 - Load context (dùng đầu MỖI phiên làm việc mới)
```
Dự án SMS Marketing VN. Đọc theo thứ tự: README.md -> CLAUDE.md -> TODO_NGAYMAI.md.
Sau đó tóm tắt ngắn: đang ở giai đoạn nào, việc ưu tiên hôm nay là gì.
Hỏi tôi muốn làm task nào.
```

## PROMPT 1 - Research thêm provider
```
Đọc rules/01_research.md. Research [TÊN PROVIDER / URL] theo format trong file đó.
Thu thập đủ: giá/tin, dịch vụ, API, reseller/affiliate program, website style.
Cập nhật vào research/research/nha_cung_cap.md (thêm vào bảng đã có, không ghi đè).
```

## PROMPT 2 - Cập nhật / kiểm tra lại giá
```
Đọc rules/01_research.md + research/research/gia_ca.md.
Crawl lại trang giá của [PROVIDER] - kiểm tra có thay đổi không.
Cập nhật file, ghi rõ ngày kiểm tra và thay đổi so với lần trước.
```

## PROMPT 3 - Làm website / content
```
Đọc rules/02_website.md + research/research/website_style.md.
Task cụ thể: [MÔ TẢ]
```

## PROMPT 4 - Phân tích cơ hội kinh doanh
```
Đọc rules/03_business.md + research/research/gia_ca.md + research/research/nha_cung_cap.md.
Phân tích: provider nào phù hợp nhất để làm reseller/affiliate? Lý do? Bước tiếp theo?
```

## PROMPT 5 - Tóm tắt cuối phiên / lưu context
```
Tóm tắt những gì đã làm hôm nay. Cập nhật TODO_NGAYMAI.md.
Có file nào cần tạo thêm để lưu thông tin quan trọng không?
```
