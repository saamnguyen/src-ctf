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

---

#### Lab: 2FA broken logic

> Des: Xác thực 2 yếu tố của lab này dễ bị attack. Để solve, truy cập vào account carlos
>
> Đăng nhập bằng `wiener:peter`

> Bài này khi đăng nhập thì cần xác thực 2 lần, thứ nhất là passwd, thứ 2 là mã opt 4 kí tự:
> ![img](../asset/Business-logic-vulnerabilities-2-2FA-broken-logic-0.png) ![img](../asset/Business-logic-vulnerabilities-2-2FA-broken-logic-1.png)

> Để lấy mã thì cần với param `verify=user` ![img](../asset/Business-logic-vulnerabilities-2-2FA-broken-logic-2.png)

> Sau đó sẽ gửi về mail, để xác thực thì `POST` nó lên đường dẫn vừa `GET` mã:
> ![img](../asset/Business-logic-vulnerabilities-2-2FA-broken-logic-3.png)

> Giờ dùng `GET` để tạo 1 otp về user `carlos`:
> ![img](../asset/Business-logic-vulnerabilities-2-2FA-broken-logic-4png.png)

> Send `POST` qua intruder để brute force nó từ 1000 -> 9999, nó trả về `302` là oke. Copy tại `show response in broswer` :
> ![img](../asset/Business-logic-vulnerabilities-2-2FA-broken-logic-5.png) ![img](../asset/Business-logic-vulnerabilities-2-2FA-broken-logic-6.png) ![img](../asset/Business-logic-vulnerabilities-2-2FA-broken-logic-7.png) ![img](../asset/Business-logic-vulnerabilities-2-2FA-broken-logic-8.png)

---

### Failing to handle unconventional input (Xử lý input không bình thường)

> Mục đính của application login là hạn chế input cảu user đối với các giá trị tuân thủ của các quy tắc kinh doanh
>
> Ví dụ: Ứng dụng có thể được thiết kế để chấp thuận một kiểu data nhất định nhưng login này có được chấp thuận của business hay

> Ví dụ: Một cửa hàng trực tuyến, khi đặt mua sp, ng dùng chỉ định số lượng họ muốn đặt. Nhưng phải đặt với số lượng cho phép, không quá số lượng của sp

> Chức năng chuyển tiền, phải xem người gửi đủ tiền trước khi hoàn thành
>
> ```
> $transferAmount = $_POST['amount'];
> $currentBalance = $user->getBalance();
>
> if ($transferAmount <= $currentBalance) {
>    // Complete the transfer
> } else {
>    // Block the transfer: insufficient funds
> }
> ```

> Sử dụng burp suite để chặn và sửa request xem nó có điều gì xảy ra không:
>
> - Có giới hạn cho data?
> - điều gì xảy ra khi đạt tới limit
> - có bất kỳ chuyển đổi, chuẩn hóa nào đang thực hiện>

#### Lab: High-level logic vulnerability

> Des: Không xác thực đầy đủ thông tin user, exploit logic vul trong quy trình mua hàng để mua mặt hàng với giá không mong muôn `lightweight l33t leather jacket`
>
> Login `wiener:peter`

> Khi đặt sản phẩm thì lab cho `quantity` là số âm được. Giờ cần bằng sao cho sản phẩm phải bằng số tiền đã cho là 100$
> ![img](../asset/Business-logic-vulnerabilities-3-High-level-logic-vulnerability-0.png) ![img](../asset/Business-logic-vulnerabilities-3-High-level-logic-vulnerability-n.png) ![img](../asset/Business-logic-vulnerabilities-3-High-level-logic-vulnerability-n-0.png)

---

#### Lab: Low-level logic flaw

> Des: Không xác thực đầy đủ thông tin user, exploit logic vul trong quy trình mua hàng để mua mặt hàng với giá không mong muôn `lightweight l33t leather jacket`
>
> Login `wiener:peter`

> Bài này sử dụng burp intruder để brute force xem limit của lab là gì. Không được đặt quá `99` số lương trên 1 lần đặt
>
> Tổng đơn hàng là không được quá: `2,147,483,647`

