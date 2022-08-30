# Information disclosure vulnerabilities

## Khái niệm

> Information disclosure, hay được gọi là rò rỉ thông tin là khi web vô tình để lộ thông tin nhạy cảm cho người dùng.
>
> - Dữ liệu về ng dùng khác
> - Dữ liệu thông tin kinh doanh, thương mại
> - Chi tiết về trang web, cơ sở hạ tầng

## Ví dụ về infomation desclosure

> - Tiết lộ các hidden folder, constructure, content thông qua `robots.txt`
> - Cung cập access vào source code thông qua các bản backups tạm thời
> - Đề cập rõ ràng về bảng db, cột trong thông báo errors
> - Khóa API, IP, infor đăng nhập CSDL trong source code

## Tìm và khai thác lỗ hổng

> Một số kỹ thuật, tools để xác định `information disclosure`

### How to test for information disclosure vulnerabilities (Kiểm tra lỗ hổng)

> Một số kỹ thuật và tools cao cấp mà có thể sử dụng để xác định vul:
>
> - Fuzzing
> - Burp scanner
> - Burp engagement tool
> - Engineering information responses

#### Fuzzing

> Nếu xác định đượck param. có thể sử dụng các data type không mong muốn vào các `fuzz strings` được chế tạo đặc biệt để xem có tác dụng gì.
>
> Sử dụng automate bằng các công cụ như `Burp Intruder`:
>
> - `add payload` vào các param và sử dụng các wordlist để kiểm tra các input khác nhau liên tiếp
> - Dễ dàng xác định sự diff bằng các xem `HTTP status code, response time, length`
> - Sử dụng grep matching rules để nhanh chóng xác định các lần xuất hiện của keyword, ví dụ như: `error, invalid, SELECT, ....`
> - Áp dụng các quy tắc grep và so sánh content của các item trong các response

> Cũng có thể dùng extension `Logger++`. Ngoài việc ghi lại log request và responses từ tất cả các tool của burp, nó cho phép xác định các filter nâng cao để làm nổi bật các mục

#### Using Burp Scanner

> Cung cấp tính năng quét trực tiếp để kiểm tra các mục
>
> Ví dụ: Sẽ cảnh báo nếu nó tìm thấy các info nhạy cảm như email credit, .... trong responses

#### Using Burp's engagement tools

#### Common sources of information disclosure

##### Files for web crawlers

> Nhiều web cung cấp file /robots.txt và /sitemap.xml để giúp tiến trình thu thập thông tin điều hướng trang web của họ

##### Directory listings

##### Developer comments

##### Error messages

#### Lab: Information disclosure in error messages

> Thông báo lỗi error message reveal tiết lộ ver của third-party framework. Lấy ver của nó rồi submit

> ![img](../asset/information-disclosure-1-Information-disclosure-in-error-messages-0.png) ![img](../asset/information-disclosure-1-Information-disclosure-in-error-messages-1.png)
