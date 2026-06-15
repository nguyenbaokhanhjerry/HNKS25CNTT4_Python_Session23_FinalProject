from datetime import datetime
def evaluate_flex_time(attendance_book):
    standard_limit = datetime.strptime("10:00", "%H:%M")
    for employee in attendance_book:
        employee_id = employee["id"]
        clock_in, clock_out = employee["times"]
        if clock_out is None:
            print(f"{employee_id} - Chưa đánh giá (đang làm việc).")
            continue
        in_time = datetime.strptime(clock_in, "%H:%M")
        out_time = datetime.strptime(clock_out, "%H:%M")
        if in_time > standard_limit:
            print(f"{employee_id} - Vi phạm: Đến muộn quá 90 phút.")
            continue
        working_hours = (out_time - in_time).total_seconds() / 3600
        if working_hours < 9:
            print(f"{employee_id} - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ.")
        else:
            print(f"{employee_id} - Hợp lệ: Hoàn thành ca làm việc.")
