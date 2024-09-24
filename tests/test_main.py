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
def category_phone(product_iphone: Any, product_samsung: Any) -> Any:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_iphone, product_samsung],
    )


def test_product(product_iphone: Any, product_samsung: Any) -> Any:
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_category(category_phone: Any) -> Any:
    assert category_phone.name == "Смартфоны"
    assert (
        category_phone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_phone.category_count == 1
    assert category_phone.product_count == 2
