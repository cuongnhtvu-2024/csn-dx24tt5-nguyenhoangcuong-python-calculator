# Báo cáo đề tài: Tìm hiểu ngôn ngữ lập trình Python và viết chương trình máy tính cầm tay

## 1. Giới thiệu đề tài

Trong thời đại công nghệ thông tin phát triển mạnh mẽ, việc học một ngôn ngữ lập trình phổ biến và dễ tiếp cận là rất cần thiết đối với sinh viên ngành Công nghệ thông tin. Python là một trong những ngôn ngữ lập trình được sử dụng rộng rãi nhờ cú pháp đơn giản, dễ đọc và có nhiều thư viện hỗ trợ.

Đề tài **“Tìm hiểu ngôn ngữ lập trình Python và viết chương trình máy tính cầm tay”** tập trung vào việc tìm hiểu kiến thức cơ bản của Python, đồng thời áp dụng vào xây dựng một ứng dụng máy tính cầm tay có giao diện đồ họa. Chương trình hỗ trợ các phép toán cơ bản, phép toán nâng cao, hàm toán học và lưu lịch sử phép tính.

## 2. Lý do chọn đề tài

Máy tính cầm tay là một ứng dụng quen thuộc, gần gũi với học sinh, sinh viên và người dùng máy tính. Thông qua việc xây dựng chương trình máy tính cầm tay, sinh viên có thể rèn luyện nhiều kỹ năng lập trình quan trọng như:

- Thiết kế giao diện người dùng.
- Xử lý sự kiện khi người dùng nhấn nút.
- Xử lý chuỗi biểu thức toán học.
- Sử dụng thư viện toán học trong Python.
- Kiểm soát lỗi trong quá trình chạy chương trình.
- Lưu trữ dữ liệu đơn giản bằng file văn bản.

Đề tài có độ khó vừa phải, phù hợp với sinh viên mới học Python nhưng vẫn có đủ nội dung để mở rộng và phát triển thêm.

## 3. Mục tiêu đề tài

Các mục tiêu chính của đề tài gồm:

1. Tìm hiểu tổng quan về ngôn ngữ lập trình Python.
2. Nắm được cách sử dụng thư viện Tkinter để xây dựng giao diện đồ họa.
3. Xây dựng chương trình máy tính cầm tay dễ sử dụng.
4. Hỗ trợ các phép toán cơ bản như cộng, trừ, nhân, chia.
5. Hỗ trợ các phép toán nâng cao như lũy thừa, căn bậc hai, modulo.
6. Hỗ trợ một số hàm toán học như sin, cos, tan, log, ln, factorial.
7. Lưu và hiển thị lịch sử phép tính.
8. Xử lý lỗi để chương trình hoạt động ổn định.

## 4. Cơ sở lý thuyết về Python

### 4.1. Giới thiệu Python

Python là ngôn ngữ lập trình bậc cao, thông dịch, được thiết kế với cú pháp rõ ràng và dễ đọc. Python thường được sử dụng trong nhiều lĩnh vực như phát triển phần mềm, trí tuệ nhân tạo, khoa học dữ liệu, tự động hóa, lập trình web và giáo dục.

Một số ưu điểm của Python:

- Cú pháp đơn giản, gần với ngôn ngữ tự nhiên.
- Có cộng đồng sử dụng lớn.
- Hỗ trợ nhiều thư viện tiêu chuẩn.
- Có thể chạy trên nhiều hệ điều hành.
- Phù hợp cho người mới bắt đầu học lập trình.

### 4.2. Thư viện Tkinter

Tkinter là thư viện giao diện đồ họa có sẵn trong Python. Với Tkinter, lập trình viên có thể tạo cửa sổ, nút bấm, ô nhập liệu, nhãn, danh sách và nhiều thành phần giao diện khác.

Trong chương trình máy tính cầm tay, Tkinter được dùng để:

- Tạo cửa sổ chính.
- Tạo ô hiển thị biểu thức và kết quả.
- Tạo các nút số và nút phép toán.
- Tạo khu vực hiển thị lịch sử phép tính.
- Hiển thị hộp thoại thông báo lỗi.

