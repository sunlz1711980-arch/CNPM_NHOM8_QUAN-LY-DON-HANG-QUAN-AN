from datetime import datetime
import os
import json
DATA_FILE = "data.json"

# ================== DỮ LIỆU CHUNG ==================
users = []
current_user = None

menu_list = []
don_hang_list = []
ma_don_tu_tang = 1

ban_list = []
kho_nguyen_lieu = []
cong_thuc_mon = []
def load_data():
    global users, menu_list, don_hang_list, ma_don_tu_tang
    global ban_list, kho_nguyen_lieu

    if not os.path.exists(DATA_FILE):
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    users = data.get("users", [])

    # 🔧 FIX: thêm role mặc định nếu thiếu
    for u in users:
        if "role" not in u:
            u["role"] = "nhan_vien"  # hoặc "quan_ly"

    menu_list = data.get("menu_list", [])
    don_hang_list = data.get("don_hang_list", [])
    ma_don_tu_tang = data.get("ma_don_tu_tang", 1)
    ban_list = data.get("ban_list", [])
    kho_nguyen_lieu = data.get("kho_nguyen_lieu", [])   

def save_data():
    data = {
        "users": users,
        "menu_list": menu_list,
        "don_hang_list": don_hang_list,
        "ma_don_tu_tang": ma_don_tu_tang,
        "ban_list": ban_list,
        "kho_nguyen_lieu": kho_nguyen_lieu
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

 # ===== MÀU ANSI =====
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def pause():
    input("\nNhấn Enter để tiếp tục...")

def hien_thi_chao_mung():
    PINK = "\033[95m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    print()
    print(f"{PINK}{BOLD}💖  CHÀO MỪNG ĐẾN VỚI QUÁN ĂN  💖{RESET}".center(70))
    print()
    print(f"{YELLOW}{BOLD}  ███████╗██╗██╗   ██╗{RESET}".center(70))
    print(f"{YELLOW}{BOLD}  ██╔════╝██║██║   ██║{RESET}".center(70))
    print(f"{YELLOW}{BOLD}  ███████╗██║██║   ██║{RESET}".center(70))
    print(f"{YELLOW}{BOLD}  ╚════██║██║██║   ██║{RESET}".center(70))
    print(f"{YELLOW}{BOLD}  ███████║██║╚██████╔╝{RESET}".center(70))
    print(f"{YELLOW}{BOLD}  ╚══════╝╚═╝ ╚═════╝ {RESET}".center(70))

    print("\n" + "-" * 70)
    print(f"{GREEN}{BOLD}👏  HỆ THỐNG QUẢN LÝ ĐƠN HÀNG  👏{RESET}".center(70))
    print(f"{YELLOW}{BOLD}✨  MENU CHÍNH  ✨{RESET}".center(70))
    print()

    print("  1. 🔐 Đăng nhập")
    print("  2. 📝 Đăng ký")
    print("  3. ❓ Quên mật khẩu")
    print("  4. 🚪 Thoát")
    print()
def nhap_lua_chon(hop_le):
    """
    hop_le: list các lựa chọn hợp lệ, ví dụ ["1","2","3","0"]
    """
    while True:
        chon = input("👉 Chọn chức năng: ").strip()
        if chon not in hop_le:
            print("❌ Lựa chọn không hợp lệ! Vui lòng nhập đúng chức năng.")
            continue
        return chon
    
# ================== ĐĂNG KÝ / ĐĂNG NHẬP ==================
def register():
    while True:
        username = input("Tên đăng ký: ").strip()
        if username == "":
            print("❌ Tên đăng nhập không được để trống!")
            continue

        if any(u["username"] == username for u in users):
            print("❌ Username đã tồn tại!")
            continue
        break

    while True:
        password = input("Mật khẩu: ").strip()
        if password == "":
            print("❌ Mật khẩu không được để trống!")
            continue

        confirm = input("Nhập lại mật khẩu: ").strip()
        if confirm != password:
            print("❌ Mật khẩu không khớp!")
            continue
        break

    while True:
        print("Chọn loại tài khoản:")
        print("1. Quản lý")
        print("2. Nhân viên")
        role = input("Lựa chọn: ").strip()

        if role == "1":
            role = "quan_ly"
            break
        elif role == "2":
            role = "nhan_vien"
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

    users.append({
        "username": username,
        "password": password,
        "role": role
    })

    save_data()
    print("✅ Đăng ký thành công!")

def menu_quan_ly():
    while True:
        clear_screen()
        print("=== MENU QUẢN LÝ ===")
        print("1. Báo cáo")
        print("0. Đăng xuất")

        c = nhap_lua_chon(["1", "0"])

        if c == "1":
            menu_bao_cao()

        elif c == "0":
            logout()
            break

def menu_nhan_vien():
    while True:
        clear_screen()
        print("=== MENU NHÂN VIÊN ===")
        print("1. Món ăn")
        print("2. Đơn hàng")
        print("3. Bàn")
        print("4. Kho")
        print("5. Thanh toán")
        print("0. Đăng xuất")

        c = nhap_lua_chon(["1","2","3","4","5","0"])

        if c == "1":
            menu_quan_ly_menu()

        elif c == "2":
            menu_quan_ly_don_hang()

        elif c == "3":
            menu_quan_ly_ban()

        elif c == "4":
            menu_quan_ly_kho()

        elif c == "5":
            menu_thanh_toan()

        elif c == "0":
            logout()
            break


def login():
    global current_user

    if not users:
        print("❌ Chưa có tài khoản nào được đăng ký!")
        input("\nNhấn Enter để quay lại...")
        return False

    while True:
        username = input("Tên đăng nhập: ").strip()
        if username == "":
            print("❌ Tên đăng nhập không được để trống!")
            continue

        user_found = next((u for u in users if u["username"] == username), None)
        if not user_found:
            print("❌ Tài khoản không tồn tại!")
            continue
        break

    while True:
        password = input("Mật khẩu: ").strip()
        if password == "":
            print("❌ Mật khẩu không được để trống!")
            continue

        if password != user_found["password"]:
            print("❌ Sai mật khẩu!")
            continue
        break

    current_user = user_found
    print(f"✅ Xin chào {username}")

    if current_user["role"] == "quan_ly":
        print("🔑 Quyền: Quản lý")
    else:
        print("👷 Quyền: Nhân viên")

    return True



def quen_mat_khau():
    print("=== QUÊN MẬT KHẨU ===")
    username = input("Nhập tên đăng nhập: ")

    for u in users:
        if u["username"] == username:
            while True:
                mk_moi = input("Nhập mật khẩu mới: ")
                mk_xac_nhan = input("Xác nhận mật khẩu mới: ")

                if mk_moi == mk_xac_nhan:
                    u["password"] = mk_moi
                    print("✅ Đổi mật khẩu thành công!")
                    return
                else:
                    print("❌ Mật khẩu không khớp, thử lại!")

    print("❌ Không tìm thấy tài khoản!")

def logout():
    global current_user
    current_user = None
    print("👋 Đã đăng xuất")

# ================== QUẢN LÝ MENU ==================
def tim_mon_theo_id(id_mon):
    return next((m for m in menu_list if m["id"] == id_mon), None)
def sua_mon_an():
    hien_thi_menu(menu_list)

    try:
        id_mon = int(input("Nhập ID món cần sửa: "))
    except:
        print("❌ ID phải là số!")
        return

    mon = tim_mon_theo_id(id_mon)
    if not mon:
        print("❌ Không tìm thấy món!")
        return

    print("\n🔧 ĐỂ TRỐNG NẾU KHÔNG MUỐN SỬA")

    ten_moi = input(f"Tên món ({mon['ten_mon']}): ").strip()
    if ten_moi:
        mon["ten_mon"] = ten_moi

    gia_moi = input(f"Giá ({mon['gia']}): ").strip()
    if gia_moi:
        try:
            mon["gia"] = int(gia_moi)
        except:
            print("⚠️ Giá không hợp lệ, giữ nguyên!")

    loai_moi = input(f"Loại ({mon['loai']}): ").strip()
    if loai_moi:
        mon["loai"] = loai_moi

    print("Trạng thái:")
    print("1. Còn hàng")
    print("2. Hết hàng")
    tt = input("Chọn (Enter để giữ nguyên): ").strip()
    if tt == "1":
        mon["trang_thai"] = "Còn hàng"
    elif tt == "2":
        mon["trang_thai"] = "Hết hàng"

    save_data()
    print("✅ Cập nhật món ăn thành công!")
def xoa_mon_an():
    hien_thi_menu(menu_list)

    try:
        id_mon = int(input("Nhập ID món cần xóa: "))
    except:
        print("❌ ID phải là số!")
        return

    mon = tim_mon_theo_id(id_mon)
    if not mon:
        print("❌ Không tìm thấy món!")
        return

    confirm = input(f"⚠️ Bạn chắc chắn muốn xóa '{mon['ten_mon']}'? (y/n): ")
    if confirm.lower() == "y":
        menu_list.remove(mon)
        save_data()
        print("✅ Đã xóa món ăn!")
    else:
        print("❎ Hủy xóa.")

def add_item():
    print("\n--- THÊM MÓN ĂN MỚI ---")
    ten_mon = input("Nhập tên món: ")
    gia = int(input("Nhập giá: "))
    loai = input("Nhập loại món: ")
    mon_moi = {
        "id": len(menu_list) + 1,
        "ten_mon": ten_mon,
        "gia": gia,
        "loai": loai,
        "trang_thai": "Còn hàng",
    }
    menu_list.append(mon_moi)
    save_data()

    print("✅ Thêm món thành công!")

def hien_thi_menu(danh_sach):
    if not danh_sach:
        print("Danh sách hiện đang trống.")
        return
    print("=" * 80)
    print(f"{'ID':<5} {'Tên món':<25} {'Giá':<10} {'Loại':<15} {'Trạng thái':<20}")
    print("-" * 80)
    for mon in danh_sach:
        print(f"{mon['id']:<5} {mon['ten_mon']:<25} {mon['gia']:<10} {mon['loai']:<15} {mon['trang_thai']:<20}")
    print("=" * 80)

def menu_quan_ly_menu():
    while True:
        clear_screen()
        print("===== QUẢN LÝ MENU =====")
        print("1. Thêm món")
        print("2. Xem danh sách menu")
        print("3. Tìm kiếm món")
        print("4. Sửa món ăn")
        print("5. Xóa món ăn")
        print("0. Quay lại")

        chon = nhap_lua_chon(["1","2","3","4","5","0"])

        if chon == "1":
            clear_screen()
            print("=== THÊM MÓN ĂN ===")
            add_item()
            pause()

        elif chon == "2":
            clear_screen()
            print("=== DANH SÁCH MENU ===")
            hien_thi_menu(menu_list)
            pause()

        elif chon == "3":
            clear_screen()
            print("=== TÌM KIẾM MÓN ===")
            tk = input("Nhập tên món: ").lower()
            kq = [m for m in menu_list if tk in m['ten_mon'].lower()]
            hien_thi_menu(kq)
            pause()

        elif chon == "4":
            clear_screen()
            print("=== SỬA MÓN ĂN ===")
            sua_mon_an()
            pause()

        elif chon == "5":
            clear_screen()
            print("=== XÓA MÓN ĂN ===")
            xoa_mon_an()
            pause()

        elif chon == "0":
            break



# ================== QUẢN LÝ ĐƠN HÀNG ==================
def tao_don_hang():
    global ma_don_tu_tang
    hien_thi_menu(menu_list)

    danh_sach_chon = []
    tong_tien = 0

    while True:
        id_mon = input("Nhập ID món muốn đặt (hoặc '0' để kết thúc): ").strip()
        if id_mon == "0":
            break

        if not id_mon.isdigit():
            print("❌ ID phải là số!")
            continue

        mon_tim_thay = next((m for m in menu_list if m["id"] == int(id_mon)), None)
        if not mon_tim_thay:
            print("❌ ID món không tồn tại!")
            continue

        # 🔗 LIÊN KẾT KHO
        kho_mon = lay_so_luong_ton(mon_tim_thay["ten_mon"])
        if not kho_mon or kho_mon["so_luong"] <= 0:
            print("❌ Món này đã hết hàng, vui lòng chọn món khác!")
            continue

        print(f"📦 Số lượng còn trong kho: {kho_mon['so_luong']}")

        try:
            sl = int(input(f"Số lượng cho món {mon_tim_thay['ten_mon']}: "))
        except:
            print("❌ Số lượng phải là số!")
            continue

        if sl <= 0:
            print("❌ Số lượng phải lớn hơn 0!")
            continue

        if sl > kho_mon["so_luong"]:
            print(f"❌ Không đủ hàng! Chỉ còn {kho_mon['so_luong']} phần.")
            continue

        # ✅ TRỪ KHO
        kho_mon["so_luong"] -= sl

        danh_sach_chon.append({
            "ten_mon": mon_tim_thay["ten_mon"],
            "gia": mon_tim_thay["gia"],
            "so_luong": sl
        })

        tong_tien += mon_tim_thay["gia"] * sl
        print(f"✅ Đã thêm {sl} x {mon_tim_thay['ten_mon']}")

    if danh_sach_chon:
        bay_gio = datetime.now()
        don_moi = {
            "ma_don": ma_don_tu_tang,
            "danh_sach_mon": danh_sach_chon,
            "tong_tien": tong_tien,
            "ngay": bay_gio.strftime("%Y-%m-%d"),
            "thang": bay_gio.strftime("%Y-%m"),
            "trang_thai": "Chưa thanh toán"
        }

        don_hang_list.append(don_moi)
        print(f"✅ Tạo đơn thành công! Mã đơn: {ma_don_tu_tang}")
        ma_don_tu_tang += 1
        save_data()
    else:
        print("⚠️ Đơn hàng trống.")

def huy_don_hang():
    try:
        ma_don = int(input("Nhập mã đơn cần hủy: "))
    except:
        print("❌ Mã đơn không hợp lệ!")
        return

    don = next((d for d in don_hang_list if d["ma_don"] == ma_don), None)
    if not don:
        print("❌ Không tìm thấy đơn hàng!")
        return

    if don["trang_thai"] == "Hoàn thành":
        print("❌ Đơn hàng đã thanh toán, không thể hủy!")
        return
    confirm = input(f"⚠️ Bạn có chắc muốn hủy đơn {ma_don}? (y/n): ").lower()
    if confirm != "y":
        print("❎ Đã hủy thao tác.")
        return
    if don["trang_thai"] == "Đã hủy":
        print("⚠️ Đơn hàng này đã bị hủy trước đó!")
        return

    # 🔄 HOÀN TRẢ KHO
    for item in don["danh_sach_mon"]:
        kho = lay_so_luong_ton(item["ten_mon"])
        if kho:
            kho["so_luong"] += item["so_luong"]
        else:
            kho_nguyen_lieu.append({
                "ten": item["ten_mon"].lower(),
                "so_luong": item["so_luong"]
            })

    # 🔓 GIẢI PHÓNG BÀN NẾU CÓ
    for ban in ban_list:
        if ban["ma_don"] == ma_don:
            ban["trang_thai"] = "Trống"
            ban["ma_don"] = None

    don["trang_thai"] = "Đã hủy"
    save_data()
    print(f"✅ Đã hủy thành công đơn hàng mã {ma_don}")

def menu_quan_ly_don_hang():
    while True:
        clear_screen()
        print("=== QUẢN LÝ ĐƠN HÀNG ===")
        print("1. Tạo đơn mới")
        print("2. Xem danh sách đơn")
        print("3. Hủy đơn hàng")
        print("0. Quay lại")

        c = nhap_lua_chon(["1","2","3","0"])

        if c == "1":
            clear_screen()
            print("=== TẠO ĐƠN HÀNG ===")
            tao_don_hang()
            pause()

        elif c == "2":
            clear_screen()
            print("=== DANH SÁCH ĐƠN ===")
            for d in don_hang_list:
                print(
                    f"Mã: {d['ma_don']} | Tổng: {d['tong_tien']} | Trạng thái: {d['trang_thai']}"
                )
            pause()

        elif c == "3":
            clear_screen()
            print("=== HỦY ĐƠN HÀNG ===")
            huy_don_hang()
            pause()

        elif c == "0":
            break


# ================== QUẢN LÝ BÀN ==================
def khoi_tao_ban():
    so = int(input("Số lượng bàn muốn tạo: "))
    ban_list.clear()
    for i in range(1, so+1):
        ban_list.append({"ma_ban": i, "trang_thai": "Trống", "ma_don": None})
    print(f"✅ Đã khởi tạo {so} bàn.")
    save_data()

def gan_don_vao_ban():
    try:
        ma_don = int(input("Nhập Mã đơn hàng: "))
        ma_ban = int(input("Nhập Số bàn: "))
        for ban in ban_list:
            if ban["ma_ban"] == ma_ban:
                if ban["trang_thai"] == "Trống":
                    ban["trang_thai"] = "Có khách"
                    ban["ma_don"] = ma_don
                    print(f"✅ Đã gán đơn {ma_don} vào bàn {ma_ban}")
                else:
                    print("❌ Bàn này đang có khách!")
                return
        print("❌ Không tìm thấy bàn!")
    except: print("❌ Vui lòng nhập số!")
    save_data()

def menu_quan_ly_ban():
    while True:
        clear_screen()
        print("=== QUẢN LÝ BÀN ===")
        print("1. Khởi tạo sơ đồ bàn")
        print("2. Gán đơn vào bàn")
        print("3. Xem danh sách bàn")
        print("0. Quay lại")

        c = nhap_lua_chon(["1", "2", "3", "0"])

        if c == "1":
            clear_screen()
            print("=== KHỞI TẠO SƠ ĐỒ BÀN ===")
            khoi_tao_ban()
            pause()

        elif c == "2":
            clear_screen()
            print("=== GÁN ĐƠN VÀO BÀN ===")
            gan_don_vao_ban()
            pause()

        elif c == "3":
            clear_screen()
            print("=== DANH SÁCH BÀN ===")
            if not ban_list:
                print("⚠️ Chưa có bàn nào!")
            else:
                for b in ban_list:
                    print(f"Bàn {b['ma_ban']} | {b['trang_thai']} | Mã đơn: {b['ma_don']}")
            pause()

        elif c == "0":
            break



# ================== QUẢN LÝ KHO ==================
def nhap_kho():
    ten = input("Nguyên liệu: ").lower()
    sl = int(input("Số lượng: "))
    for nl in kho_nguyen_lieu:
        if nl["ten"] == ten:
            nl["so_luong"] += sl
            return
    kho_nguyen_lieu.append({"ten": ten, "so_luong": sl})
    save_data()
def lay_so_luong_ton(ten_mon):
    for nl in kho_nguyen_lieu:
        if nl["ten"] == ten_mon.lower():
            return nl
    return None

def menu_quan_ly_kho():
    while True:
        clear_screen()
        print("=== QUẢN LÝ KHO ===")
        print("1. Nhập kho")
        print("2. Xem tồn kho")
        print("0. Quay lại")

        c = nhap_lua_chon(["1","2","0"])

        if c == "1":
            clear_screen()
            print("=== NHẬP KHO ===")
            nhap_kho()
            pause()

        elif c == "2":
            clear_screen()
            print("=== TỒN KHO ===")
            for nl in kho_nguyen_lieu:
                print(f"Nguyên liệu: {nl['ten']} | Tồn: {int(nl['so_luong'])}")
            pause()

        elif c == "0":
            break


# ================== THANH TOÁN ==================
def thanh_toan_theo_ban():
    try:
        so_ban = int(input("Nhập số bàn: "))
    except:
        print("❌ Số bàn không hợp lệ!")
        return

    ban = next((b for b in ban_list if b["ma_ban"] == so_ban), None)
    if not ban or not ban["ma_don"]:
        print("❌ Bàn không có đơn hàng!")
        return

    don = next((d for d in don_hang_list if d["ma_don"] == ban["ma_don"]), None)
    if not don:
        print("❌ Không tìm thấy đơn hàng!")
        return

    hien_thi_hoa_don(don)

    if xac_nhan_thanh_toan():
        cap_nhat_thanh_toan(don, ban)
def thanh_toan_theo_ma_don():
    try:
        ma_don = int(input("Nhập mã đơn: "))
    except:
        print("❌ Mã đơn không hợp lệ!")
        return

    don = next((d for d in don_hang_list if d["ma_don"] == ma_don), None)
    if not don:
        print("❌ Không tìm thấy đơn hàng!")
        return

    ban = next((b for b in ban_list if b["ma_don"] == ma_don), None)

    hien_thi_hoa_don(don)

    if xac_nhan_thanh_toan():
        cap_nhat_thanh_toan(don, ban)
def hien_thi_hoa_don(don):
    print("\n" + "="*30)
    print(f"HÓA ĐƠN MÃ: {don['ma_don']}")
    for item in don["danh_sach_mon"]:
        print(f"{item['ten_mon']:<15} x{item['so_luong']} {item['gia']*item['so_luong']}")
    print(f"TỔNG CỘNG: {don['tong_tien']}")
    print("="*30)
def xac_nhan_thanh_toan():
    return input("Xác nhận thanh toán? (y/n): ").lower() == "y"
def cap_nhat_thanh_toan(don, ban=None):
    while True:
        ngay = input("Nhập ngày (DD): ").strip()
        thang = input("Nhập tháng (MM): ").strip()
        nam = input("Nhập năm (YYYY): ").strip()

        if not (ngay.isdigit() and thang.isdigit() and nam.isdigit()):
            print("❌ Ngày tháng năm phải là số!")
            continue

        if not (1 <= int(ngay) <= 31 and 1 <= int(thang) <= 12):
            print("❌ Ngày hoặc tháng không hợp lệ!")
            continue

        break

    don["trang_thai"] = "Hoàn thành"
    don["ngay"] = f"{nam}-{thang.zfill(2)}-{ngay.zfill(2)}"
    don["thang"] = f"{nam}-{thang.zfill(2)}"
    don["nam"] = nam

    if ban:
        ban["trang_thai"] = "Trống"
        ban["ma_don"] = None

    save_data()
    print("✅ Thanh toán hoàn tất!")
def menu_thanh_toan():
    while True:
        clear_screen()
        print("=== THANH TOÁN ===")
        print("1. Thanh toán theo số bàn")
        print("2. Thanh toán theo mã đơn")
        print("0. Quay lại")

        c = nhap_lua_chon(["1", "2", "0"])

        if c == "1":
            clear_screen()
            print("=== THANH TOÁN THEO SỐ BÀN ===")
            thanh_toan_theo_ban()
            pause()

        elif c == "2":
            clear_screen()
            print("=== THANH TOÁN THEO MÃ ĐƠN ===")
            thanh_toan_theo_ma_don()
            pause()

        elif c == "0":
            break


# ================== BÁO CÁO ==================
def menu_bao_cao():
    while True:
        clear_screen()
        print("=== BÁO CÁO DOANH THU ===")
        print("1. Báo cáo theo ngày")
        print("2. Báo cáo theo tháng")
        print("0. Quay lại")

        c = nhap_lua_chon(["1","2","0"])

        if c == "1":
            clear_screen()
            print("=== BÁO CÁO THEO NGÀY ===")

            ngay = input("Nhập ngày (DD): ").zfill(2)
            thang = input("Nhập tháng (MM): ").zfill(2)
            nam = input("Nhập năm (YYYY): ")

            key_ngay = f"{nam}-{thang}-{ngay}"

            tong = sum(
                d["tong_tien"]
                for d in don_hang_list
                if d.get("ngay") == key_ngay and d["trang_thai"] == "Hoàn thành"
            )

            print(f"\n💰 Doanh thu ngày {key_ngay}: {tong}")
            pause()

        elif c == "2":
            clear_screen()
            print("=== BÁO CÁO THEO THÁNG ===")

            thang = input("Nhập tháng (MM): ").zfill(2)
            nam = input("Nhập năm (YYYY): ")

            key_thang = f"{nam}-{thang}"

            tong = sum(
                d["tong_tien"]
                for d in don_hang_list
                if d.get("thang") == key_thang and d["trang_thai"] == "Hoàn thành"
            )

            print(f"\n💰 Doanh thu tháng {key_thang}: {tong}")
            pause()

        elif c == "0":
            break

# ================== HỆ THỐNG CHÍNH ==================
def main_menu():
    while True:
        print("\n" + "★"*10 + " MENU QUẢN LÝ " + "★"*10)
        print("1. Món ăn\n2. Đơn hàng\n3. Bàn\n4. Kho\n5. Thanh toán\n6. Báo cáo\n7. Đăng xuất")
        c = nhap_lua_chon(["1","2","3","4","5","6","7"])
        if c == "1":
            clear_screen()
            menu_quan_ly_menu()

        elif c == "2":
            clear_screen()
            menu_quan_ly_don_hang()

        elif c == "3":
            clear_screen()
            menu_quan_ly_ban()

        elif c == "4":
            clear_screen()
            menu_quan_ly_kho()

        elif c == "5":
            clear_screen()
            menu_thanh_toan()
            pause()

        elif c == "6":
            clear_screen()
            menu_bao_cao()
            pause()
def main():
    load_data()
    while True:
        clear_screen()
        hien_thi_chao_mung()   

        chon = nhap_lua_chon(["1", "2", "3", "4"])


        if chon == "1":  # Đăng nhập
            clear_screen()
            print("=== ĐĂNG NHẬP TÀI KHOẢN ===")
            if login():
                if current_user["role"] == "quan_ly":
                    menu_quan_ly()
                else:
                    menu_nhan_vien()


        elif chon == "2":  # Đăng ký
            clear_screen()
            print("=== ĐĂNG KÝ TÀI KHOẢN ===")
            register()
            input("\nNhấn Enter để quay lại...")

        elif chon == "3":
            clear_screen()
            quen_mat_khau()
            input("\nNhấn Enter để quay lại...")


        elif chon == "4":
            print("👋 Tạm biệt!")
            break

        else:
            print("❌ Lựa chọn không hợp lệ!")
            input("Nhấn Enter để tiếp tục...")



if __name__ == "__main__":
    main()
