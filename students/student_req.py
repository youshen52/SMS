class StudentReq:
    def __init__(self, admin_no, request):
        self._admin_no = admin_no
        self._request = request

    @property
    def admin_no(self):
        return self._admin_no

    @property
    def request(self):
        return self._request

    @admin_no.setter
    def admin_no(self, value):
        self._admin_no = value

    @request.setter
    def request(self, value):
        self._request = value
