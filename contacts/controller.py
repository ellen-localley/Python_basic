from contacts.model import Model
from contacts.service import Service

class Controller:
    def __init__(self):
        self.service = Service()

    def register(self, name, phone, email, addr):
        model = Model()
        model.name = name # _ 제거됨
        model.phone = phone
        model.email = email
        model.addr = addr
        self.service.add_contact(model)

    def search(self, name):
        self.service.get_contact(name)

    def list(self):
        self.service.get_contacts()

    def remove(self, name):
        self.service.del_contact(name)