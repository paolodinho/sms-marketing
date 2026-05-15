# Bộ nhận diện thương hiệu — dichvusmsvn.com
Xây dựng: 15/05/2026 | Phiên bản: 1.0

---

## 1. Tổng quan thương hiệu

| | |
|---|---|
| **Tên thương hiệu** | SMS VN (viết tắt gọn) / DichVuSMS.VN (đầy đủ) |
| **Domain** | dichvusmsvn.com |
| **Thương hiệu mẹ** | Digicom — digicomvn.com |
| **Tagline đề xuất** | *"Nhắn tin marketing — đơn giản như nhắn tin thường"* |
| **Sub-tagline** | Powered by Digicom |
| **Định vị** | Dịch vụ SMS Brandname + Zalo ZNS + OTP giá minh bạch, dễ bắt đầu cho SME Việt Nam |

---

## 2. Màu sắc

### Triết lý màu
Kế thừa DNA màu từ Digicom nhưng **đảo trọng tâm**: dùng **teal `#00B39C` làm màu chính** thay vì navy — tạo ra sự khác biệt rõ trong thị trường SMS (đối thủ đều dùng blue), đồng thời vẫn giữ kết nối thị giác với thương hiệu mẹ qua bảng màu chung.

### Bảng màu chính

| Tên | Hex | RGB | Dùng cho |
|---|---|---|---|
| **SMS Teal** (primary) | `#00B39C` | 0, 179, 156 | CTA, button, accent, icon, highlight |
| **Digicom Navy** (secondary) | `#004DD8` | 0, 77, 216 | Header, heading lớn, link, trust signal |
| **Dark Text** | `#0A1628` | 10, 22, 40 | Body text, footer background |
| **Light Background** | `#F0FBF9` | 240, 251, 249 | Section background teal-tinted |
| **White** | `#FFFFFF` | 255, 255, 255 | Nền chính, card |
| **Gray Mid** | `#6B7A8D` | 107, 122, 141 | Sub-text, caption, placeholder |
| **Gray Light** | `#E8EDF3` | 232, 237, 243 | Border, divider, input background |

### Màu trạng thái (UI)

| Tên | Hex | Dùng cho |
|---|---|---|
| Success | `#00B39C` | (reuse teal) Gửi thành công, tích xanh |
| Warning | `#F59E0B` | Cảnh báo số dư thấp |
| Error | `#EF4444` | Lỗi API, tin bị từ chối |
| Info | `#004DD8` | (reuse navy) Thông báo thông thường |

### Quan hệ màu với Digicom

```
Digicom (mẹ)          dichvusmsvn.com (con)
────────────────      ─────────────────────
#004DD8 (primary)  →  #004DD8 (secondary)     [giữ nguyên, hạ cấp]
#00B39C (accent)   →  #00B39C (PRIMARY)        [đẩy lên chính]
```

> Cách nhận ra ngay: website nào teal nổi bật = sản phẩm SMS VN của Digicom.

---

## 3. Typography

### Font chính: **Be Vietnam Pro**
- Google Fonts: https://fonts.google.com/specimen/Be+Vietnam+Pro
- Lý do: tối ưu tiếng Việt, dấu chữ rõ ràng, modern sans-serif, miễn phí
- Được dùng bởi nhiều brand tech Việt Nam

### Thang cỡ chữ (Type Scale)

| Vai trò | Size | Weight | Dùng cho |
|---|---|---|---|
| Hero Heading | 48–56px | 700 Bold | H1 trang chủ |
| Section Heading | 32–36px | 700 Bold | H2 các section |
| Sub-heading | 22–24px | 600 SemiBold | H3, card title |
| Body Large | 18px | 400 Regular | Lead paragraph |
| Body | 16px | 400 Regular | Nội dung chính |
| Body Small | 14px | 400 Regular | Caption, note |
| Label / Tag | 12px | 600 SemiBold + UPPERCASE | Badge, tag, label |

### Font dự phòng (nếu không load được)
```css
font-family: 'Be Vietnam Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

---

## 4. Logo

### Concept logo (brief cho designer)

**Hướng 1 — Wordmark + icon (khuyến nghị)**
- Icon: hình sóng/signal 3 vạch (≈ biểu tượng SMS/wifi) màu teal `#00B39C`
- Wordmark: "SMS VN" — font Be Vietnam Pro Bold
- "SMS" màu navy `#004DD8`, "VN" màu teal `#00B39C`
- Layout ngang (horizontal) — tương tự logo Digicom (160×45px)

