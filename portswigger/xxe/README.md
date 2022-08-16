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
