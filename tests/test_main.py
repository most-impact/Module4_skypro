from typing import Any

import pytest

from src.main import Category, Product


@pytest.fixture()
def product_iphone() -> Any:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product_samsung() -> Any:
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture()
def product_xiaomi() -> Any:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture()
def category_phone(product_iphone: Any, product_samsung: Any) -> Any:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_iphone, product_samsung],
    )


def test_product(product_iphone: Any, product_samsung: Any) -> Any:
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.quantity == 8

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


def test_category(category_phone: Any, product_xiaomi: Any) -> Any:
    assert category_phone.name == "Смартфоны"
    assert (
        category_phone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_phone.category_count == 1
    assert category_phone.product_count == 2

    # testing the add_product function
    category_phone.add_product(product_xiaomi)

    assert category_phone.product_count == 3
    assert category_phone.products == (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        + "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        + "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )


def test_magic_methods_product(product_iphone: Any, product_samsung: Any) -> Any:
    assert str(product_iphone) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product_samsung) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

    assert product_iphone + product_samsung == 2580000.0


def test_magic_methods_category(category_phone: Any) -> Any:
    assert str(category_phone) == "Смартфоны, количество продуктов: 13 шт."