> Đầu tiên send POST của đặt hàng qua intruder:
> ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-0.png)

> Để check xem max của đơn hàng là bao nhiêu, nó bị lỗi lúc số âm, lúc dương, sau đó remove hết đi exploit lại
> ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-1.png)

> ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-2.png) ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-3.png)

> Set payload như hình để attack:
> ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-4.png) ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-5.png) ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-7.png) ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-6.png)

> Sau đó gửi 47 cái jacket để giảm số âm cho đủ rồi mua thêm đồ để thành số dương cho đủ 100$
> ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-8.png) ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-n.png) ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-n-n.png) ![img](../asset/Business-logic-vulnerabilities-4-Low-level-logic-flaw-n-n-n.png)

---

#### Lab: Inconsistent handling of exceptional input

> Des: Không xác thực đầy đủ thông tin user. Lấy quyền admin và xóa user carlos

> ![img](../asset/Business-logic-vulnerabilities-5-Inconsistent-handling-of-exceptional-input-4.png)![img](../asset/Business-logic-vulnerabilities-5-Inconsistent-handling-of-exceptional-input-3.png)

> Bài này khi register xong cũng không thấy gì để exploit. Dùng burp để quét xem path `/admin`:
> ![img](../asset/Business-logic-vulnerabilities-5-Inconsistent-handling-of-exceptional-input-0.png) ![img](../asset/Business-logic-vulnerabilities-5-Inconsistent-handling-of-exceptional-input-1.png)

> Vào path `/admin` thì nó bắt là phải mang domamin `dontwannaycry.com` thì mới làm được quyền admin:
> ![img](../asset/Business-logic-vulnerabilities-5-Inconsistent-handling-of-exceptional-input-2.png)

> Thử register nhiều ký tự với email xem sao, nếu quá 256 thì nó sẽ bị cắt:
> ![img](../asset/Business-logic-vulnerabilities-5-Inconsistent-handling-of-exceptional-input-5.png)

> Nên để exploit thì sẽ đăng kí với email dài + `@dontwannacry.com` + `.email-id.web-security-academy.net` > ![img](../asset/Business-logic-vulnerabilities-5-Inconsistent-handling-of-exceptional-input-6.png)

> Do thừa nên đăng kí lại:
> ![img](../asset/Business-logic-vulnerabilities-5-Inconsistent-handling-of-exceptional-input-7.png)

> Done:
> ![img](../asset/Business-logic-vulnerabilities-5-Inconsistent-handling-of-exceptional-input-8.png)

---

### Making flawed assumptions about user behavior (Giả định sai làm về hành vi user)

#### Trusted users won't always remain trustworthy ( Người dùng nào không phải lúc nào cũng tin cậy)

> Khi đã pass qua các kiểm soát nghiêm ngặt rồi, dữ liệu của user được tin cậy vô thời hạn

#### Lab: Inconsistent security controls

> Lab này cho phép user access vào chức năng administrator dành cho nhân viên. Truy cập và xóa `carlos`

> Bài này là về tin tưởng vô thời hạn nên exploit như bài trước thì không được:
> ![img](../asset/Business-logic-vulnerabilities-6-Inconsistent-security-controls-0.png)

> Vì là không nên tin tưởng nên change email thành subdomain của công ty luôn xem sao mà lại solve được luôn =)):
> ![img](../asset/Business-logic-vulnerabilities-6-Inconsistent-security-controls-1.png)

---

#### Users won't always supply mandatory input (Người dùng không phải lúc nào cũng cung cấp thông tin đầu vào bắt buộc)

> Luôn cung cấp giá trị cho trường bắt buộc. user bình thường sẽ không thể gửi kèm các trường không bắt buộc, nhưng attacker thì khác, có thể giả mạo chúng

> Khi thăm dò lỗi logic, thử bỏ từng param và quan sát xem có ảnh hưởng gì tới response:
>
> - Chỉ xóa 1 param tại 1 time để đảm bảo được tất cả các path có liên quan
> - Xóa thử param + tham số. Máy chủ sẽ xem xét và xử lý 2 trường hợp
> - Thực hiện nhiều quá trình cho tới khi hoàn thành