**Hướng 2 — Monogram**
- Chữ "S" cách điệu (SMS) kết hợp hình bong bóng chat
- Màu gradient: `#004DD8` → `#00B39C` (trái sang phải)

### Các biến thể cần có

| Biến thể | Nền | Dùng cho |
|---|---|---|
| Ngang đầy đủ (primary) | Trắng | Header website, tài liệu |
| Ngang đầy đủ (reversed) | Navy `#004DD8` | Email header, dark bg |
| Icon vuông (favicon) | Teal `#00B39C` | Favicon, app icon, avatar |
| Icon vuông (reversed) | Trắng | Dark mode |

### Vùng bảo vệ (Clear space)
Tối thiểu 16px xung quanh logo. Không đặt text hay element khác vào vùng này.

---

## 5. Tone of voice

### Kế thừa từ Digicom
- Chuyên nghiệp, kết quả cụ thể, đáng tin cậy
- Nói ngắn gọn, dùng số liệu thực

### Điều chỉnh cho SMS VN (phù hợp SME)
- **Dễ hiểu**: Tránh jargon kỹ thuật (không viết "API gateway", viết "kết nối hệ thống")
- **Thực tế**: Nói lợi ích, không nói tính năng ("khách nhận được tin trong 5 giây" thay vì "độ trễ <5s")
- **Gần gũi nhưng không suồng sã**: xưng "chúng tôi / bạn", không dùng "tụi mình / bạn ơi"
- **Minh bạch về giá**: Luôn có bảng giá rõ ràng, không "liên hệ để báo giá" với gói nhỏ

### Ví dụ tone

| ❌ Tránh | ✅ Dùng |
|---|---|
| "Giải pháp SMS marketing toàn diện hàng đầu" | "Gửi tin nhắn thương hiệu đến khách hàng — từ 490đ/tin" |
| "Hệ sinh thái omnichannel tiên tiến" | "SMS + Zalo ZNS + OTP — quản lý trong 1 nơi" |
| "Liên hệ để được tư vấn giá tốt nhất" | "Xem bảng giá ngay — không cần đăng ký" |
| "Chúng tôi cam kết uptime 99.9%" | "Hệ thống hoạt động 24/7, nếu có sự cố — phản hồi trong 30 phút" |

---

## 6. Quan hệ thương hiệu mẹ — con

### Nguyên tắc
- dichvusmsvn.com **là sản phẩm của Digicom**, không phải công ty độc lập
- Ghi "Powered by Digicom" ở footer (nhỏ, không chiếm không gian)
- Không dùng logo Digicom trên trang chính — chỉ mention bằng text link

### Điểm kết nối thị giác
1. **Màu navy `#004DD8`** — giống hệt Digicom primary
2. **Màu teal `#00B39C`** — giống hệt Digicom accent, chỉ đổi vai trò
3. **Font Be Vietnam Pro** — nếu Digicom cũng dùng (hoặc dùng font tương đương)
4. **Phong cách thiết kế** — clean, white space, professional

### Người dùng nhìn vào sẽ cảm nhận
> "Đây là dịch vụ chuyên biệt của một agency uy tín, không phải startup vô danh."

---

## 7. Ứng dụng thực tế

### Website
- Header: nền trắng, logo trái, nav phải, CTA button teal
- Hero: nền `#F0FBF9` (teal-tinted), heading navy, button teal
- Sections xen kẽ: trắng ↔ `#F0FBF9`
- Footer: nền `#0A1628` (dark), text trắng, "Powered by Digicom" cuối trang

### Email / Zalo OA
- Header email: nền navy `#004DD8`, logo reversed (trắng)
- CTA button: teal `#00B39C`

### Tài liệu báo giá / PDF
- Cover: navy + teal gradient
- Bảng giá: nền trắng, header bảng teal, text dark

---

## 8. Checklist hoàn thiện bộ nhận diện

- [ ] Thiết kế logo (thuê designer hoặc dùng AI tool) theo brief mục 4
- [ ] Export logo: SVG + PNG (transparent) + PNG (dark bg)
- [ ] Tạo favicon 32×32px và 180×180px (Apple touch icon)
- [ ] Tạo OG Image mặc định 1200×630px (cho social share)
- [ ] Thiết lập Google Fonts embed code cho website
- [ ] Tạo Figma/Canva template cơ bản (trang báo giá, banner quảng cáo)
