from datetime import timedelta
import socket

class Mesin:
    def __init__(self):
        self.conn = None
        self.ip = None
        self.port = None
        self.comkey = None
        self.is_connected = False
        self.NL = "\r\n"

    payload = {
        'GetAttLog': '<GetAttLog><ArgComKey xsi:type="xsd:integer">#COMKEY</ArgComKey>#PIN</GetAttLog>',
        'GetUserInfo': '<GetUserInfo><ArgComKey xsi:type="xsd:integer">#COMKEY</ArgComKey>#PIN</GetUserInfo>'
    }

    def connect(self, ip, port=80, comkey=0):
        self.ip = ip
        self.port = port
        self.comkey = comkey

        try:
            self.conn = socket.create_connection((self.ip, self.port), timeout=1)
            self.is_connected = True
        except Exception as e:
            self.is_connected = False

        return self

    def get_status(self):
        return 'connected' if self.is_connected else 'disconnected'

    def get_user_info(self, pin='all'):
        payload = self.payload['GetUserInfo']

        # self.connect(self.ip, self.port, self.comkey)

        if isinstance(pin, list):
            pin_payload = ""
            for value in pin:
                pin_payload += f"<Arg><PIN>{value}</PIN></Arg>"
            pin = pin_payload
        else:
            pin = f"<Arg><PIN>{pin}</PIN></Arg>"

        payload = payload.replace("#PIN", pin)

        self.generate_request(self,payload)

        buffer = ""
        is_start_now = False
        while True:
            res = self.conn.recv(1024).decode('utf-8')
            if not res:
                break
            if "<GetUserInfoResponse>" in res:
                is_start_now = True
            if is_start_now:
                buffer += res

        ga_res = ["<GetUserInfoResponse>", "</GetUserInfoResponse>", "\r\n"]
        buffer = buffer.replace(ga_res[0], "").replace(ga_res[1], "").replace(ga_res[2], "")

        self.conn.close()
        return self.parse_user_info_data(buffer)

    @staticmethod
    def parse_user_info_data(data=""):
        data_row = data.split("<Row>")
        data_row.pop(0)

        user_data = []

        for value in data_row:
            end_row = value.split("</Row>")[0]

            fid = Mesin.get_value_from_tag(end_row, "<PIN>", "</PIN>")
            name = Mesin.get_value_from_tag(end_row, "<Name>", "</Name>")
            password = Mesin.get_value_from_tag(end_row, "<Password>", "</Password>")
            group = Mesin.get_value_from_tag(end_row, "<Group>", "</Group>")
            privilege = Mesin.get_value_from_tag(end_row, "<Privilege>", "</Privilege>")
            card = Mesin.get_value_from_tag(end_row, "<Card>", "</Card>")
            pin2 = Mesin.get_value_from_tag(end_row, "<PIN2>", "</PIN2>")

            user_data.append({
                'pin': fid,
                'name': name,
                'password': password,
                'group': group,
                'privilege': privilege,
                'card': card,
                'pin2': pin2
            })

        return user_data

    def get_attendance(self, pin='all', date_start=None, date_end=None):
        if date_start and not date_end:
            date_end = date_start

        payload = self.payload['GetAttLog']

        print("ip ===",self.ip)
        # self.connect(self.ip, self.port, self.comkey)

        if isinstance(pin, list):
            pin_payload = ""
            for value in pin:
                pin_payload += f"<Arg><PIN>{value}</PIN></Arg>"
            pin = pin_payload
        else:
            pin = f"<Arg><PIN>{pin}</PIN></Arg>"

        payload = payload.replace("#PIN", pin)

        self.generate_request(self,payload)


        buffer = ""
        is_start_now = False
        while True:
            print("recv ", self.conn)
            res = self.conn.recv(1024).decode('utf-8')
            if not res:
                break
            if "<GetAttLogResponse>" in res:
                is_start_now = True
            if is_start_now:
                buffer += res

        ga_res = ["<GetAttLogResponse>", "</GetAttLogResponse>", "\r\n"]
        buffer = buffer.replace(ga_res[0], "").replace(ga_res[1], "").replace(ga_res[2], "")

        self.conn.close()
        return self.parse_attendance_data(buffer, date_start, date_end)

    @staticmethod
    def parse_attendance_data(data="", date_start=None, date_end=None):
        data_row = data.split("<Row>")
        data_row.pop(0)

        finger_data = []

        for value in data_row:
            end_row = value.split("</Row>")[0]

            fid = Mesin.get_value_from_tag(end_row, "<PIN>", "</PIN>")
            datetime = Mesin.get_value_from_tag(end_row, "<DateTime>", "</DateTime>")
            verified = Mesin.get_value_from_tag(end_row, "<Verified>", "</Verified>")
            status = Mesin.get_value_from_tag(end_row, "<Status>", "</Status>")
            workcode = Mesin.get_value_from_tag(end_row, "<WorkCode>", "</WorkCode>")

            if date_start and date_end:
                range_date = Mesin.date_range(date_start, date_end)
                date_check = datetime.split(' ')[0]

                if date_check in range_date:
                    finger_data.append({
                        'pin': fid,
                        'datetime': datetime,
                        'verified': verified,
                        'status': status,
                        'workcode': workcode
                    })

            else:
                finger_data.append({
                    'pin': fid,
                    'datetime': datetime,
                    'verified': verified,
                    'status': status,
                    'workcode': workcode
                })

        return finger_data

    @staticmethod
    def get_value_from_tag(a, b, c):
        a = " " + a
        hasil = ""
        awal = a.find(b)
        if awal != -1:
            akhir = a[awal:].find(c)
            if akhir != -1:
                hasil = a[awal + len(b): awal + akhir]
        return hasil

    @staticmethod
    def date_range(start_date, end_date):
        date_range = []
        for n in range(int((end_date - start_date).days) + 1):
            date_range.append((start_date + timedelta(n)).strftime('%Y-%m-%d'))
        return date_range

    def generate_request(self, payload):
        payload = payload.replace("#COMKEY", str(self.comkey))
        request = "POST /iWsService HTTP/1.0{self.NL}Content-Type: text/xml{self.NL}Content-Length: {len(payload)}{self.NL}{self.NL}{payload}{self.NL}"
        self.conn.sendall(request.encode('utf-8'))

    def __getattr__(self, name):
        return getattr(self, name)

    @staticmethod
    def __call_static(method, *args):
        return getattr(Mesin(), method)(*args)
