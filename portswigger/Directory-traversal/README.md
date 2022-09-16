# Directory traversal

## Khái niệm

> Directory traversal (Truyền tài đường dẫn tệp): Là vul cho attacker tấn công và đọc các file tùy ý trên server đang sử dụng

> Có thể là code, data, thông tin xác thực và các file

> Một số trường hợp attacker có thể ghi vào các file tùy ý trên máy chủ, sửa đổi info và hành vi của app và cuối cùng là toàn quyền kiểm soát server

## Reading arbitrary files via directory traversal

> Xem ứng dụng hiển thi hình ảnh được bán qua URL sau:
>
> ```
> <img src="/loadImage?filename=218.png">
> ```

> `loadImage` URL nhận tham số là tên file và sẽ trả về file cụ thể.Bản thân các file ảnh sẽ được lưu trữ tại `/var/www/imags`.

> Trong trường hợp này thì `API` sẽ lấy từ:
>
> ```
> /var/www/images/image.png
> ```

> Nếu app không có bất kì biện pháp bảo vệ `directory traversal` thì attacker có thể tấn công theo URL sau:
>
> ```
> https://insecure-website.com/loadImage?filename=../../../etc/passwd
> ```

> Điều này sẽ khiến ứng dụng đọc:
>
> ```
> /var/www/images/../../../etc/passwd
> ```

### Lab: File path traversal, simple case

> Des: Lab này chứa vul `Directory traversal` tại images

> Để solve thì truy cập content của path : `/etc/passwd`

> Bài này chỉ cần đổi path tại path: `/image?filename=../../../etc/passwd`:
> ![img](../asset/Directory-traversal-0-Filepath-traversal-simple-case-0.png)