### 4.3. Thư viện math

`math` là thư viện tiêu chuẩn của Python, cung cấp nhiều hàm toán học như:

- `sin()`
- `cos()`
- `tan()`
- `sqrt()`
- `log()`
- `factorial()`
- Hằng số `pi`, `e`

Chương trình sử dụng thư viện này để thực hiện các phép toán nâng cao và hàm toán học.

## 5. Các chức năng của chương trình

Chương trình máy tính cầm tay Python có các chức năng chính sau:

### 5.1. Phép toán cơ bản

- Cộng hai hoặc nhiều số.
- Trừ hai hoặc nhiều số.
- Nhân các số.
- Chia các số.

### 5.2. Phép toán nâng cao

- Lũy thừa bằng toán tử `**`.
- Căn bậc hai bằng hàm `sqrt()`.
- Chia lấy dư bằng toán tử `%`.

### 5.3. Hàm toán học

- Tính sin, cos, tan (hỗ trợ chuyển đổi giữa hai chế độ đo góc DEG và RAD, mặc định là DEG).
- Tính log cơ số 10 và log tự nhiên (nút log tính log10, nút ln tính ln).
- Tính giai thừa.
- Sử dụng hằng số pi.

### 5.4. Giao diện người dùng

- Giao diện có tiêu đề “Máy tính cầm tay Python”.
- Bố cục nút rõ ràng như máy tính cầm tay.
- Màu sắc nhẹ nhàng, hiện đại.
- Font chữ dễ nhìn.
- Có khu vực hiển thị lịch sử phép tính.

### 5.5. Lưu lịch sử phép tính

Sau mỗi phép tính thành công, chương trình lưu biểu thức và kết quả vào danh sách lịch sử. Lịch sử được hiển thị trên giao diện và lưu vào file `history.txt` để có thể xem lại ở lần chạy sau.

### 5.6. Xử lý lỗi

Chương trình xử lý các lỗi thường gặp như:

- Chia cho 0.
- Nhập biểu thức không hợp lệ.
- Gọi sai hàm toán học.
- Nhập ký tự hoặc hàm không được hỗ trợ.

Khi có lỗi, chương trình hiển thị thông báo thay vì bị dừng đột ngột.

## 6. Phân tích và thiết kế chương trình

### 6.1. Phân tích yêu cầu

Người dùng cần một chương trình máy tính cầm tay có giao diện trực quan, dễ thao tác và có khả năng thực hiện nhiều phép tính khác nhau. Chương trình cần chạy trực tiếp bằng Python, không yêu cầu cài đặt thư viện ngoài.

### 6.2. Thiết kế giao diện

Giao diện được chia thành các khu vực:

1. Tiêu đề chương trình.
2. Ô hiển thị biểu thức và kết quả.
3. Khung chứa các nút số, toán tử và hàm toán học.
4. Khu vực lịch sử phép tính.
5. Nút xóa lịch sử.

### 6.3. Thiết kế xử lý

Chương trình được xây dựng theo hướng lập trình hướng đối tượng với lớp `CalculatorApp`. Lớp này quản lý toàn bộ giao diện và logic xử lý.

Các phương thức chính:

- `create_widgets()`: tạo giao diện chương trình.
- `on_button_click()`: xử lý khi người dùng nhấn nút.
- `calculate()`: tính kết quả biểu thức.
- `clear()`: xóa toàn bộ biểu thức.
- `delete_last()`: xóa ký tự cuối cùng.
- `update_history()`: cập nhật lịch sử trên giao diện.
- `save_history()`: lưu lịch sử ra file.

### 6.4. Thiết kế dữ liệu

Chương trình sử dụng:

- Biến chuỗi `expression` để lưu biểu thức hiện tại.
- Danh sách `history` để lưu lịch sử phép tính.
- File `history.txt` để lưu lịch sử lâu dài.

## 7. Giải thích mã nguồn chính

### 7.1. Lớp CalculatorApp

Lớp `CalculatorApp` là thành phần quan trọng nhất của chương trình. Lớp này chịu trách nhiệm tạo giao diện, xử lý sự kiện, tính toán kết quả và quản lý lịch sử.

