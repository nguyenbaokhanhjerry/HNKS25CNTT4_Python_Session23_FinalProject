from tabulate import tabulate
def display_records(attendance_book):
    table_data = []
    for employee in attendance_book:
        clock_in, clock_out = employee["times"]
        if clock_out is None:
            clock_out = "[Đang làm việc]"
        table_data.append([employee["id"], employee["name"], clock_in, clock_out])
    print(tabulate(
        table_data,
        headers=["Mã NV", "Tên Nhân Viên", "Giờ Vào", "Giờ Ra"],
        tablefmt="grid"
    ))
