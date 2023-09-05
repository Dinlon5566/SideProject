import subprocess
import time
from tkinter import Tk, Label, Button, StringVar
import threading
import re
def ping_host():
    """進行一次ping操作並返回結果和延遲時間"""
    try:
        start_time = time.time()
        response = subprocess.run(['ping',  '-w', '1','-n', '2' , '8.8.8.8'], capture_output=True, shell=True)
        stdout_str = response.stdout.decode('big5')
        match = re.search(r'時間=(\d+)ms', stdout_str)
        
        if match:
            delay = int(match.group(1))
            print(match)
            if delay <= int(200):
                return "正常", int(delay)
            else:
                return "高延遲", int(delay)
        else:
            return "無法連接", None
    except Exception as e:
        return f"錯誤: {e}", None

# 初始化Tkinter窗口
root = Tk()
root.title("網路延遲檢查工具")

# 定義StringVar變量來更新狀態和延遲時間
status_var = StringVar(value="狀態：未開始")
delay_var = StringVar(value="延遲時間：未知")

# 定義Label來顯示狀態和延遲時間
status_label = Label(root, textvariable=status_var, font=("Arial", 24))
status_label.pack(pady=10)

delay_label = Label(root, textvariable=delay_var, font=("Arial", 24))
delay_label.pack(pady=10)

is_running = False

def check_ping():
    global is_running
    while is_running:
        status, delay = ping_host()
        status_var.set(f"狀態：{status}")
        if delay is not None:
            delay_var.set(f"延遲時間：{delay} ms")
        else:
            delay_var.set(f"延遲時間：未知")

        if status == "正常":
            root.configure(bg="#84EB80")
            status_label.configure(bg="#84EB80")
            delay_label.configure(bg="#84EB80")
        elif status == "高延遲":
            root.configure(bg="yellow")
            status_label.configure(bg="yellow")
            delay_label.configure(bg="yellow")
        else:
            root.configure(bg="red")
            status_label.configure(bg="red")
            delay_label.configure(bg="red")

        time.sleep(0.5)


def start_stop_ping():
    global is_running
    if start_stop_button.cget("text") == "開始":
        is_running = True
        start_stop_button.config(text="停止")
        threading.Thread(target=check_ping).start()
    else:
        is_running = False
        start_stop_button.config(text="開始")

# 定義開始/停止按鈕
start_stop_button = Button(root, text="開始", command=start_stop_ping, font=("Arial", 24))
start_stop_button.pack(pady=10)

# 定義關閉按鈕的回調函數
def close_app():
    root.destroy()

# 定義關閉按鈕
close_button = Button(root, text="關閉", command=close_app, font=("Arial", 24))
close_button.pack(pady=10)

# 運行Tkinter事件循環
root.mainloop()
