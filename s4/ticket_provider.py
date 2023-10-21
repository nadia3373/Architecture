from ticket import Ticket


class TicketProvider:
    _tickets: {int, Ticket}

    def __init__(self):
        self._tickets = {}

    def update_tickets(self, ticket: Ticket) -> bool:
        """
        Обновляет статус билета (куплен/не куплен).
        :param ticket: Билет для обновления
        :type ticket: Ticket
        :return: True, если обновление прошло успешно, иначе False
        :rtype: bool
        """
        if ticket.number in self._tickets:
            self._tickets[ticket.number].is_valid = not self._tickets[ticket.number].is_valid
            return True
        return False

    def get_ticket(self, ticket_number) -> Ticket | None:
        """
        Поиск билета по номеру.
        :param rootNumber: Номер билета
        :type rootNumber: int
        :return: Найденный билет, если существует, иначе None
        :rtype: Ticket or None
        """
        return self._tickets.get(ticket_number, None)

    def add_ticket(self, ticket: Ticket) -> None:
        """
        Добавляет новый билет в словарь билетов.
        :param ticket: Билет для добавления
        :type ticket: Ticket
        """
        self._tickets[ticket.number] = ticket
