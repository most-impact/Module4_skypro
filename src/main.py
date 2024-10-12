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
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
