import socket
import os
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext

HOST = '192.168.1.158'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

running = True 

def log_to_gui(msg):
    log_text.config(state='normal')
    log_text.insert(tk.END, msg + '\n')
    log_text.see(tk.END)
    log_text.config(state='disabled')

def server_loop():
    global running
    log_to_gui(" سرور در حال اجراست و منتظر اتصال...")
    while running:
        try:
            server_socket.settimeout(1.0)
            try:
                conn, addr = server_socket.accept()
            except socket.timeout:
                continue
            with conn:
                log_to_gui(f"📡 اتصال جدید از {addr}")
                try:
                    credentials = conn.recv(1024).decode()
                    username, password = credentials.split(',')
                except:
                    conn.sendall("❌ فرمت نادرست اطلاعات".encode())
                    continue

                if username == "administrator" and password == "adminADMIN123":
                    conn.sendall("✅ ورود موفقیت‌آمیز بود.".encode())
                    log_to_gui(f"✅ ورود موفقیت‌آمیز توسط {username}")

                    while running:
                        try:
                            command = conn.recv(1024).decode()
                            if not command:
                                break
                            if command == "shutdown":
                                conn.sendall("📴 سیستم در حال خاموش شدن است...".encode())
                                log_to_gui("📴 دستور خاموشی دریافت شد.")
                                os.system("shutdown /s /t 0")
                                break
                            else:
                                conn.sendall("❓ فرمان ناشناخته است.".encode())
                                log_to_gui(f"⚠️ فرمان ناشناخته: {command}")
                        except:
                            break
                else:
                    conn.sendall("🚫 نام کاربری یا رمز عبور اشتباه است.".encode())
                    log_to_gui("🚫 تلاش ناموفق برای ورود.")
        except Exception as e:
            log_to_gui(f"❌ خطا در سرور: {e}")
    log_to_gui("🛑 سرور متوقف شد.")

def stop_server():
    global running
    if messagebox.askokcancel("خروج", "آیا می‌خواهید سرور را متوقف کنید؟"):
        running = False
        server_socket.close()
        root.destroy()

root = tk.Tk()
root.title("کنترل سرور")
root.geometry("500x400")

label = tk.Label(root, text="سرور در حال اجراست...", font=("Arial", 14))
label.pack(pady=10)

log_text = scrolledtext.ScrolledText(root, height=15, state='disabled')
log_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

stop_button = tk.Button(root, text="قطع اتصال سرور", fg="red", command=stop_server)
stop_button.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", stop_server)

server_thread = threading.Thread(target=server_loop, daemon=True)
server_thread.start()

root.mainloop()
