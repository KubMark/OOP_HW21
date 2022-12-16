from typing import Dict

from abstract_storage import AbstractStorage
from exceptions import UnknownStorageError, InvalidRequestError


class Request:
    def __init__(self, request_str: str, storages: Dict[str, AbstractStorage]):
        split_request = request_str.lower().split(' ')
        if len(split_request) != 7 or not split_request[1].isdigit():
            raise InvalidRequestError
        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.to = split_request[6]
        self.fromm = split_request[4]

        if self.to not in storages or self.fromm not in storages:
            raise UnknownStorageError
