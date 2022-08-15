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

> Cuộc tấn công SSRF chống lại server, attacker có thể khiến ứng dụng thực hiện yêu cầu quay lại máy chủ đang lưu trữ ứng dụng thông qua loopback network interface
>
> Ví dụ:
> Xem 1 ứng dụng shopping mua sắm liệu người dùng có được xem một mặt hàng có trong kho cụ thể hay không?
>
> Để cung cấp thông tin về kho, ứng dụng cần truy vấn REST API Back-end khác nhau, phụ thuộc vào sản phẩm và cửa hàng
>
> Vì vậy khi user xem trạng thái còn hàng của một mặt hàng sẽ truy vấn như sau:
>
> ```
> POST /product/stock HTTP/1.0
> Content-Type: application/x-www-form-urlencoded
> Content-Length: 118
>
> stockApi=http://stock.weliketoshop.net:8080/product/stock/check%3FproductId%3D6%26storeId%3D1
> ```
>
> Điều này khiến máy chủ yêu cầu thực hiện yêu cầu đến URL được chỉ định, truy xuất trạng thái của sản phẩm
>
> Trong trường hợp này, attacker có thể chỉnh sửa URL
>
> ```
> POST /product/stock HTTP/1.0
> Content-Type: application/x-www-form-urlencoded
> Content-Length: 118
>
> stockApi=http://localhost/admin
> ```
>
> Ở đây thì server sẽ tìm và trả về content của `/admin` của URL

#### Lab: Basic SSRF against the local server (SSRF cơ bản)

> Des: Lab này chứa tính năng kiểm tra data, lấy dữ liệu từ hệ thống nội bộ
> Mục tiêu: Thay đổi URL kiểm tra data để access vào admin interface tại `http://localhost/admin` và delete user `carlos`

**Giao diện ban đầu**
![img](../asset/ssrf-1-basic-ssrf-against-the-local-server-0.png)

> Để check sản phẩm thì `checkstock`:
> ![img](../asset/ssrf-1-basic-ssrf-against-the-local-server-1.png)

> Dùng burp để chặn request và sửa `stockUrl` của đề
> ![img](../asset/ssrf-1-basic-ssrf-against-the-local-server-2.png)

> Send to repeater, sửa `stockApi` là `http://localhost/admin`:
> ![img](../asset/ssrf-1-basic-ssrf-against-the-local-server-3.png)

> Server sẽ trả về:
> ![img](../asset/ssrf-1-basic-ssrf-against-the-local-server-4.png)

> Sửa theo nó:
> ![img](../asset/ssrf-1-basic-ssrf-against-the-local-server-5.png)

> Done:
> ![img](../asset/ssrf-1-basic-ssrf-against-the-local-server-6.png) ![img](../asset/ssrf-1-basic-ssrf-against-the-local-server-7.png)

### SSRF attacks against other back-end systems (SSRF chống lại hệ thống backend)

> Các trust relationship thường được phát sinh với giả mạo từ phía server là nới server app có thể tương tác với các hệ thống backend khác mà user không được quyền truy cập trực tiếp
>
> Các hệ thống này thường có địa chỉ IP riêng không được định tuyến.
>
> Ở ví dụ trước, giả sử giao diện quản trị tại URL backend: `http://192.168.0.68/admin` thì attacker có thể khai thác SSRF để exploit:
>
> ```
> POST /product/stock HTTP/1.0
> Content-Type: application/x-www-form-urlencoded
> Content-Length: 118
>
> stockApi=http://192.168.0.68/admin
> ```

#### Lab: Basic SSRF against another back-end system

> Des: Lab này có tình năng kiểm tra sản phẩm xem có còn hay không, để solve thì quét tại IP `192.168.0.x` với path là `/admin`

**Giao diện ban đầu**
![img](../asset/ssrf-2-Basic-SSRF-against-another-back-end-system-0.png)

> Dùng Burp Suite để chặn, bắt request:
> ![img](../asset/ssrf-2-Basic-SSRF-against-another-back-end-system-1.png)

> Send nó qua Intruder và chỉnh payload:
> ![img](../asset/ssrf-2-Basic-SSRF-against-another-back-end-system-2.png)

> ![img](../asset/ssrf-2-Basic-SSRF-against-another-back-end-system-3.png)

> Sau đó attack và thấy Status là `200` thì lấy nó, chứng tỏ IP đó đúng:
> ![img](../asset/ssrf-2-Basic-SSRF-against-another-back-end-system-4.png)

> DONE:
> ![img](../asset/ssrf-2-Basic-SSRF-against-another-back-end-system-5.png) ![img](../asset/ssrf-2-Basic-SSRF-against-another-back-end-system-6.png)
