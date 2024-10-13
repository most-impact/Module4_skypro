from typing import Any

import pytest

from src.main import Category, LawnGrass, Product, Smartphone


@pytest.fixture()
def lawn_grass1() -> Any:
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture()
def smartphone_iphone() -> Any:
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture()
def smartphone_samsung() -> Any:
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture()
def smartphone_xiaomi() -> Any:
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )


@pytest.fixture()
def category_phone(smartphone_iphone: Any, smartphone_samsung: Any) -> Any:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [smartphone_iphone, smartphone_samsung],
    )


def test_error_zero_quantity() -> Any:
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_mixin_log(capfd) -> Any:
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )

    expected_repr = f"Product({product.__dict__})"
    assert repr(product) == expected_repr


def test_lawn_grass(lawn_grass1: Any) -> Any:
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Элитная трава для газона"
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"


def test_product(smartphone_iphone: Any, smartphone_samsung: Any) -> Any:
    assert smartphone_iphone.name == "Iphone 15"
    assert smartphone_iphone.description == "512GB, Gray space"
    assert smartphone_iphone.price == 210000.0
    assert smartphone_iphone.quantity == 8
    assert smartphone_iphone.efficiency == 98.2
    assert smartphone_iphone.color == "Gray space"
    assert smartphone_iphone.memory == 512
    assert smartphone_iphone.model == "15"

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.price == 180000.0
    new_product.price = -100
    assert new_product.price == "Цена не должна быть нулевая или отрицательная"
    new_product.price = 180000.0
    assert smartphone_iphone + smartphone_samsung == 2580000


def test_category(category_phone: Any, smartphone_xiaomi: Any) -> Any:
    assert category_phone.name == "Смартфоны"
    assert (
            category_phone.description
            == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_phone.products == (
            "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
            + "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.")
    assert category_phone.category_count == 1
    assert category_phone.product_count == 2
    assert str(category_phone) == "Смартфоны, количество продуктов: 13 шт."

    # testing the add_product function
    category_phone.add_product(smartphone_xiaomi)

    assert category_phone.product_count == 3
    assert category_phone.products == (
            "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
            + "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
            + "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )

    assert category_phone.middle_price() == 140333
    new_category = Category("Пустая категория", "Категория без продуктов", [])
    assert new_category.middle_price() == 0


def test_magic_methods_product(smartphone_iphone: Any, smartphone_samsung: Any) -> Any:
    assert str(smartphone_iphone) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert (
            str(smartphone_samsung)
            == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )

    assert smartphone_iphone + smartphone_samsung == 2580000.0
