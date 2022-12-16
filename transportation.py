from typing import Dict
from abstract_storage import AbstractStorage
from request import Request


class Transport:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        self.__fromm: AbstractStorage = storages[self.__request.fromm]
        self.__to: AbstractStorage = storages[self.__request.to]

    def move(self):
        self.__fromm.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забрал {self.__request.amount} {self.__request.product} из {self.__request.fromm}')

        print(f'Курьер везет {self.__request.amount} {self.__request.product}')

        self.__to.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.to}')

    def cancel(self):
        ...