> Áp dụng cho URL và POST, kiểm tra thêm cả cookie

#### Lab: Weak isolation on dual-use endpoint

> Des:Đưa ra 1 giả định sai lầm về đặc quyền của user dựa trên thông tin đầu vào của họ. exploit tính năng quản lý tài khoản để có quyền truy cập vào account của user. Xóa carlos. Login bằng `wiener:peter`

> Bài này thì đầu tiên thử quét các path xem sao:
> ![img](../asset/Business-logic-vulnerabilities-7-Weak-isolation-on-dual-use-endpoint-0.png)

> Thử đổi passwd:
> ![img](../asset/Business-logic-vulnerabilities-7-Weak-isolation-on-dual-use-endpoint-1.png)

> Chall này bảo xóa từ param đi và thử xem server trả về gì. Ban đầu thử xóa tham số của `current-password` thì lỗi, k đổi được. Xong xóa cả param + tham số đi thì vẫn change được. Chứng tỏ không cần param `current-password` thì vẫn đổi được pass -> đổi luôn của administrator:
> ![img](../asset/Business-logic-vulnerabilities-7-Weak-isolation-on-dual-use-endpoint-2.png) ![img](../asset/Business-logic-vulnerabilities-7-Weak-isolation-on-dual-use-endpoint-3.png) ![img](../asset/Business-logic-vulnerabilities-7-Weak-isolation-on-dual-use-endpoint-4.png)

---

#### Lab: Password reset broken logic

> Bài này có lỗi ở reset passwd, đổi passwd của carlos rồi vào `my-account` để solve

> Khi reset lại passwd phải có mail để gửi link về. Lab cũng cung cấp 1 server email để nhận link:
> ![img](../asset/Business-logic-vulnerabilities-8-Password-reset-broken-logic-0.png)

> Nhập và làm theo, dùng burp để chặn:
> ![img](../asset/Business-logic-vulnerabilities-8-Password-reset-broken-logic-1.png) ![img](../asset/Business-logic-vulnerabilities-8-Password-reset-broken-logic-2.png) ![img](../asset/Business-logic-vulnerabilities-8-Password-reset-broken-logic-3.png) ![img](../asset/Business-logic-vulnerabilities-8-Password-reset-broken-logic-4.png)

#### Users won't always follow the intended sequence

> Nhiều giao dịch dựa trên quy trình công việc được xác định bao gồm một chuỗi các bước. Giao diện web thường hướng dẫn user qua quy trình này, những attacker sẽ không tuân thủ theo những quy định

> Ví dụ: Nhiều ứng dụng sử dụng xác thực 2 yếu tố 2FA dùng để login. Theo quy định thì user phải làm theo điều này việc xác minh thì không phải họ làm, attacker sẽ bỏ qua hoàng toàn 2FA

#### Lab: 2FA simple bypass

> Lab này xác thực 2 yếu tố có thể bị bỏ qua, để solve hãy truy cập tài khoản của carlos

> Login: `wiener:peter`, victim: `carlos: montoya`

> Bài này thử brute force mã otp mà không được =)), nó chỉ cho nhập 1 lần. Nếu sai là cút luôn.
>
> Login với tài khoản victim, khi vào chỗ nhập mã otp thì trên path chuyển sang path `/my-account` thì solve luôn. Chứng tỏ làm cái nhập mã otp không sử dụng đến cũng được =))
> ![img](../asset/Business-logic-vulnerabilities-9-2FA-simple-bypass-0.png) ![img](../asset/Business-logic-vulnerabilities-9-2FA-simple-bypass-1.png) ![img](../asset/Business-logic-vulnerabilities-9-2FA-simple-bypass-2.png)

---

> Sử dụng công cụ như Burp Proxy hay Repeater giúp attacker có thể gửi đi gửi lại các request

> Để xác định lỗi này, brute force để gửi các yêu cầu không mong muốn.

#### Lab: Insufficient workflow validation

> Lab này đưa ra các giả định thiếu sót về chuỗi sự kiện quy trình mua hàng. Để solve hãy mua `Lightweight l334 jacket`
>
> Login: `wiener:peter`

