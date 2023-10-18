from fingerprint import Fingerprint

# initial
machine = Fingerprint('10.31.3.247', '80', '0')

# get machine status
print("Machine Status : "+machine.getStatus()) # connected | disconnected

# get all log data
# print(machine.getAttendance()) # return List of Attendance Log

# get all log data with date
# print(machine.getAttendance('all', '2023-10-15')) # return List of Attendance Log

# get all log data with date range
print(machine.getAttendance('all', '2023-10-16', '2023-10-17')) # return List of Attendance Log

# # get specific pin log data
# print(machine.getAttendance('1')) # return List of Attendance Log
# # OR List
# print(machine.getAttendance(['1', '2'])) # return List of Attendance Log

# # get exported json format
# user_attendance_data = machine.getAttendance()
# json_data = json.dumps(user_attendance_data, cls=UserAttendanceEncoder, indent=4)
# file_path = 'user_attendance2.json'
# with open(file_path, 'w') as file:
#     file.write(json_data)

# print(f"JSON data for user attendance saved to {file_path}")
