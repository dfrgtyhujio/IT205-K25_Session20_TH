ticket_db = [
    {
        "ticket_id": "T01",
        "buyer_name": "Nguyen Van A",
        "price": 500.0,
        "status": "Booked",
        "seat": ("A", 1)
    },
    {
        "ticket_id": "T02",
        "buyer_name": "Tran Thi B",
        "price": 300.0,
        "status": "Cancelled",
        "seat": ("B", 5)
    },
    {
        "ticket_id": "T03",
        "buyer_name": "Le Van C",
        "price": 500.0,
        "status": "Booked",
        "seat": ("A", 2)
    }
]


def display_tickets(tickets):
    if not tickets:
        print("Hiện chưa có vé nào trong hệ thống.")
        return

    print("\n--- DANH SÁCH VÉ ---")
    print("Mã Vé | Tên Khách Hàng | Giá Vé | Chỗ Ngồi | Trạng Thái")
    print("-" * 70)

    for ticket in tickets:
        try:
            seat = f"{ticket['seat'][0]}-{ticket['seat'][1]}"

            status = ticket["status"]
            if status == "Cancelled":
                status += " [ĐÃ HỦY]"

            print(f"{ticket['ticket_id']:<5} | {ticket['buyer_name']:<18} | {ticket['price']:<7} | {seat:<8} | {status}")

        except KeyError:
            print("Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")

    print("-" * 70)


def input_price():
    while True:
        try:
            price = float(input("Nhập giá vé: "))

            if price <= 0:
                print("Giá vé phải lớn hơn 0. Vui lòng nhập lại.")
                continue

            return price

        except ValueError:
            print("Giá vé phải là số. Vui lòng nhập lại.")


def input_seat_number(message):
    while True:
        try:
            seat_number = int(input(message))

            if seat_number <= 0:
                print("Số ghế phải lớn hơn 0.")
                continue

            return seat_number

        except ValueError:
            print("Số ghế phải là số nguyên. Vui lòng nhập lại.")


def book_ticket(tickets):
    print("\n--- ĐẶT VÉ MỚI ---")

    ticket_id = input("Nhập mã vé: ").strip()

    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            print(f"Lỗi: Mã vé {ticket_id} đã tồn tại.")
            return

    buyer_name = input("Nhập tên khách hàng: ").strip()

    price = input_price()

    area = input("Nhập khu vực ghế: ").strip().upper()

    seat_number = input_seat_number("Nhập số ghế: ")

    new_ticket = {
        "ticket_id": ticket_id,
        "buyer_name": buyer_name,
        "price": price,
        "status": "Booked",
        "seat": (area, seat_number)
    }

    tickets.append(new_ticket)

    print(f"Thành công: Đã đặt vé {ticket_id} cho khách hàng {buyer_name}.")


def change_seat(tickets):
    print("\n--- ĐỔI CHỖ NGỒI ---")

    ticket_id = input("Nhập mã vé cần đổi chỗ: ").strip()

    for ticket in tickets:

        if ticket["ticket_id"] == ticket_id:

            new_area = input("Nhập khu vực ghế mới: ").strip().upper()

            new_seat = input_seat_number("Nhập số ghế mới: ")

            ticket["seat"] = (
                new_area,
                new_seat
            )

            print(f"Thành công: Đã đổi chỗ vé {ticket_id} sang {new_area}-{new_seat}.")
            return

    print(f"Không tìm thấy vé mang mã {ticket_id}.")


def cancel_ticket(tickets):
    print("\n--- HỦY VÉ ---")

    ticket_id = input("Nhập mã vé cần hủy: ").strip()

    for ticket in tickets:

        if ticket["ticket_id"] == ticket_id:

            if ticket["status"] == "Cancelled":
                print(f"Vé {ticket_id} đã ở trạng thái Cancelled trước đó.")
                return

            ticket["status"] = "Cancelled"

            print(f"Thành công: Vé {ticket_id} đã được hủy.")
            return

    print(f"Không tìm thấy vé mang mã {ticket_id}.")


def calculate_revenue(tickets):
    print("\n--- BÁO CÁO DOANH THU ---")

    revenue = 0
    booked_count = 0
    cancelled_count = 0

    for ticket in tickets:

        try:
            if ticket["status"] == "Booked":
                revenue += ticket["price"]
                booked_count += 1
            else:
                cancelled_count += 1

        except KeyError:
            print("Lỗi: Một vé đang bị thiếu dữ liệu doanh thu.")

    print(f"Tổng số vé đã đặt: {booked_count}")
    print(f"Tổng số vé đã hủy: {cancelled_count}")
    print(f"Tổng doanh thu hợp lệ: {revenue}")


def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===")
        print("1. Xem danh sách vé đã bán")
        print("2. Đặt vé mới")
        print("3. Đổi chỗ ngồi")
        print("4. Hủy vé")
        print("5. Báo cáo doanh thu")
        print("6. Thoát chương trình")
        print("========================================")


        choice = input(
            "Chọn chức năng (1-6): "
        ).strip()

        if choice == "1":
            display_tickets(ticket_db)

        elif choice == "2":
            book_ticket(ticket_db)

        elif choice == "3":
            change_seat(ticket_db)

        elif choice == "4":
            cancel_ticket(ticket_db)

        elif choice == "5":
            calculate_revenue(ticket_db)

        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()