Khi khởi tạo, chương trình thiết lập tiêu đề cửa sổ, kích thước cửa sổ, màu nền, biến lưu biểu thức và file lịch sử.

### 7.2. Phương thức create_widgets()

Phương thức `create_widgets()` tạo các thành phần giao diện như nhãn tiêu đề, ô nhập biểu thức, các nút bấm và danh sách lịch sử. Các nút được sắp xếp theo dạng lưới để giống bố cục của máy tính cầm tay.

### 7.3. Phương thức on_button_click()

Phương thức `on_button_click()` nhận giá trị của nút được nhấn và quyết định hành động tương ứng:

- Nếu nhấn `C`, chương trình xóa biểu thức.
- Nếu nhấn `DEL`, chương trình xóa ký tự cuối.
- Nếu nhấn `=`, chương trình tính kết quả.
- Nếu nhấn các nút toán học, chương trình thêm ký hiệu hoặc hàm tương ứng vào biểu thức.

### 7.4. Phương thức calculate()

Phương thức `calculate()` dùng để tính giá trị của biểu thức. Chương trình sử dụng `eval()` nhưng có giới hạn môi trường thực thi để đảm bảo an toàn hơn. Chỉ các hàm toán học được khai báo trong danh sách cho phép mới được sử dụng.

Phương thức này cũng bắt các lỗi như chia cho 0, lỗi cú pháp, lỗi giá trị và lỗi gọi hàm sai.

### 7.5. Phương thức update_history() và save_history()

Sau khi tính toán thành công, `update_history()` thêm kết quả vào danh sách lịch sử trên giao diện. Sau đó `save_history()` ghi toàn bộ lịch sử vào file `history.txt`.

## 8. Kết quả đạt được

Sau khi hoàn thành, chương trình đạt được các kết quả sau:

- Xây dựng được ứng dụng máy tính cầm tay bằng Python.
- Có giao diện đồ họa bằng Tkinter.
- Hỗ trợ các phép toán cơ bản và nâng cao.
- Hỗ trợ một số hàm toán học thường dùng.
- Có chức năng lưu và hiển thị lịch sử phép tính.
- Có xử lý lỗi giúp chương trình hoạt động ổn định.
- Mã nguồn rõ ràng, có comment tiếng Việt, phù hợp cho sinh viên học tập và nộp bài.

## 9. Hạn chế

Chương trình vẫn còn một số hạn chế:

- Chưa hỗ trợ nhập liệu trực tiếp từ bàn phím một cách đầy đủ.
- Chưa có chế độ giao diện tối.
- Chưa có chức năng xuất lịch sử sang các định dạng khác như CSV hoặc Excel.
- Việc tính biểu thức vẫn dựa trên `eval()` có kiểm soát, chưa xây dựng bộ phân tích biểu thức riêng.

## 10. Hướng phát triển

Trong tương lai, chương trình có thể được phát triển thêm các chức năng:

- Hỗ trợ nhập biểu thức từ bàn phím.
- Thêm các hàm toán học nâng cao như arcsin, arccos, arctan.
- Thêm giao diện dark mode.
- Thêm chức năng lưu lịch sử theo ngày giờ.
- Đóng gói chương trình thành file `.exe` để chạy dễ dàng trên Windows.
- Xây dựng bộ phân tích biểu thức riêng thay cho `eval()`.

## 11. Kết luận

Đề tài **“Tìm hiểu ngôn ngữ lập trình Python và viết chương trình máy tính cầm tay”** giúp sinh viên hiểu rõ hơn về ngôn ngữ Python, thư viện Tkinter và cách xây dựng một ứng dụng có giao diện đồ họa. Thông qua đề tài, sinh viên được rèn luyện kỹ năng phân tích yêu cầu, thiết kế giao diện, xử lý sự kiện, xử lý lỗi và lưu trữ dữ liệu đơn giản.

Chương trình máy tính cầm tay tuy không quá phức tạp nhưng có tính ứng dụng thực tế, phù hợp để làm đồ án môn học và làm nền tảng cho các project Python nâng cao hơn.
