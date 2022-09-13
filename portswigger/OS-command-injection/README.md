# OS command injection

## Khái niệm

> ![img](../asset/os-command-injection-0.png)

## OS command injection là gì?

> OS command injection (hay còn được gọi là shell injection) là 1 vul web cho phép attacker thực thi command trên OS (HĐH) tùy ý trên server và xâm phạm, lấy cắp data.

> Thông thường attacker có thể lợi dụng vul để xâm phạm các thành phần khác, khai thác các mối quan hệ

## Executing arbitrary commands

> Xem xét ứng dụng shopping sau để xem mặt hàng có còn trog shop hay không:
>
> ```
> https://insecure-website.com/stockStatus?productID=381&storeID=29
> ```

> Để cung cấp thông tin mặt hàng, app phải query các system kế thừa nhau. Các chức năng có thể gọi bằng shell:
>
> ```
> stockreport.pl 381 29
> ```

> Vì app không triển khai các biện pháp bảo vệ nên có thể đưa shell vào OS:
>
> ```
> & echo aiwefwlguh &
> ```

> Nó sẽ execute:
>
> ```
> stockreport.pl & echo aiwefwlguh & 29
> ```

> `echo` chỉ là lệnh in cơ bản, đây là cách hữu ích để thử exploit. `&` để phân tách chuỗi trong shell. Kết quả:
>
> ```
> Error - productID was not provided
> aiwefwlguh
> 29: command not found
> ```

> 3 Dòng đầu chứng minh rằng:
>
> `stockreport.pl` không được thực thi là do thiếu đối số
>
> `echo` vẫn được execute
>
> `29` nó là không phải command

### Lab: OS command injection, simple case

> Des: Lab này chứa vul OS command injection trong check sản phẩm. Ứng dụng thực thi một lệnh shell với id của sản phẩm. Để solve hãy thực hiện lệnh `whoami` tại người dùng hiện tại

> Bài này chỉ cần vào check stock rổi thay đổi param thêm `|whoami` là oke:
> ![img](../asset/os-command-injection-1-OS-command-injection-simple-case-0.png)