> Bài này ban đầu cứ đặt 1 sản phẩm nhỏ hơn 100$ đã cho và chặn nó. Tới 1 path là `/cart/order-confirmation?order-confirmed=true` copy nó rồi chuyến sang sản phẩm kia rồi chặn và sửa nó khi bị lỗi không đủ tiền:
> ![img](../asset/Business-logic-vulnerabilities-10-Insufficient-workflow-validation-0.png)

> Nếu đủ tiền:
> ![img](../asset/Business-logic-vulnerabilities-10-Insufficient-workflow-validation-1.png)

> Nếu không đủ:
> ![img](../asset/Business-logic-vulnerabilities-10-Insufficient-workflow-validation-2.png)

> Nên ta đổi path `/cart` là oke

---

#### Lab: Authentication bypass via flawed state machine

> Des: Lab này đưa ra các giả định thiếu sót về chuỗi sự kiện quy trình đăng nhập. Lấy quyền admin và xóa `carlos`
>
> Đăng nhập bằng `wiener:peter`

> Ban đầu làm cứ tưởng đổi role thành administrator là oke:
> ![img](../asset/Business-logic-vulnerabilities-11-Authentication-bypass-via-flawed-state-machine-6.png)

> Nhưng không được, khi login, nó sẽ yêu cầu account, dùng burp để chặn nó khi gửi request đi, `forward` là 1 sẽ ra path : `/role-selector`, drop nó đi rồi quay lại trang chủ là được =))
> ![img](../asset/Business-logic-vulnerabilities-11-Authentication-bypass-via-flawed-state-machine-0.png) ![img](../asset/Business-logic-vulnerabilities-11-Authentication-bypass-via-flawed-state-machine-1.png) ![img](../asset/Business-logic-vulnerabilities-11-Authentication-bypass-via-flawed-state-machine-2.png) ![img](../asset/Business-logic-vulnerabilities-11-Authentication-bypass-via-flawed-state-machine-3.png) ![img](../asset/Business-logic-vulnerabilities-11-Authentication-bypass-via-flawed-state-machine-4.png) ![img](../asset/Business-logic-vulnerabilities-11-Authentication-bypass-via-flawed-state-machine-5.png)

### Domain-specific flaws

> Trong nhiều trường hợp, sẽ gặp phải lỗi logic. Ví dụ chức năng discount của shop
>
> Cửa hàng sẽ có mã giảm 10% đối với đơn từ 1000$ nhưng attacker sẽ dễ thay đổi chiết khấu.
>
> Trường hợp này ng mua sẽ lấy đủ 1000$ xong loại bỏ các sản phẩm không cần đi. Họ nhận được chiết khấu cho đơn hàng cho dù không đủ chỉ tiêu

#### Lab: Flawed enforcement of business rules

> Des: Có lỗ hổng khi mua hàng, để sovle hãy mua `Lightweight l33t leather jacket`
>
> Login bằng `wiener:peter`

> Mới vào lab đã thấy có `discount`:
> ![img](../asset/Business-logic-vulnerabilities-12-Flawed-enforcement-of-business-rules-0.png)

> Kéo xuống thì có cái sign up để nhập 1 cái phiếu discount khác=))
> ![img](../asset/Business-logic-vulnerabilities-12-Flawed-enforcement-of-business-rules-1.png)

> Khi nhận xong thì nhập discount so le sẽ được :
> ![img](../asset/Business-logic-vulnerabilities-12-Flawed-enforcement-of-business-rules-2.png) ![img](../asset/Business-logic-vulnerabilities-12-Flawed-enforcement-of-business-rules-3.png)

---

#### Lab: Infinite money logic flaw

> Des: Có lỗ hổng khi mua hàng, để sovle hãy mua `Lightweight l33t leather jacket`
>
> Login bằng `wiener:peter`

> Giao diện:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-0.png)

> Đầu tiên thì cứ mua trước 1 đồ gì đó:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-1.png)

> Sau đó qua `/home` để lấy mã giảm giá:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-2.png)

> Sau đó apply mã đó vào để được giảm:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-3.png) ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-4.png)

> Sau đó click vào `Place order` để nhận code:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-5.png)

