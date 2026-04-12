# ========================================
# Szkielet pliku: product.py
# Uzupelnij implementacje!
# ========================================

class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        if not isinstance(name, str) or not name:
            raise ValueError("name must be a non-empty string")
        if price < 0:
            raise ValueError("price must be >= 0")
        if quantity < 0:
            raise ValueError("quantity must be >= 0")

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def add_stock(self, amount: int):
        # TODO: Dodaj ilosc do magazynu. Rzuc ValueError jesli amount < 0
        if amount < 0:
            raise ValueError('ilosc nie moze byc ujemna')
        self.quantity += amount


    def remove_stock(self, amount: int):
        # TODO: Usun ilosc z magazynu.
        # Rzuc ValueError jesli amount < 0 lub amount > quantity
        if amount < 0 or amount > self.quantity:
            raise ValueError("nie mozna usunac zle wartosci")
        self.quantity -= amount

    def is_available(self) -> bool:
        # TODO: Zwroc True jesli quantity > 0
        return self.quantity > 0

    def total_value(self) -> float:
        # TODO: Zwroc price * quantity
        return self.price * self.quantity