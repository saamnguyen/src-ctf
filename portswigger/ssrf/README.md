# Lỗ hổng SSRF (Server-side request forgery) - Giả mạo yêu cầu phía máy chủ

## Khái niệm

> SSRF là một vul web cho phép attacker tấn công khiến server thực hiện yêu cầu tới một vị trí không mong muốn
>
> Cuộc tấn công SSRF điển hình, attacker khiến máy chủ tạo kết nối với hệ thống, cơ sở hạ tầng (trong hoặc ngoài tùy ý), có khả năng rò rỉ dữ liệu

---

## Tác hại

> Cuộc attack SSRF thành công thường dẫn tới hành động truy cập trái phép vào dữ liệu, ứng dụng dễ bị attack nhất là phần `backend`
>
> Một số cuộc attack SSRF có thể cho phép kẻ attacker thực hiện lệnh tùy ý
>
> Cuộc tấn công SSRF kết nối với hệ thống thứ 3 bên ngoài dẫn tới các cuộc attack nguy hiểm bắt nguồn từ tổ chức lưu trữ ứng dụng

---

## Cuộc attack SSRF phổ biến

> Các cuộc attack SSRF thường khai thác các mối tin cậy (relationships) để leo thang đặc quyền

---

### SSRF attacks against the server itself (SSRF chống lại server)
