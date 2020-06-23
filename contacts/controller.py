from contacts.model import Model
from contacts.service import Service

class Controller:
    def __init__(self):
        self._service = Service()

    def register(self, name, phone, email, addr):
        model = Model()
        model.name = name # _ 제거됨
        model.phone = phone
        model.email = email
        model.addr = addr
        self._service.add_contact(model)

    def search(self):
        pass

    def list(self):
        pass

    def remove(self):
        pass