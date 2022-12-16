from typing import Dict

from base_storage import BaseStorage
from exceptions import TooManyDifferentItemsError


class Shop(BaseStorage):
    def __init__(self, items: Dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentItemsError
        super().add(name, amount)
