from datetime import datetime

from cash_provider import CashProvider
from customer import Customer
from ticket import Ticket
from ticket_provider import TicketProvider

if __name__ == "__main__":
    customer = Customer(1, CashProvider(1234567890123456))
    ticket_provider = TicketProvider()

    ticket1 = Ticket(50.0, 1, 101, datetime(2023, 10, 15, 14, 0))
    ticket2 = Ticket(40.0, 2, 102, datetime(2023, 10, 16, 15, 0))

    ticket_provider.add_ticket(ticket1)
    ticket_provider.add_ticket(ticket2)

    customer.authorize()
    customer.buy_ticket(ticket1)
    ticket_provider.update_tickets(ticket1)

    found_tickets = customer.search_ticket(datetime(2023, 10, 15, 14, 0))

    for ticket in found_tickets:
        print(f"Билет покупателя {customer.id} на место {ticket.place}, дата {ticket.date}.")
