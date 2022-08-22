# Access control (Kiểm soát truy cập & leo thang đặc quyền)

## Kiểm soát truy cập là gì? (Access control)

> `Access Control` (authenrization) là việc áp dụng ràng buộc với ai hoặc cái gì có thể thực hiện các hành động cố gắng hoặc truy xuất tài nguyên.
>
> - `Autherization` người dùng và confirm chính là họ
> - `Session management` xác định các yêu cầu `HTTP` nào đang được thực hiện
> - `Access control` xác định người dùng xem có được quyền truy cập

> `Broken access control` là 1 vul thường gặp và nghiêm trọng. Thiết kế và quản lí `access control` là 1 vấn đề phức tạp

> Từ góc độ người dùng `access control` được chia thành:
>
> - Kiểm soát truy cập dọc (Vertical access control)
> - Kiểm soát truy cập ngang (Horizontal access control)
> - Kiểm soát truy cập phụ thuộc vào ngữ cảnh (Context-depement access control)

### Vertical access controls

> Là cơ chế hạn chế truy cập vào function sensitive không có sẵn cho người dùng.
>
> Với `Vertical access control`, user khác nhau có quyền truy cập vào các function ứng dụng khác nhau
>
> Ví dụ: qtv có thể sửa, xóa bất kì tài khoản của user nào, trong khi user bình thường không có các chức năng này

### Horizontal access controls

> Là cơ chế hạn chế truy cập vào tài nguyên đối với user được phép truy cập vào tài nguyên đó
>
> User khác nhau được phép truy cập vào tập hợp con các tài nguyên cùng loại
>
> Ví dụ:

### Context-dependent access controls

> Hạn chế quyền truy cập vào function, tài nguyên dựa trên trạng thái của ứng dụng hoặc tương tác của user với nó
>
> Ngăn chặn người dùng thực hiện hành động không đúng thứ tự
>
> Ví dụ:
> web bán lẻ ngăn người dùng sửa đổi nội dung trong giỏ hàng sau khi họ đã thanh toán

## Examples of broken access controls

### Vertical privilege escalation

> Nếu người dùng có thể truy cập vào các chức năng không được phép, đó là sự leo thang độc quyền

#### Unprotected functionality

> Cơ bản, sự leo thang độc quyền theo chiều dọc phát sinh khi ứng dụng không thực thi bất kì biện pháp bảo vệ nào đối với các chức năng nhạy cảm
>
> Ví dụ: Chức năng quản trị viên được liên kết từ trang chào mừng của quản trị viên nhưng không được liên kết với trang của user. User có thể vào thẳng path `/admin`:
>
> ```
> https://insecure-website.com/admin
> ```

#### Lab: Unprotected admin functionality

> Des: Lab chứa `admin panel` nhưng không được bảo vệ, xóa người dùng `carlos`

> Vào path với file `robots.txt`:
> ![img](../asset/access-control-1-Unprotected-admin-functionality-0.png)

> Làm theo nó:
> ![img](../asset/access-control-1-Unprotected-admin-functionality-1.png) ![img](../asset/access-control-1-Unprotected-admin-functionality-2.png)

---

> Một số trường hợp, chức năng nhạy cảm không được bảo vệ mạnh mẽ mà được che dấu bằng cách cung cấp cho nó 1 URL ít được dự đoán.
>
> Ví dụ:
>
> ```
> https://insecure-website.com/administrator-panel-yb556
> ```

> Attacker không thể đoán được trực tiếp điều này. Tuy nhiên ứng dụng vẫn có thể làm rò rỉ URL cho user.
>
> Ví dụ có thể tiết lộ tỏng JS tạo giao diện người dùng dựa trên vai trò của người dùng

> ```
> <script>
> var isAdmin = false;
> if (isAdmin) {
> 	...
> 	var adminPanelTag = document.createElement('a');
> 	adminPanelTag.setAttribute('https://insecure-website.com/administrator-panel-yb556');
> 	adminPanelTag.innerText = 'Admin panel';
> 	...
> }
> </script>
> ```

> Tệp lệnh này thêm liên kết giao diện người dùng nếu họ là admin. Tuy nhiên tập lệnh chứa URL hiển thị tất cả người dùng bất kể vai trò của họ

#### Lab: Unprotected admin functionality with unpredictable URL

> Des: `admin panel` không được bảo vệ. Nó nằm ở vị trí không thể đoán nhưng vị trí được tiết lộ ở đâu đó trong app. Xóa carlos

> path được dấu tại trang chủ, `view source` là thấy `script`:
> ![img](../asset/access-control-2-Unprotected-admin--functionality-with-unpredictable-URL-0.png) ![img](../asset/access-control-2-Unprotected-admin--functionality-with-unpredictable-URL-1.png) ![img](../asset/access-control-2-Unprotected-admin--functionality-with-unpredictable-URL-2.png)

---

#### Parameter-based access control methods

> Một số ứng dụng xác định ủy quyền truy cập hoặc vai trò của user khi login, sau đó lưu trữ thông tin này ở vị trí user có thể kiểm soát.
>
> Chẳng hạn như hidden field, cookie, tham số
>
> Ví dụ:
>
> ```
> https://insecure-website.com/login/home.jsp?admin=true
> https://insecure-website.com/login/home.jsp?role=1
> ```

> Như này là k an toàn, có thể sửa giá trị

#### Lab: User role controlled by request parameter

> Des: Chứa admin panel `/admin`. Bảng này xác định admin sử dụng cookie. Xóa carlos
>
> Dùng tài khoản: `wiener:peter`

> Đăng nhập tài khoản đã cho rồi chỉnh sửa cookie -> true:
> ![img](../asset/access-control-3-User-role-controlled-by-request-parameter-0.png) ![img](../asset/access-control-3-User-role-controlled-by-request-parameter-1.png)

---

#### Lab: User role can be modified in user profile

> Des: Chứa admin panel `/admin`. Sửa vai trò với user là 2.
>
> Đăng nhập với tài khoản `wiener:peter`

> Dùng tài khoản đã cho vào thay đổi email:
> ![img](../asset/access-control-4-User-role-can-be-modified-in-user-profile-0.png)

> `roleid`=1 thì không thấy gì, đổi sang 2 thì về lại web thì solve được
> ![img](../asset/access-control-4-User-role-can-be-modified-in-user-profile-1.png) ![img](../asset/access-control-4-User-role-can-be-modified-in-user-profile-3.png)
