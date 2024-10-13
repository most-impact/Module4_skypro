from abc import ABC


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


class MixinLog:
    def __init__(self, *args):
        super().__init__(*args)
        print(f"{self.__class__.__name__}{args}")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"


class Product(MixinLog, BaseProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return self.quantity * self.__price + other.quantity * other.__price
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_info: dict):
        return cls(
            product_info["name"],
            product_info["description"],
            product_info["price"],
            product_info["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            self.__price = "Цена не должна быть нулевая или отрицательная"
        else:
            self.__price = price


class Category:
    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {sum([i.quantity for i in self.__products])} шт."

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    def middle_price(self):
        try:
            return sum(i.price for i in self.__products) // len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        return "\n".join(
            [
                f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт."
                for i in self.__products
            ]
        )


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print(
            "Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством"
        )

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
