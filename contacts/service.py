class Service:
    def __init__(self):
        self._contacts = []

    def add_contact(self, payload):
        self._contacts.append(payload)

    def get_contact(self, payload):
        self._contacts[payload]

    def get_contacts(self):
        self._contacts

    def del_contact(self, payload): # name
        pass