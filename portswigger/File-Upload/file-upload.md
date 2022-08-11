# Lỗ hổng File Upload

## Khái niệm

> File upload là khi web server cho phép user upload file mà lên hệ thống mà không có cơ chế xác minh đầy đủ ví dụ như filename, type, size, ...
> Ví dụ như một chức năng tải ảnh lên server mà không có xác minh đầy đủ hoặc xác minh sai thì các hacker có thể tải lên những tệp độc hại, nguy hiểm.
> Điều này có thể dẫn tới server có thể bị lỗi RCE.

## Tác hại

> Khi file đã được upload lên hệ thống (ví dụ như các file .php, .jsp, ...) được thực thi dưới dạng mã, hacker sẽ có chức năng như web shell, và có toàn quyền trên hệ
> thống.
> Nếu tệp không được xác thực đúng cách, trùng tên file trong hệ thống. Điều này có thể khiến các file trong hệ thống bị ghi đè.
> Không đảm bảo được size của file, điều này sẽ dẫn tới cuộc tấn công từ chối dịch vụ ví dụ như DoS (attacker sẽ lấp đầy dung lượng đĩa có sẵn).

<p><red>123</red>
