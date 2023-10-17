from datetime import datetime
from mesin import Mesin

# Membuat objek Fingerprint dan menghubungkannya ke perangkat
# machine = Mesin.connect('10.31.3.247', 80, 123456)
machine = Mesin.connect(Mesin,'10.31.3.247', 80, 0)

# Mendapatkan status perangkat
print("Machine Status:", machine.get_status(Mesin))

# Mendapatkan data kehadiran untuk semua pegawai pada tanggal tertentu (misalnya, '2022-05-24')
attendance_data = machine.get_attendance(machine,'all', date_start='2023-10-17')
# print("Attendance Data:", attendance_data)

# Mendapatkan informasi pengguna
# user_info = machine.get_user_info()
# print("User Info:", user_info)
