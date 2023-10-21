from datetime import datetime

from cash_provider import CashProvider
from ticket import Ticket


class Customer:
    _id: int
    _ticket: list[Ticket]
    _cash: CashProvider

    def __init__(self, id, cash_provider):
        self._id = id
        self._tickets = []
        self._cash = cash_provider

    def authorize(self) -> bool:
        """
        Авторизация.
        :return: True, если авторизация прошла успешно, иначе False
        :rtype: bool
        """
        return self._cash.authorization(self)

    def buy_ticket(self, ticket: Ticket) -> bool:
        """
        Купить билет.
        :param ticket: Билет для покупки
        :type ticket: Ticket
        :return: True, если покупка прошла успешно, иначе False
        :rtype: bool
        """
        if self._cash.buy(ticket.price):
            self._tickets.append(ticket)
            return True
        return False

    def search_ticket(self, date: datetime) -> list[Ticket]:
        """
        Поиск билетов по дате мероприятия.
        :param date: Дата мероприятия
        :type date: datetime
        :return: Список найденных билетов
        :rtype: list of Ticket
        """
        return [ticket for ticket in self._tickets if ticket.date == date]

    @property
    def id(self):
        return self._id
