## Máy tính cầm tay Python

Project này được xây dựng cho đề tài: **Tìm hiểu ngôn ngữ lập trình Python và viết chương trình máy tính cầm tay**.

Ứng dụng sử dụng **Python** và thư viện giao diện đồ họa **Tkinter**. Tkinter là thư viện có sẵn trong Python nên người dùng không cần cài đặt thêm thư viện bên ngoài.

## 1. Mục tiêu project

- Tìm hiểu cú pháp và cách lập trình bằng Python.
- Xây dựng chương trình máy tính cầm tay có giao diện đồ họa.
- Hỗ trợ các phép toán cơ bản, nâng cao và một số hàm toán học.
- Lưu và hiển thị lịch sử phép tính.
- Xử lý lỗi để chương trình không bị dừng đột ngột khi nhập sai.

## 2. Cấu trúc thư mục

```text
python-calculator-project/
│
├── main.py       # Mã nguồn chính của chương trình
├── README.md     # Tài liệu hướng dẫn sử dụng
├── history.txt   # File lưu lịch sử phép tính
└── report.md     # Báo cáo ngắn về đề tài
```

## 3. Yêu cầu môi trường

- Hệ điều hành: Windows, Linux hoặc macOS.
- Python phiên bản 3.8 trở lên.
- Không cần cài thêm thư viện ngoài.

Kiểm tra phiên bản Python:

```bash
python --version
```

Nếu máy dùng lệnh `python3`, có thể kiểm tra bằng:

```bash
python3 --version
```

## 4. Cách chạy chương trình

Mở Command Prompt hoặc Terminal tại thư mục `python-calculator-project`, sau đó chạy:

```bash
python main.py
```

Nếu hệ thống dùng lệnh `python3`, chạy:

```bash
python3 main.py
```

## 5. Chức năng chính

### 5.1. Phép toán cơ bản

- Cộng: `+`
- Trừ: `-`
- Nhân: `*`
- Chia: `/`

### 5.2. Phép toán nâng cao

- Lũy thừa: nút `^`, được xử lý thành toán tử `**` trong Python.
- Căn bậc hai: nút `√`, được xử lý thành hàm `sqrt()`.
- Chia lấy dư: `%`.

### 5.3. Hàm toán học

- `sin()`
- `cos()`
- `tan()`
- `log()` hoặc `ln()`
- `factorial()` thông qua nút `!`
- Hằng số `π` được xử lý thành `pi`.

Lưu ý: Các hàm lượng giác mặc định tính toán theo đơn vị Độ (DEG). Bạn có thể dễ dàng chuyển đổi giữa chế độ Độ (DEG) và Radian (RAD) thông qua các nút chọn trên giao diện.

Ví dụ:
- Ở chế độ DEG: `sin(30) = 0.5`, `cos(90) = 0`
- Ở chế độ RAD: `sin(pi/2) = 1`
- Các phép toán khác:
  ```text
  sqrt(16) = 4
  2**3 = 8
  10%3 = 1
  ```

## 6. Chức năng giao diện

- Ô hiển thị biểu thức và kết quả.
- Các nút số từ 0 đến 9.
- Nút dấu chấm thập phân.
- Các nút phép toán.
- Nút `C` để xóa toàn bộ biểu thức.
- Nút `DEL` để xóa từng ký tự.
- Nút `=` để tính kết quả.
- Khu vực hiển thị lịch sử phép tính.
- Nút xóa lịch sử.

## 7. Lịch sử phép tính

Sau mỗi phép tính thành công, chương trình sẽ:

1. Thêm biểu thức và kết quả vào danh sách lịch sử trên giao diện.
2. Lưu lịch sử vào file `history.txt`.
3. Tự động đọc lại lịch sử cũ khi mở chương trình lần sau.

## 8. Xử lý lỗi

Chương trình có xử lý các lỗi thường gặp:

- Chia cho 0.
- Biểu thức không hợp lệ.
- Dùng sai cú pháp hàm toán học.
- Nhập hàm hoặc ký tự không được hỗ trợ.

Khi có lỗi, chương trình hiển thị hộp thoại thông báo thay vì bị crash.

## 9. Ghi chú về an toàn khi tính toán biểu thức

Chương trình có sử dụng `eval()` để tính biểu thức, nhưng đã giới hạn môi trường thực thi:

- Không cho phép truy cập `__builtins__`.
- Chỉ cho phép các hàm toán học được khai báo trong danh sách an toàn như `sin`, `cos`, `sqrt`, `log`, `factorial`, `pi`, `e`.

Cách làm này giúp chương trình an toàn hơn so với việc dùng `eval()` trực tiếp không kiểm soát.

## 10. Gợi ý cải tiến

- Thêm bàn phím vật lý để nhập biểu thức.
- Thêm giao diện dark mode.
- Thêm chức năng xuất lịch sử ra file CSV.
- Đóng gói thành file `.exe` bằng PyInstaller.
