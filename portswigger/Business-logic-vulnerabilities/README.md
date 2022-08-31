# Business logic vulnerabilities

## Khái niệm

> Phát sinh do những sai lầm từ user
> ![img](../asset/Business-logic-vulnerabilities.jpg)

## What are business logic vul?

> Là những vul trong design và implement của 1 app cho phép attacker gây ra các behavior ngoài ý muốn.
>
> Logic flaws thường không thể thấy đối với những người không tìm kiếm một các rõ ràng vì chúng không thể bị lộ khi sử dụng app bình thường

> Ví dụ:
> hoàn thành 1 đơn hàng giao dịch mà không cần thông qua quy trình mua hàng

## Phát sinh như nào?

> Phát sinh cho đội ngũ design, implement đưa ra các giả định sai về cách user tương tác với app. Giả định này sẽ không tốt dẫn đến xác nhận không đầy đủ info từ user.

## Tác động

> Khá nhỏ

## Ví dụ

### Excessive trust in client-side controls (Tin tưởng quá mức vào các kiểm soát phía máy khách)

> Giả định cơ bản, người dùng tương tác qua giao diện trang web. Nó vẫn nguy hiểm vì có thể dùng các tool như `burp proxy` để chặn và sửa request

#### Lab: Excessive trust in client-side controls

> Des:Lab không xác thực đầy đủ data từ user. Exploit và có thể mua hàng với giá không mong muốn. Để solve thì mua `Lightweight l33t leather jacket`
>
> Đăng nhập bằng `wiener:peter`

> Bài này chỉ cần dùng burp để chặn và sửa giá + id của sản phẩm:
> ![img](../asset/Business-logic-vulnerabilities-0-Excessive%20trust-in-client-side-controls-0.jpg) ![img](../asset/Business-logic-vulnerabilities-0-Excessive%20trust-in-client-side-controls-1.png.jpg) ![img](../asset/Business-logic-vulnerabilities-0-Excessive%20trust-in-client-side-controls-2.jpg) ![img](../asset/Business-logic-vulnerabilities-0-Excessive%20trust-in-client-side-controls-3.jpg) ![img](../asset/Business-logic-vulnerabilities-0-Excessive%20trust-in-client-side-controls-4.jpg)
