class Ticket:
    def __init__(self, price_ticket, place, root_number, date_time):
        self._price_ticket = price_ticket
        self._place = place
        self._root_number = root_number
        self._date_time = date_time
        self._is_valid = True

    @property
    def date(self):
        return self._date_time

    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, status):
        self._is_valid = status

    @property
    def number(self):
        return self._root_number

    @property
    def place(self):
        return self._place

    @property
    def price(self):
        return self._price_ticket
