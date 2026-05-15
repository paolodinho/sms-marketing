# Hướng Dẫn Tìm Domain Có Backlink Báo Việt Nam

Cập nhật: 11/05/2026

## THỰC TẾ PHÁT HIỆN (Research 11/05/2026)

**Domain squatter .vn SMS rất nghiêm trọng**: Đã check 50+ domain keyword SMS/brandname/marketing, TẤT CẢ đều đã bị đăng ký. Không tìm được domain available với keyword thông thường.

**Lý do**: Domain squatter Việt Nam đăng ký hàng loạt keyword .vn từ ~2015-2020 (giá rẻ, chỉ 230k/năm) và giữ mà không build website.

**Hệ quả**: Cần pivot sang 1 trong 3 hướng bên dưới.

---

---

## 3 Cách Tìm Domain (từ dễ đến khó)

### Cách 1: Mua backlink báo cho domain mới (DỄ NHẤT, ~500k-2tr VND)

Đăng ký domain keyword mới -> mua backlink từ báo VN.

**Bước thực hiện:**
1. Đăng ký domain tại matbao.net hoặc nhanhoa.com:
   - `guisms.vn` (~230k/năm) - "gửi SMS"
   - `smsgiare.vn` (~230k/năm) - từ khóa target
   - `smsplatform.vn` - B2B rõ ràng
2. Mua 3-5 backlink báo từ dịch vụ:
   - [famemedia.vn/backlink-bao](https://famemedia.vn/backlink-bao/) - từ 500k/bài
   - [muabacklinkbao.com](https://muabacklinkbao.com/) - từ 300k/bài
   - [seoranklead.com/dich-vu-backlink-bao](https://seoranklead.com/dich-vu-backlink-bao)
3. Yêu cầu đặt bài trên: cafebiz.vn, 24h.com.vn, ictnews.vn, baomoi.com

**Chi phí:** 1.5-5 triệu VND | **Thời gian:** 1-2 tuần

---

### Cách 2: Chạy Domain Hunter Agent (PYTHON SCRIPT)

Script tự động check availability + backlink.

```bash
# Cài thư viện
pip install requests beautifulsoup4 colorama

# Chạy full agent
cd "D:\claude\sms marketing\tools"
python domain_hunter.py

# Check nhanh 1 domain
python domain_hunter.py guisms.vn
python domain_hunter.py smsgiare.vn
```

**Script sẽ:**
- Check 15+ candidate domain có available không
- Search expired domain trên expireddomains.net
- Dùng Ahrefs free để check DR + referring domains
- Filter ra domain nào có báo VN đang link
- Xuất bảng xếp hạng + lưu JSON

**Lưu ý:** Ahrefs free cho ~10 check/ngày. Chạy 1 lần/ngày.

---

### Cách 3: Dùng DomCop (CÔNG CỤ TRẢ PHÍ, KẾT QUẢ TỐT NHẤT)

[domcop.com](https://domcop.com) - $24/tháng, hủy anytime.

**Cách filter cho dự án này:**
1. Vào "Expiring Domains" hoặc "Expired Domains"
2. Filter: TLD = `.vn`
3. Filter: DA > 10, TF > 5
4. Xem cột "Referring Domains" - click để xem chi tiết
5. Tìm domain nào có referring domain là báo VN (vnexpress, tuoitre, cafef...)

**Tip DomCop:**
- Dùng cột "Anchor" để thấy anchor text - ưu tiên có "SMS", "tin nhắn", "marketing"
- Sort theo "Moz DA" descending
- Export CSV để phân tích offline

---

## Danh Sách Domain Candidate (Check Ngay)

Dán từng cái vào [matbao.net](https://www.matbao.net) hoặc [nhanhoa.com](https://nhanhoa.com) để check available:

```
guisms.vn
smsgiare.vn
smsnhanh.vn
smsplatform.vn
nhasms.vn
smsreseller.vn
smspro.com.vn
smslab.vn
smscloud.vn
smsexpress.vn
smsauto.vn
smspartner.vn
marketingsms.vn
dichvusms.vn
smsapi.com.vn
bulktextvn.vn
textvietnam.vn
tinchieu.vn
```

---

## Tiêu Chí Chọn Domain Tốt

| Tiêu chí | Mức tốt | Ghi chú |
|---|---|---|
| DR (Ahrefs) | >= 10 | Domain có authority |
| DA (Moz) | >= 15 | Chỉ số uy tín |
| TF (Majestic) | >= 8 | Trust flow |
| Báo VN đang link | >= 2 | Lý do chính lấy expired |
| Keyword trong tên | SMS / tin nhắn | SEO on-brand |
| TLD | .vn > .com > .net | .vn ưu tiên VN search |
| Tuổi domain | >= 2 năm | Domain già rank tốt hơn |

---

## Công Cụ Check Backlink Miễn Phí

| Công cụ | Link | Giới hạn |
|---|---|---|
| Ahrefs Free | [ahrefs.com/backlink-checker](https://ahrefs.com/backlink-checker) | 10 domain/ngày |
| Moz Link Explorer | [moz.com/link-explorer](https://moz.com/link-explorer) | 10 check/tháng |
| Majestic Free | [majestic.com](https://majestic.com) | Hạn chế |
| SEMrush Free | [semrush.com](https://semrush.com) | 10 check/ngày |

**Workflow nhanh:**
1. Moz check DA -> lọc DA > 15
2. Ahrefs check referring domains -> filter báo VN
3. Wayback Machine check xem domain cũ làm gì

---

## Báo Việt Nam Có Giá Trị SEO Cao Nhất

Ưu tiên tìm backlink từ:

1. **vnexpress.net** - DR 82, traffic lớn nhất
2. **tuoitre.vn** - DR 79
3. **thanhnien.vn** - DR 75
4. **cafebiz.vn** - DR 72, chuyên business
5. **cafef.vn** - DR 70, chuyên tài chính
6. **dantri.com.vn** - DR 74
7. **ictnews.vn** - DR 58, chuyên tech/telecom (PERFECT cho SMS)
8. **genk.vn** - DR 60, tech
9. **baomoi.com** - DR 65, aggregator
10. **vneconomy.vn** - DR 64, B2B

---

## Quy Trình Recommended (Ít Vốn Nhất)

```
Week 1: Check domain candidate list -> đăng ký cái tốt nhất available
         Budget: ~230k VND (domain .vn/năm)

Week 2: Dựng website cơ bản (landing page)
         Nội dung: dịch vụ, giá, liên hệ

Week 3: Mua 3 backlink báo (cafebiz + ictnews + baomoi)
         Budget: ~1.5-3 triệu VND
         Nội dung bài: "Dịch vụ SMS Marketing cho SME Việt Nam"

Week 4+: Content SEO, blog, so sánh provider
```

Tổng chi phí ban đầu: ~2-4 triệu VND
