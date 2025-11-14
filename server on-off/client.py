import socket
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

HOST = '192.168.1.158'
PORT = 12345

def get_mac_address():
    filename = "mac_address.txt"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            mac = f.read().strip()
    else:
        mac = simpledialog.askstring("آدرس MAC", "لطفاً آدرس MAC سرور را وارد کنید:")
        if mac:
            with open(filename, "w") as f:
                f.write(mac)
        else:
            messagebox.showerror("خطا", "آدرس MAC وارد نشد.")
            return None
    return mac

def wake_on_lan(mac_address):
    if not mac_address:
        return

    mac_address = mac_address.replace(":", "").replace("-", "")
    if len(mac_address) != 12:
        messagebox.showerror("خطا", "آدرس MAC نادرست است.")
        return

    mac_bytes = bytes.fromhex(mac_address)
    magic_packet = b'\xff' * 6 + mac_bytes * 16

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(magic_packet, ('<broadcast>', 9))

    messagebox.showinfo("ارسال شد", "پکت روشن کردن (Wake-on-LAN) ارسال شد.")

def connect_to_server():
    username = entry_username.get()
    password = entry_password.get()

    try:
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.sendall(f"{username},{password}".encode())
        response = sock.recv(1024).decode()

        text_log.config(state='normal')
        text_log.insert(tk.END, "✅ پاسخ سرور: " + response + "\n")
        text_log.config(state='disabled')

        if "موفقیت‌آمیز" in response:
            button_shutdown.config(state='normal')
            button_exit.config(state='normal')
        else:
            messagebox.showerror("ورود ناموفق", "نام کاربری یا رمز عبور اشتباه است.")
    except (ConnectionRefusedError, socket.timeout, OSError):
        answer = messagebox.askyesno("سرور خاموش است", "آیا مایلید سیستم را با Wake-on-LAN روشن کنید؟")
        if answer:
            wake_on_lan(SERVER_MAC_ADDRESS)
    except Exception as e:
        messagebox.showerror("خطا", str(e))

def send_shutdown():
    try:
        sock.sendall("shutdown".encode())
        reply = sock.recv(1024).decode()
        text_log.config(state='normal')
        text_log.insert(tk.END, "📴 پاسخ سرور: " + reply + "\n")
        text_log.config(state='disabled')
    except Exception as e:
        messagebox.showerror("خطا", str(e))

def exit_program():
    try:
        sock.close()
    except:
        pass
    root.destroy()


root = tk.Tk()
root.title("Remote Server Controller")
root.geometry("400x300")

tk.Label(root, text="👤 نام کاربری:").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="🔑 رمز عبور:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

button_connect = tk.Button(root, text="اتصال به سرور", command=connect_to_server)
button_connect.pack(pady=5)

button_shutdown = tk.Button(root, text="خاموش کردن سرور", command=send_shutdown, state='disabled')
button_shutdown.pack()

button_exit = tk.Button(root, text="خروج", command=exit_program, state='disabled')
button_exit.pack(pady=5)

text_log = tk.Text(root, height=8, state='disabled')
text_log.pack(fill='both', expand=True, padx=10, pady=10)

SERVER_MAC_ADDRESS = get_mac_address()

root.mainloop()
