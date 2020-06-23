class Service:
    def __init__(self):
        self._contacts = []

    def add_contact(self, payload):
        self._contacts.append(payload)

    def get_contact(self, payload):
        for i in self._contacts:
            if payload == i.name:
                return i

    def get_contacts(self):
        return self._contacts

    def del_contact(self, payload): # name
        for i in self._contacts:
            if payload == i.name:
                self._contacts.remove(i)