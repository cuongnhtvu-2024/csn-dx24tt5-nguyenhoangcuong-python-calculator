"""
Chương trình: Máy tính cầm tay Python
Tác giả: Sinh viên Nguyễn Hoàng Cương - DX24TT5
Mô tả: Ứng dụng máy tính cầm tay có giao diện Tkinter, hỗ trợ các phép toán cơ bản,
nâng cao, hàm toán học và lưu lịch sử phép tính.
"""

import math
import tkinter as tk
from tkinter import messagebox
from pathlib import Path


class CalculatorApp:
    """Lớp chính quản lý giao diện và chức năng của máy tính."""

    def __init__(self, root):
        self.root = root
        self.root.title("Máy tính cầm tay Python")
        self.root.geometry("520x750")
        self.root.minsize(480, 600)
        self.root.configure(bg="#eef2f7")

        # Biểu thức hiện tại người dùng đang nhập
        self.expression = ""

        # Danh sách lưu lịch sử phép tính trong phiên chạy hiện tại
        self.history = []

        # File lưu lịch sử phép tính
        self.history_file = Path(__file__).parent / "history.txt"

        # Tạo biến StringVar để cập nhật ô hiển thị dễ dàng
        self.display_var = tk.StringVar(value="")

        # Chế độ đo góc mặc định (DEG: Độ, RAD: Radian)
        self.angle_mode = "DEG"

        self.create_widgets()
        self.load_history()

    def create_widgets(self):
        """Tạo toàn bộ thành phần giao diện cho chương trình."""
        title_label = tk.Label(
            self.root,
            text="MÁY TÍNH CẦM TAY PYTHON",
            font=("Segoe UI", 18, "bold"),
            bg="#eef2f7",
            fg="#1f2937",
            pady=12,
        )
        title_label.pack(fill="x")

        main_frame = tk.Frame(self.root, bg="#eef2f7", padx=14, pady=8)
        main_frame.pack(fill="both", expand=True)

        # Ô hiển thị biểu thức và kết quả
        display_entry = tk.Entry(
            main_frame,
            textvariable=self.display_var,
            font=("Consolas", 22),
            justify="right",
            bd=0,
            relief="flat",
            bg="#ffffff",
            fg="#111827",
            insertbackground="#111827",
        )
        display_entry.pack(fill="x", ipady=14, pady=(0, 12))

        # Khung chọn chế độ góc (DEG / RAD)
        mode_frame = tk.Frame(main_frame, bg="#eef2f7")
        mode_frame.pack(fill="x", pady=(0, 8))

        self.deg_btn = tk.Button(
            mode_frame,
            text="DEG",
            font=("Segoe UI", 9, "bold"),
            bd=0,
            relief="flat",
            cursor="hand2",
            command=lambda: self.set_angle_mode("DEG"),
            width=8,
            pady=4,
        )
        self.deg_btn.pack(side="left", padx=(0, 4))

        self.rad_btn = tk.Button(
            mode_frame,
            text="RAD",
            font=("Segoe UI", 9, "bold"),
            bd=0,
            relief="flat",
            cursor="hand2",
            command=lambda: self.set_angle_mode("RAD"),
            width=8,
            pady=4,
        )
        self.rad_btn.pack(side="left")
        self.update_mode_buttons()

        # Khung chứa các nút bấm
        button_frame = tk.Frame(main_frame, bg="#eef2f7")
        button_frame.pack(fill="both")

        # Danh sách nút theo bố cục máy tính cầm tay
        buttons = [
            ["C", "DEL", "(", ")", "√"],
            ["sin", "cos", "tan", "log", "ln"],
            ["7", "8", "9", "/", "^"],
            ["4", "5", "6", "*", "%"],
            ["1", "2", "3", "-", "!"],
            ["0", ".", "=", "+", "π"],
        ]

        for row_index, row in enumerate(buttons):
            button_frame.rowconfigure(row_index, weight=1)
            for col_index, text in enumerate(row):
                button_frame.columnconfigure(col_index, weight=1)
                button = tk.Button(
                    button_frame,
                    text=text,
                    font=("Segoe UI", 13, "bold"),
                    bd=0,
                    relief="flat",
                    cursor="hand2",
                    command=lambda value=text: self.on_button_click(value),
                )
                button.grid(
                    row=row_index,
                    column=col_index,
                    sticky="nsew",
                    padx=4,
                    pady=4,
                    ipady=12,
                )
                self.style_button(button, text)

        # Khu vực lịch sử phép tính
        history_header = tk.Frame(main_frame, bg="#eef2f7")
        history_header.pack(fill="x", pady=(14, 6))

        history_label = tk.Label(
            history_header,
            text="Lịch sử phép tính",
            font=("Segoe UI", 13, "bold"),
            bg="#eef2f7",
            fg="#1f2937",
        )
        history_label.pack(side="left")

        clear_history_button = tk.Button(
            history_header,
            text="Xóa lịch sử",
            font=("Segoe UI", 10, "bold"),
            bg="#ef4444",
            fg="#ffffff",
            activebackground="#dc2626",
            activeforeground="#ffffff",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.clear_history,
            padx=10,
            pady=5,
        )
        clear_history_button.pack(side="right")

        history_frame = tk.Frame(main_frame, bg="#ffffff", bd=0)
        history_frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(history_frame)
        scrollbar.pack(side="right", fill="y")

        self.history_listbox = tk.Listbox(
            history_frame,
            font=("Consolas", 11),
            bg="#ffffff",
            fg="#374151",
            bd=0,
            relief="flat",
            yscrollcommand=scrollbar.set,
            selectbackground="#bfdbfe",
            selectforeground="#111827",
        )
        self.history_listbox.pack(side="left", fill="both", expand=True, padx=8, pady=8)
        scrollbar.config(command=self.history_listbox.yview)

    def style_button(self, button, text):
        """Áp dụng màu sắc cho từng nhóm nút để giao diện dễ nhìn hơn."""
        if text == "=":
            bg, fg, active = "#2563eb", "#ffffff", "#1d4ed8"
        elif text in {"C", "DEL"}:
            bg, fg, active = "#f97316", "#ffffff", "#ea580c"
        elif text in {"+", "-", "*", "/", "^", "%", "√", "!"}:
            bg, fg, active = "#dbeafe", "#1e3a8a", "#bfdbfe"
        elif text in {"sin", "cos", "tan", "log", "ln", "π"}:
            bg, fg, active = "#e0e7ff", "#3730a3", "#c7d2fe"
        else:
            bg, fg, active = "#ffffff", "#111827", "#e5e7eb"

        button.configure(
            bg=bg,
            fg=fg,
            activebackground=active,
            activeforeground=fg,
        )

    def on_button_click(self, value):
        """Xử lý sự kiện khi người dùng nhấn một nút trên giao diện."""
        if value == "C":
            self.clear()
        elif value == "DEL":
            self.delete_last()
        elif value == "=":
            self.calculate()
        elif value == "√":
            self.expression += "sqrt("
        elif value == "^":
            self.expression += "**"
        elif value == "π":
            self.expression += "pi"
        elif value == "!":
            self.expression += "factorial("
        elif value in {"sin", "cos", "tan", "log", "ln"}:
            # log là log cơ số 10, ln là log tự nhiên
            if value == "ln":
                self.expression += "log("
            elif value == "log":
                self.expression += "log10("
            else:
                self.expression += f"{value}("
        else:
            self.expression += value

        self.display_var.set(self.expression)

    def calculate(self):
        """Tính toán biểu thức và xử lý lỗi để chương trình không bị crash."""
        if not self.expression.strip():
            return

        original_expression = self.expression

        # Chỉ cho phép một số hàm và hằng số toán học an toàn.
        # Không truyền __builtins__ để hạn chế rủi ro khi dùng eval.
        allowed_names = {
            "sin": self.safe_sin,
            "cos": self.safe_cos,
            "tan": self.safe_tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "factorial": math.factorial,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
            "round": round,
        }

        try:
            result = eval(original_expression, {"__builtins__": {}}, allowed_names)

            # Làm đẹp kết quả: nếu là số nguyên dạng 5.0 thì hiển thị 5
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.expression = str(result)
            self.display_var.set(self.expression)
            self.update_history(original_expression, result)
            self.save_history()

        except ZeroDivisionError:
            self.show_error("Không thể chia cho 0.")
        except ValueError:
            self.show_error("Giá trị nhập vào không phù hợp với hàm toán học.")
        except SyntaxError:
            self.show_error("Biểu thức không hợp lệ. Vui lòng kiểm tra lại.")
        except NameError:
            self.show_error("Biểu thức chứa ký tự hoặc hàm không được hỗ trợ.")
        except TypeError:
            self.show_error("Bạn đã dùng sai cú pháp của hàm toán học.")
        except Exception:
            self.show_error("Đã xảy ra lỗi khi tính toán biểu thức.")

    def show_error(self, message):
        """Hiển thị lỗi thân thiện cho người dùng."""
        messagebox.showerror("Lỗi", message)
        self.display_var.set("Lỗi")
        self.expression = ""

    def clear(self):
        """Xóa toàn bộ biểu thức hiện tại."""
        self.expression = ""
        self.display_var.set("")

    def delete_last(self):
        """Xóa ký tự cuối cùng trong biểu thức."""
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)

    def update_history(self, expression, result):
        """Cập nhật lịch sử phép tính trên giao diện."""
        item = f"{expression} = {result}"
        self.history.append(item)
        self.history_listbox.insert(tk.END, item)
        self.history_listbox.yview_moveto(1)

    def save_history(self):
        """Lưu toàn bộ lịch sử phép tính ra file history.txt."""
        try:
            with self.history_file.open("w", encoding="utf-8") as file:
                for item in self.history:
                    file.write(item + "\n")
        except OSError:
            messagebox.showwarning("Cảnh báo", "Không thể lưu lịch sử ra file history.txt.")

    def load_history(self):
        """Đọc lịch sử cũ từ file history.txt nếu file đã tồn tại."""
        if not self.history_file.exists():
            self.history_file.write_text("", encoding="utf-8")
            return

        try:
            lines = self.history_file.read_text(encoding="utf-8").splitlines()
            for line in lines:
                if line.strip():
                    self.history.append(line)
                    self.history_listbox.insert(tk.END, line)
        except OSError:
            messagebox.showwarning("Cảnh báo", "Không thể đọc file history.txt.")

    def clear_history(self):
        """Xóa lịch sử trên giao diện và trong file."""
        self.history.clear()
        self.history_listbox.delete(0, tk.END)
        self.save_history()

    def set_angle_mode(self, mode):
        """Đặt chế độ đo góc và cập nhật các nút chọn."""
        self.angle_mode = mode
        self.update_mode_buttons()

    def update_mode_buttons(self):
        """Cập nhật giao diện (màu sắc) cho các nút chọn DEG / RAD."""
        if self.angle_mode == "DEG":
            self.deg_btn.configure(
                bg="#2563eb",
                fg="#ffffff",
                activebackground="#1d4ed8",
                activeforeground="#ffffff",
            )
            self.rad_btn.configure(
                bg="#e5e7eb",
                fg="#4b5563",
                activebackground="#d1d5db",
                activeforeground="#4b5563",
            )
        else:
            self.deg_btn.configure(
                bg="#e5e7eb",
                fg="#4b5563",
                activebackground="#d1d5db",
                activeforeground="#4b5563",
            )
            self.rad_btn.configure(
                bg="#10b981",
                fg="#ffffff",
                activebackground="#059669",
                activeforeground="#ffffff",
            )

    def safe_sin(self, x):
        """Tính sine của x tùy theo chế độ góc DEG hay RAD."""
        if self.angle_mode == "DEG":
            return round(math.sin(math.radians(x)), 10)
        return math.sin(x)

    def safe_cos(self, x):
        """Tính cosine của x tùy theo chế độ góc DEG hay RAD."""
        if self.angle_mode == "DEG":
            return round(math.cos(math.radians(x)), 10)
        return math.cos(x)

    def safe_tan(self, x):
        """Tính tangent của x tùy theo chế độ góc DEG hay RAD."""
        if self.angle_mode == "DEG":
            # Kiểm tra xem cos(x) có gần 0 hay không để phát hiện tangent không xác định
            if abs(math.cos(math.radians(x))) < 1e-15:
                raise ValueError("Tangent không xác định tại góc này.")
            return round(math.tan(math.radians(x)), 10)
        else:
            if abs(math.cos(x)) < 1e-15:
                raise ValueError("Tangent không xác định tại góc này.")
            return math.tan(x)


def main():
    """Hàm khởi động chương trình."""
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
