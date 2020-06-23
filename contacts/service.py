class Service:
    def __init__(self):
        self._contacts = []

    def add_contact(self, payload):
        self._contacts.append(payload)

    def get_contact(self, payload):
        for i in self._contacts:
            if(payload == i.name):
                print(i)

    def get_contacts(self):
        for i in self._contacts:
            print(i)

    def del_contact(self, payload): # name
        cnt = 0
        for i in self._contacts:
            if(payload == i.name):
                del self._contacts[cnt]
            cnt += 1