> Sau đó copy chuyển sang `my-account` để áp mã:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-6.png) ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-7.png)

> -> Nó đã được discount lại tiền nhiều hơn lúc ban đầu (3$)

> Vì nó được thêm 3$ nên ta sẽ tận dụng lỗi này để auto quá trình này. Sử dụng `Project options -> sessions` làm theo như sau:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-8.png)

> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-9.png) ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-10.png)

> Để `include all URLs`:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-11.png)

> Chọn `Run a macro`:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-12.png) ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-13.png)

> Sẽ như này:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-14.png)

> Click (chuột trái rồi chọn thêm):
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-15.png) ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-16.png) ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-17.png) ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-18.png) ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-19.png)

> Tiếp đó:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-20.png)

> `Configure item` :
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-21.png)

> Sẽ hiện ra:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-22.png)

> Set up:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-23.png)

> `Configure item` tiếp:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-24.png)

> Set up:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-25.png)

> Sau đó có thể test thử trước:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-26.png)

> Oke rồi đó:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-27.png)

> Sang `HTTP history` để tìm path `/my-account`:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-28.png)

> Send sang `intruder` và set up nó:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-29.png) ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-30.png)

> Chỗ này sẽ là tạo 1 `Resource pool` mới với `maximum concurrent request là 1`:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-31.png)

> Start và đợi kết quả:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-32.png)

> Mua đồ thêm thôi:
> ![img](../asset/Business-logic-vulnerabilities-13-Infinite-money-logic-flaw-33.png)

### Providing an encryption oracle

> Các tình huống nguy hiểm có thể xảy ra khi input do user kiểm soát được encrypted và cipher lại được cung cấp cho user theo 1 cách nào đó

> Loại input này được gọi là `Encryption oracle` . Attacker có thể sử dụng input để encrypt data tùy ý bằng cách sử dụng các thuật toán chính xác và khóa không đối xứng

> Điều này sẽ trở nên nguy hiểm khi các input khác do user kiểm soát trong ứng dụng được mã hóa bằng cùng 1 mật mã. Attacker có thể dự đoán mã để tạo input hợp lệ sau đó chuyển nó vào các function nhạy cảm

#### Lab: Authentication bypass via encryption oracle

> Des: Lab này làm lộ ra encrytion oracle của user. Để sovle thì hãy truy cập vào admin và xóa carlos

> Login bằng : `wiener:peter`

> Giao diện:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-0.png)

> Nếu khi login ta click vào `Stay logged in` thì sẽ có cookie được mã hóa:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-1.png)

> Khi comment bằng một mail invalid thì sẽ lỗi và `cookie notification` sẽ được mã hóa trước khi chuyển về lại blog mà bạn comment:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-2.png) ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-3.png) ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-4.png) ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-5.png)

> Suy ra điều này phải được giải mã từ cookie notification. Gửi `POST /post/comment` và `GET /post?postid=x` tới repeater

> Copy `stay-logged-in` rồi paste vào `notification` tại path `/post?postId=x` rồi xem response:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-6.png) ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-7.png)

> Tại tab `ENCRYPT` (tự đặt tên ở repeater) đổi email thành `administrator:xxxx` x là copy từ response trước:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-8.png)

> Copy `Set-cookie: notification:xxxx`:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-9.png)

> Qua tab `DECRYPT` paste vào Cookie `notification` và xem response:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-10.png)

> Qua lại `ENCRYPT` và send cookie ở response như này:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-11.png)

> Ban đầu là decode qua URL, Base64 (click chuột phải chọn các bit như sau):
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-12.png)

> Sau đó encode ngược lại để được script:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-13.png)

> Qua DECRYPT dán script vào cookie `notification`:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-14.png)

> Thấy response vì ít nhất là 16 kí tự tại input nên sửa lại:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-15.png)

> Làm lại các bước decode sau đó gửi nó sẽ trả về `administrator:xxxx` và không có lỗi
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-16.png)

> Dùng burp chặn `/home` và sửa `stay-logged-in:scrip` và xóa `session`:
> ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-17.png) ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-18.png) ![img](../asset/Business-logic-vulnerabilities-14-Authentication-bypass-via-encryption-oracle-19.png)
