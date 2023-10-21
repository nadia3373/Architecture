class CashProvider:
    _card: int
    _is_authorization: bool

    def __init__(self, card):
        self._card = card
        self._is_authorization = False

    def buy(self, price):
        """
        Купить билет.
        :param price: Цена билета
        :type price: double
        :return: True, если покупка прошла успешно, иначе False
        :rtype: bool
        """
        if self._is_authorization:
            print("Билет успешно куплен.")
            return True
        return False

    def authorization(self, customer) -> bool:
        """
        Авторизоваться.
        :param customer: Клиент, который пытается авторизоваться
        :type customer: Customer
        :return: True, если авторизация прошла успешно, иначе False
        :rtype: bool
        """
        self._is_authorization = True
        print("Пользователь успешно авторизован.")
        return True

    @property
    def is_authorization(self):
        return self._is_authorization
