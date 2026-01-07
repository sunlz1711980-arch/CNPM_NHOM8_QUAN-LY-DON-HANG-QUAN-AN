import os
from core import *

CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_logo():
    clear()
    print(CYAN + BOLD)
    print("====================================")
    print("  HỆ THỐNG QUẢN LÝ ĐƠN HÀNG QUÁN ĂN  ")
    print("====================================")
    print(RESET)

def main():
    while True:
        show_logo()
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("0. Thoát")
        c = input("Chọn: ")

        if c == "1":
            register()
            input("Enter để tiếp tục...")
        elif c == "2":
            if login():
                main_menu()
        elif c == "0":
            break

if __name__ == "__main__":
    main()
