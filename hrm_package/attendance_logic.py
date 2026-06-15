def clock_in(attendance_book):
    employee_id = input("Nhập mã nhân viên: ").strip()

    for employee in attendance_book:
        if employee["id"] == employee_id:
            print("Lỗi: Mã nhân viên đã tồn tại.")
            return

    name = input("Nhập tên nhân viên: ").strip()
    time_in = input("Nhập giờ vào (HH:MM): ").strip()

    attendance_book.append({
        "id": employee_id,
        "name": name,
        "times": (time_in, None)
    })

    print(f"Thành công: Đã ghi nhận {employee_id} chấm công vào lúc {time_in}!")

def clock_out(attendance_book):
    employee_id = input("Nhập mã nhân viên: ").strip()
    time_out = input("Nhập giờ ra (HH:MM): ").strip()

    for employee in attendance_book:
        if employee["id"] == employee_id:
            old_time_in, _ = employee["times"]
            employee["times"] = (old_time_in, time_out)
            print(f"Thành công: {employee_id} đã chấm công ra lúc {time_out}!")
            return

    print("Không tìm thấy nhân viên.")
