# Directory traversal

---

## Khái niệm

> Directory traversal (Truyền tài đường dẫn tệp): Là vul cho attacker tấn công và đọc các file tùy ý trên server đang sử dụng

> Có thể là code, data, thông tin xác thực và các file

> Một số trường hợp attacker có thể ghi vào các file tùy ý trên máy chủ, sửa đổi info và hành vi của app và cuối cùng là toàn quyền kiểm soát server

---

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

---

## Common obstacles to exploiting file path traversal vulnerabilities

> Nhiều ứng dụng đặt input của user nhập vào đường dẫn tệp, điều đó thực hiện một số loại defen `directory traversal` nhưng nó vẫn có thể bị bypass

> Nếu ứng dụng tách hoặc chặn folder từ file tải lên do user cung cấp thì có thể pass qua bằng nhiều tech.

> Có thể sử dụng path tuyệt đối từ folder root của hệ thống chẳng hạn như `filename=/etc/passwd` để có thể tham chiếu đến trực tiếp mà không cần qua sử dụng bất kì sự truyền tải nào

### Lab: File path traversal, traversal sequences blocked with absolute path bypass

> Des: Lab này chứ vul `directory traversal`

> Lab chặn các trình tự truyền tải coi như filename được cung cấp có các liên quan đến folder làm việc mặc định.

> Để solve thì truy xuất content của `/etc/passwd`

> Bài này chỉ cần đổi `filename=/etc/passwd` > ![img](../asset/Directory-traversal-1-File-path-traversal-traversal-sequences-blocked-with-absolutepath-bypass-0.png)

---

> Nếu các trình duyệt không nhận thì có thể thay đổi kí tự:
>
> ```
> .....// or ....\/
> ```

### Lab: File path traversal, traversal sequences stripped non-recursively

> Des:Lab này chứ vul `directory traversal`

> Ứng dụng tách các trình tự truyền tải đường dẫn khỏi tên tệp do người dùng cung cấp trước khi sử dụng.

> Để solve thì truy xuất content của `/etc/passwd`

> Bài này chỉ cần đổi `filename=....//....//....//etc/passwd` > ![img](../asset/Directory-traversal-2-File-path-traversal-traversal-sequences-stripped-non-recursively-0.png)

---

> Trong một vài ngữ cảnh, chẳng hạn URL path hoặc param của request là `multipart/form-data`. Server có thể tách bất kì thư mục của input

> Đôi khi có thể bỏ qua nó bằng cách `URL encode` or `Double URL encoding`.

> `../` sẽ thành `%2e%2e%2f` or `%252e%252e%252f`

> Với người dùng burp pro, `Burp Intruder` có cung cấp các list payload (Fuzzing - path traversal) chứa nhiều trình tự trình duyệt khác nhau.

---

### Lab: File path traversal, traversal sequences stripped with superfluous URL-decode

> Des:Lab này chứ vul `directory traversal`
>
> Ứng dụng chặn input, sau đó thực hiện giải mã URL encode.
>
> Để solve thì hãy truy cập vào `etc/passwd`

> Bài này nó 2 lần URL encode nên ta 2 lần encode `../../../` sẽ exploit được:
> ![img](../asset/Directory-traversal-3-File-path-traversal-traversal-sequences-stripped-with-superfluous-URL-decode-1.png) ![img](../asset/Directory-traversal-3-File-path-traversal-traversal-sequences-stripped-with-superfluous-URL-decode-2.png) ![img](../asset/Directory-traversal-3-File-path-traversal-traversal-sequences-stripped-with-superfluous-URL-decode-0.png)

---

> Nếu một ứng dụng yêu cầu filename do người dùng cung cấp phải bắt đầu từ folder cơ sở. chẳng hạn như `/var/www/images`, thì có thể bao gồm folder base theo sau:
>
> ```
> filename=/var/www/images/../../../etc/passwd
> ```

### Lab: File path traversal, validation of start of path

> Des:Lab này chứ vul `directory traversal`

> Ứng dụng truyền đường dẫn filename đầy đủ thông tin tham gia yêu cầu và xác nhận rằng đường dẫn được cung cấp bắt đầu với thư mục mong đợi

> Dùng burp chặn request thì ta thấy:
> ![img](../asset/Directory-traversal-4-File-path-traversal-validation-of-start-of-ath-0.png)

> Sửa, ta phải thoát khỏ 3 thư mục đầu:
> ![img](../asset/Directory-traversal-4-File-path-traversal-validation-of-start-of-ath-1.png)

---

> Nếu ứng dụng yêu cầu tên tệp do người dùng input phải kết thúc bằng extension file dự kiến, chẳng hạn như `null byte`:
>
> ```
> filename=../../../etc/passwd%00.png
> ```

### Lab: File path traversal, validation of file extension with null byte bypass

> Des:Lab này chứ vul `directory traversal`

> Ứng dụng xác nhận filename được cung cấp của user bằng kết thúc của file mở rộng.

> Để sovle thì hãy truy xuất content của `/etc/passwd`

> Bài này dùng null byte:
> ![img](../asset/Directory-traversal-5-File-path-traversal-validation-of-file-extension-with-null-byte-bypass-0.png) ![img](../asset/Directory-traversal-5-File-path-traversal-validation-of-file-extension-with-null-byte-bypass-1.png)

## Cách phòng chống

> Cách hiệu quả để ngăn chặn `directory traversal` là tránh hoàn toàn input do user nhập vào với các API hệ thống.
>
> - So sánh với whitelist
